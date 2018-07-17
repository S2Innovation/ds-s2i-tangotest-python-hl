# -*- coding: utf-8 -*-
#
# This file is part of the TangoTest project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

"""TANGO Device Server for testing generic clients

A device to test generic clients. It offers a \``echo\`` like command for
each TANGO data type (i.e. each command returns an exact copy of <argin>).
"""

from . import release
from .TangoTest import TangoTest, main

__version__ = release.version
__version_info__ = release.version_info
__author__ = release.author
