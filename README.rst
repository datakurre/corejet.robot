Robot Framework support for CoreJet
===================================

A work in progress. Has rough edges. Depends on `robotsuite`_.

Is auto-imported by ``corejet.testrunner >= 1.0.1`` just before
the generation of CoreJet test report (until a better way for
plugins is discovered).
Provides IStory-adapter for ``robotsuite``'s *RobotTestCase* to do the magic.

.. _robotsuite: http://github.com/datakurre/robotsuite/


Generating test skeletons
-------------------------

``corejet.robot`` ships with an XSLT stylesheet for generating test skeletons
for Python unittest. If you are using buildout, you can install a helper
script for executing the XSLT-transformation with::

    [corejet2robot]
    recipe = zc.recipe.egg
    eggs = corejet.robot
    scripts = corejet2robot

And execute it with::

    bin/corejet2robot path/to/corejet.xml

Try ``bin/corejet2robot --help`` for more information.
