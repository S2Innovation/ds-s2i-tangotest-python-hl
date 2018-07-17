#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the TangoTest project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

import os
import sys
from setuptools import setup

setup_dir = os.path.dirname(os.path.abspath(__file__))

# make sure we use latest info from local code
sys.path.insert(0, setup_dir)

readme_filename = os.path.join(setup_dir, 'README.rst')
with open(readme_filename) as file:
    long_description = file.read()

release_filename = os.path.join(setup_dir, 'TangoTest', 'release.py')
exec(open(release_filename).read())

pack = ['TangoTest']

setup(name=name,
      version=version,
      description='A device to test generic clients. It offers a \``echo\`` like command for\neach TANGO data type (i.e. each command returns an exact copy of <argin>).',
      packages=pack,
      include_package_data=True,
      test_suite="test",
      entry_points={'console_scripts':['TangoTest = TangoTest:main']},
      author='tango',
      author_email='tango at esrf.fr',
      license='GPL',
      long_description=long_description,
      url='www.tango-controls.org',
      platforms="All Platforms"
      )
