# -*- coding: utf-8 -*-
"""Registers CoreJet-adapter for Robot Framework tests"""

from zope.interface import implementer
from zope.component import adapter, provideAdapter

from robotsuite import RobotTestCase

from corejet.core.interfaces import IStory
from corejet.core.model import Story
from corejet.core.parser import appendScenarios


class RobotStory(Story):
    """Wraps CoreJet story to support the way corejet.testrunner.formatter
    looks up scenarios for test results"""

    # XXX: The following properties are required, because corejet.testrunner
    # wants to getattr(story, caseInfo.test._testMethodName).scenario

    @property
    def runTest(self):
        # this is after the test method name of RobotTestCase
        return self

    @property
    def scenario(self):
        # this returns the only scenario of RobotTestCase
        return self.scenarios[0]


@implementer(IStory)
@adapter(RobotTestCase)
def adaptRobotTestCaseToStory(context):
    """Creates a CoreJet story out of RobotTestCase by concatenating
    steps and parsing the result with appendScenarios."""

    def find_suite(child_suite, default=None):
        """Returns the first test suite, which contains tests."""
        if child_suite.testcase_table.tests:
            return child_suite
        for grandchild in getattr(child_suite, 'children', []):
            first_suite_with_test_cases = find_suite(grandchild)
            if first_suite_with_test_cases:
                return first_suite_with_test_cases
        return default

    suite = find_suite(context._robot_suite, context._robot_suite)
    name, title = (u"", u"")

    for metadata in suite.setting_table.metadata:
        if metadata.name == u"Id":
            name = metadata.value
        elif metadata.name == u"Title":
            title = metadata.value

    story = RobotStory(name, title)
    setattr(story, context._testMethodName, story.runTest)
    source = u""

    for keyword in suite.keyword_table.keywords:
        # here we expect that possible story level steps are described
        # as Background-keyword
        if keyword.name == u"Background":
            for step in keyword.steps:
                source += u"\n".join(step.as_list()) + u"\n"
            source += u"\n"

    for scenario in suite.testcase_table.tests:
        source += u"Scenario: %s\n" % scenario.name
        for step in scenario.steps:
            source += u"\n".join(step.as_list()) + "\n"
        source += "\n"

    appendScenarios(story, source)
    for scenario in story.scenarios:
        # we must prepend scenarios level givens, whens and thens with
        # story level ones to support the behavior of corejet.testrunner
        scenario.givens = story.givens + scenario.givens
        scenario.whens = story.whens + scenario.whens
        scenario.thens = story.thens + scenario.thens
    return story.scenarios and story or None

provideAdapter(adaptRobotTestCaseToStory)
