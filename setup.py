from setuptools import setup, find_packages

version = "0.5.0"

requires = [
    "setuptools",
    "argparse",
    "robotsuite",
    "corejet.core",
    "corejet.testrunner>=1.0.1",
    "zope.interface",
    "zope.component",
]

setup(name="corejet.robot",
      version=version,
      description="Robot Framework support for CoreJet",
      long_description=open("README.rst").read() + "\n" +
                       open("HISTORY.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords="",
      author="Asko Soukka",
      author_email="asko.soukka@iki.fi",
      url="https://github.com/datakurre/corejet.robot/",
      license="GPL",
      packages=find_packages(exclude=["ez_setup"]),
      namespace_packages=["corejet"],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      corejet2robot = corejet.robot.scripts.corejet2robot:main
      """
      )
