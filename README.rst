Robot Framework support for CoreJet
===================================

Currently, pretty simple one.

Depends on `robotsuite`_.

.. _robotsuite: http://github.com/datakurre/robotsuite/


Generating test skeletons
-------------------------

``corejet.robot`` ships with an XSLT stylesheet for generating test skeletons
for Python unittest. If you are using buildout, you can install a helper
script for executing the XSLT-transformation with::

    [corejet2robot]
    recipe = zc.recipe.rgg
    eggs = corejet.robot
    scripts = corejet2robot

And execute it with::

    bin/corejet2robot path/to/corejet.xml

Try ``bin/corejet2robot --help`` for more information.
