import codecs
import os
import re
import sys

from setuptools import find_packages
from distutils.core import setup
from distutils.command.clean import clean
from distutils.command.build import build

here = os.path.abspath(os.path.dirname(__file__))

class CustomClean(clean):
    """Regular clean and clean documentation"""
    def run(self):
        # call regular clean command
        clean.run(self)
        os.chdir(os.path.join("doc"))
        if not self.dry_run:
            if os.system("make clean") != 0:
                print("'make clean' failed!")
                raise SystemExit(1)

class CustomBuild(build):
    """Regular build along with build of all docs"""
    def run(self):
        # call the regular build
        build.run(self)
        os.chdir(os.path.join("doc"))
        if not self.dry_run:
            if os.system("make all") != 0:
                print ("'make all' failed!")
                raise SystemExit(1)

def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()

packages=find_packages()
print("packages = %s" % packages)

setup(
    name='sarra',
    version='0.1.1',
    description='Subscribe, Acquire, and Re-Advertise products.',
    long_description=(read('README.rst') + '\n\n' +
                      read('CHANGES.txt') + '\n\n' +
                      read('AUTHORS.txt')),
    url='http://metpx.sourceforge.net/',
    license='GPLv2',
    author='Shared Services Canada, Supercomputing, Data Interchange',
    author_email='Peter.Silva@canada.ca',
    packages=find_packages(),
    entry_points={
        "console_scripts":[
              "sr_post=sarra.sr_post:main",
              "sr_log=sarra.sr_log:main",
              "sr_sarra=sarra.sr_sarra:main",
              "sr_sender=sarra.sr_sender:main",
              "sr_watch=sarra.sr_watch:main",
              "sr_subscribe=sarra.sr_subscribe:main",
              "sr_log2source=sarra.sr_log2source:main",
              "sr_log2clusters=sarra.sr_log2clusters:main"
              ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Environment :: Console',
        'Topic :: Communications :: File Sharing',
        'Topic :: Internet :: File Transfer Protocol',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging',
    ],
    cmdclass={ "clean": CustomClean, "build": CustomBuild }
)
