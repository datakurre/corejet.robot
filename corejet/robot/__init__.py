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

    suite = context._robot_suite
    name, title = (None, None)

    for metadata in suite.setting_table.metadata:
        if metadata.name == u"Id":
            name = metadata.value
        elif metadata.name == u"Name":
            title = metadata.value

    story = RobotStory(name, title)
    source = u""

    for keyword in suite.keyword_table.keywords:
        # here we expect that possible story level steps are described
        # as Background-keyword
        if keyword.name == u"Background":
            for step in keyword.steps:
                source += u"  ".join(step.as_list()) + u"\n"
            source += u"\n"

    for scenario in suite.testcase_table.tests:
        source += u"Scenario: %s\n" % scenario.name
        for step in scenario.steps:
            source += "  ".join(step.as_list()) + "\n"
        source += "\n"

    appendScenarios(story, source)
    return story

provideAdapter(adaptRobotTestCaseToStory)
