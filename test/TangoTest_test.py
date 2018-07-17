#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the TangoTest project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.
"""Contain the tests for the TANGO Device Server for testing generic clients."""

# Path
import sys
import os
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.insert(0, os.path.abspath(path))

# Imports
from time import sleep
from mock import MagicMock
from PyTango import DevFailed, DevState
from devicetest import DeviceTestCase, main
from TangoTest import TangoTest

# Note:
#
# Since the device uses an inner thread, it is necessary to
# wait during the tests in order the let the device update itself.
# Hence, the sleep calls have to be secured enough not to produce
# any inconsistent behavior. However, the unittests need to run fast.
# Here, we use a factor 3 between the read period and the sleep calls.
#
# Look at devicetest examples for more advanced testing


# Device test case
class TangoTestDeviceTestCase(DeviceTestCase):
    """Test case for packet generation."""
    # PROTECTED REGION ID(TangoTest.test_additionnal_import) ENABLED START #
    # PROTECTED REGION END #    //  TangoTest.test_additionnal_import
    device = TangoTest
    properties = {'Mthreaded_impl': '', 'Sleep_period': '', 'UShort_image_ro_size': '251', 
                  }
    empty = None  # Should be []

    @classmethod
    def mocking(cls):
        """Mock external libraries."""
        # Example : Mock numpy
        # cls.numpy = TangoTest.numpy = MagicMock()
        # PROTECTED REGION ID(TangoTest.test_mocking) ENABLED START #
        # PROTECTED REGION END #    //  TangoTest.test_mocking

    def test_properties(self):
        # test the properties
        # PROTECTED REGION ID(TangoTest.test_properties) ENABLED START #
        # PROTECTED REGION END #    //  TangoTest.test_properties
        pass

    def test_State(self):
        """Test for State"""
        # PROTECTED REGION ID(TangoTest.test_State) ENABLED START #
        self.device.State()
        # PROTECTED REGION END #    //  TangoTest.test_State

    def test_Status(self):
        """Test for Status"""
        # PROTECTED REGION ID(TangoTest.test_Status) ENABLED START #
        self.device.Status()
        # PROTECTED REGION END #    //  TangoTest.test_Status

    def test_CrashFromDevelopperThread(self):
        """Test for CrashFromDevelopperThread"""
        # PROTECTED REGION ID(TangoTest.test_CrashFromDevelopperThread) ENABLED START #
        self.device.CrashFromDevelopperThread()
        # PROTECTED REGION END #    //  TangoTest.test_CrashFromDevelopperThread

    def test_CrashFromOmniThread(self):
        """Test for CrashFromOmniThread"""
        # PROTECTED REGION ID(TangoTest.test_CrashFromOmniThread) ENABLED START #
        self.device.CrashFromOmniThread()
        # PROTECTED REGION END #    //  TangoTest.test_CrashFromOmniThread

    def test_DevBoolean(self):
        """Test for DevBoolean"""
        # PROTECTED REGION ID(TangoTest.test_DevBoolean) ENABLED START #
        self.device.DevBoolean(False)
        # PROTECTED REGION END #    //  TangoTest.test_DevBoolean

    def test_DevDouble(self):
        """Test for DevDouble"""
        # PROTECTED REGION ID(TangoTest.test_DevDouble) ENABLED START #
        self.device.DevDouble(0.0)
        # PROTECTED REGION END #    //  TangoTest.test_DevDouble

    def test_DevFloat(self):
        """Test for DevFloat"""
        # PROTECTED REGION ID(TangoTest.test_DevFloat) ENABLED START #
        self.device.DevFloat(0.0)
        # PROTECTED REGION END #    //  TangoTest.test_DevFloat

    def test_DevLong(self):
        """Test for DevLong"""
        # PROTECTED REGION ID(TangoTest.test_DevLong) ENABLED START #
        self.device.DevLong(0)
        # PROTECTED REGION END #    //  TangoTest.test_DevLong

    def test_DevLong64(self):
        """Test for DevLong64"""
        # PROTECTED REGION ID(TangoTest.test_DevLong64) ENABLED START #
        self.device.DevLong64(0)
        # PROTECTED REGION END #    //  TangoTest.test_DevLong64

    def test_DevShort(self):
        """Test for DevShort"""
        # PROTECTED REGION ID(TangoTest.test_DevShort) ENABLED START #
        self.device.DevShort(0)
        # PROTECTED REGION END #    //  TangoTest.test_DevShort

    def test_DevString(self):
        """Test for DevString"""
        # PROTECTED REGION ID(TangoTest.test_DevString) ENABLED START #
        self.device.DevString("")
        # PROTECTED REGION END #    //  TangoTest.test_DevString

    def test_DevULong(self):
        """Test for DevULong"""
        # PROTECTED REGION ID(TangoTest.test_DevULong) ENABLED START #
        self.device.DevULong(0)
        # PROTECTED REGION END #    //  TangoTest.test_DevULong

    def test_DevULong64(self):
        """Test for DevULong64"""
        # PROTECTED REGION ID(TangoTest.test_DevULong64) ENABLED START #
        self.device.DevULong64(0)
        # PROTECTED REGION END #    //  TangoTest.test_DevULong64

    def test_DevUShort(self):
        """Test for DevUShort"""
        # PROTECTED REGION ID(TangoTest.test_DevUShort) ENABLED START #
        self.device.DevUShort(0)
        # PROTECTED REGION END #    //  TangoTest.test_DevUShort

    def test_DevVarCharArray(self):
        """Test for DevVarCharArray"""
        # PROTECTED REGION ID(TangoTest.test_DevVarCharArray) ENABLED START #
        self.device.DevVarCharArray([0])
        # PROTECTED REGION END #    //  TangoTest.test_DevVarCharArray

    def test_DevVarDoubleArray(self):
        """Test for DevVarDoubleArray"""
        # PROTECTED REGION ID(TangoTest.test_DevVarDoubleArray) ENABLED START #
        self.device.DevVarDoubleArray([0.0])
        # PROTECTED REGION END #    //  TangoTest.test_DevVarDoubleArray

    def test_DevVarDoubleStringArray(self):
        """Test for DevVarDoubleStringArray"""
        # PROTECTED REGION ID(TangoTest.test_DevVarDoubleStringArray) ENABLED START #
        self.device.DevVarDoubleStringArray([[0.0], [""]])
        # PROTECTED REGION END #    //  TangoTest.test_DevVarDoubleStringArray

    def test_DevVarFloatArray(self):
        """Test for DevVarFloatArray"""
        # PROTECTED REGION ID(TangoTest.test_DevVarFloatArray) ENABLED START #
        self.device.DevVarFloatArray([0.0])
        # PROTECTED REGION END #    //  TangoTest.test_DevVarFloatArray

    def test_DevVarLong64Array(self):
        """Test for DevVarLong64Array"""
        # PROTECTED REGION ID(TangoTest.test_DevVarLong64Array) ENABLED START #
        self.device.DevVarLong64Array([0])
        # PROTECTED REGION END #    //  TangoTest.test_DevVarLong64Array

    def test_DevVarLongArray(self):
        """Test for DevVarLongArray"""
        # PROTECTED REGION ID(TangoTest.test_DevVarLongArray) ENABLED START #
        self.device.DevVarLongArray([0])
        # PROTECTED REGION END #    //  TangoTest.test_DevVarLongArray

    def test_DevVarLongStringArray(self):
        """Test for DevVarLongStringArray"""
        # PROTECTED REGION ID(TangoTest.test_DevVarLongStringArray) ENABLED START #
        self.device.DevVarLongStringArray([[0], [""]])
        # PROTECTED REGION END #    //  TangoTest.test_DevVarLongStringArray

    def test_DevVarShortArray(self):
        """Test for DevVarShortArray"""
        # PROTECTED REGION ID(TangoTest.test_DevVarShortArray) ENABLED START #
        self.device.DevVarShortArray([0])
        # PROTECTED REGION END #    //  TangoTest.test_DevVarShortArray

    def test_DevVarStringArray(self):
        """Test for DevVarStringArray"""
        # PROTECTED REGION ID(TangoTest.test_DevVarStringArray) ENABLED START #
        self.device.DevVarStringArray([""])
        # PROTECTED REGION END #    //  TangoTest.test_DevVarStringArray

    def test_DevVarULong64Array(self):
        """Test for DevVarULong64Array"""
        # PROTECTED REGION ID(TangoTest.test_DevVarULong64Array) ENABLED START #
        self.device.DevVarULong64Array([0])
        # PROTECTED REGION END #    //  TangoTest.test_DevVarULong64Array

    def test_DevVarULongArray(self):
        """Test for DevVarULongArray"""
        # PROTECTED REGION ID(TangoTest.test_DevVarULongArray) ENABLED START #
        self.device.DevVarULongArray([0])
        # PROTECTED REGION END #    //  TangoTest.test_DevVarULongArray

    def test_DevVarUShortArray(self):
        """Test for DevVarUShortArray"""
        # PROTECTED REGION ID(TangoTest.test_DevVarUShortArray) ENABLED START #
        self.device.DevVarUShortArray([0])
        # PROTECTED REGION END #    //  TangoTest.test_DevVarUShortArray

    def test_DevVoid(self):
        """Test for DevVoid"""
        # PROTECTED REGION ID(TangoTest.test_DevVoid) ENABLED START #
        self.device.DevVoid()
        # PROTECTED REGION END #    //  TangoTest.test_DevVoid

    def test_DumpExecutionState(self):
        """Test for DumpExecutionState"""
        # PROTECTED REGION ID(TangoTest.test_DumpExecutionState) ENABLED START #
        self.device.DumpExecutionState()
        # PROTECTED REGION END #    //  TangoTest.test_DumpExecutionState

    def test_SwitchStates(self):
        """Test for SwitchStates"""
        # PROTECTED REGION ID(TangoTest.test_SwitchStates) ENABLED START #
        self.device.SwitchStates()
        # PROTECTED REGION END #    //  TangoTest.test_SwitchStates

    def test_ampli(self):
        """Test for ampli"""
        # PROTECTED REGION ID(TangoTest.test_ampli) ENABLED START #
        self.device.ampli
        # PROTECTED REGION END #    //  TangoTest.test_ampli

    def test_boolean_scalar(self):
        """Test for boolean_scalar"""
        # PROTECTED REGION ID(TangoTest.test_boolean_scalar) ENABLED START #
        self.device.boolean_scalar
        # PROTECTED REGION END #    //  TangoTest.test_boolean_scalar

    def test_double_scalar(self):
        """Test for double_scalar"""
        # PROTECTED REGION ID(TangoTest.test_double_scalar) ENABLED START #
        self.device.double_scalar
        # PROTECTED REGION END #    //  TangoTest.test_double_scalar

    def test_double_scalar_rww(self):
        """Test for double_scalar_rww"""
        # PROTECTED REGION ID(TangoTest.test_double_scalar_rww) ENABLED START #
        self.device.double_scalar_rww
        # PROTECTED REGION END #    //  TangoTest.test_double_scalar_rww

    def test_double_scalar_w(self):
        """Test for double_scalar_w"""
        # PROTECTED REGION ID(TangoTest.test_double_scalar_w) ENABLED START #
        self.device.double_scalar_w
        # PROTECTED REGION END #    //  TangoTest.test_double_scalar_w

    def test_float_scalar(self):
        """Test for float_scalar"""
        # PROTECTED REGION ID(TangoTest.test_float_scalar) ENABLED START #
        self.device.float_scalar
        # PROTECTED REGION END #    //  TangoTest.test_float_scalar

    def test_long64_scalar(self):
        """Test for long64_scalar"""
        # PROTECTED REGION ID(TangoTest.test_long64_scalar) ENABLED START #
        self.device.long64_scalar
        # PROTECTED REGION END #    //  TangoTest.test_long64_scalar

    def test_long_scalar(self):
        """Test for long_scalar"""
        # PROTECTED REGION ID(TangoTest.test_long_scalar) ENABLED START #
        self.device.long_scalar
        # PROTECTED REGION END #    //  TangoTest.test_long_scalar

    def test_long_scalar_rww(self):
        """Test for long_scalar_rww"""
        # PROTECTED REGION ID(TangoTest.test_long_scalar_rww) ENABLED START #
        self.device.long_scalar_rww
        # PROTECTED REGION END #    //  TangoTest.test_long_scalar_rww

    def test_long_scalar_w(self):
        """Test for long_scalar_w"""
        # PROTECTED REGION ID(TangoTest.test_long_scalar_w) ENABLED START #
        self.device.long_scalar_w
        # PROTECTED REGION END #    //  TangoTest.test_long_scalar_w

    def test_no_value(self):
        """Test for no_value"""
        # PROTECTED REGION ID(TangoTest.test_no_value) ENABLED START #
        self.device.no_value
        # PROTECTED REGION END #    //  TangoTest.test_no_value

    def test_short_scalar(self):
        """Test for short_scalar"""
        # PROTECTED REGION ID(TangoTest.test_short_scalar) ENABLED START #
        self.device.short_scalar
        # PROTECTED REGION END #    //  TangoTest.test_short_scalar

    def test_short_scalar_ro(self):
        """Test for short_scalar_ro"""
        # PROTECTED REGION ID(TangoTest.test_short_scalar_ro) ENABLED START #
        self.device.short_scalar_ro
        # PROTECTED REGION END #    //  TangoTest.test_short_scalar_ro

    def test_short_scalar_rww(self):
        """Test for short_scalar_rww"""
        # PROTECTED REGION ID(TangoTest.test_short_scalar_rww) ENABLED START #
        self.device.short_scalar_rww
        # PROTECTED REGION END #    //  TangoTest.test_short_scalar_rww

    def test_short_scalar_w(self):
        """Test for short_scalar_w"""
        # PROTECTED REGION ID(TangoTest.test_short_scalar_w) ENABLED START #
        self.device.short_scalar_w
        # PROTECTED REGION END #    //  TangoTest.test_short_scalar_w

    def test_string_scalar(self):
        """Test for string_scalar"""
        # PROTECTED REGION ID(TangoTest.test_string_scalar) ENABLED START #
        self.device.string_scalar
        # PROTECTED REGION END #    //  TangoTest.test_string_scalar

    def test_throw_exception(self):
        """Test for throw_exception"""
        # PROTECTED REGION ID(TangoTest.test_throw_exception) ENABLED START #
        self.device.throw_exception
        # PROTECTED REGION END #    //  TangoTest.test_throw_exception

    def test_uchar_scalar(self):
        """Test for uchar_scalar"""
        # PROTECTED REGION ID(TangoTest.test_uchar_scalar) ENABLED START #
        self.device.uchar_scalar
        # PROTECTED REGION END #    //  TangoTest.test_uchar_scalar

    def test_ulong64_scalar(self):
        """Test for ulong64_scalar"""
        # PROTECTED REGION ID(TangoTest.test_ulong64_scalar) ENABLED START #
        self.device.ulong64_scalar
        # PROTECTED REGION END #    //  TangoTest.test_ulong64_scalar

    def test_ushort_scalar(self):
        """Test for ushort_scalar"""
        # PROTECTED REGION ID(TangoTest.test_ushort_scalar) ENABLED START #
        self.device.ushort_scalar
        # PROTECTED REGION END #    //  TangoTest.test_ushort_scalar

    def test_ulong_scalar(self):
        """Test for ulong_scalar"""
        # PROTECTED REGION ID(TangoTest.test_ulong_scalar) ENABLED START #
        self.device.ulong_scalar
        # PROTECTED REGION END #    //  TangoTest.test_ulong_scalar

    def test_boolean_spectrum(self):
        """Test for boolean_spectrum"""
        # PROTECTED REGION ID(TangoTest.test_boolean_spectrum) ENABLED START #
        self.device.boolean_spectrum
        # PROTECTED REGION END #    //  TangoTest.test_boolean_spectrum

    def test_boolean_spectrum_ro(self):
        """Test for boolean_spectrum_ro"""
        # PROTECTED REGION ID(TangoTest.test_boolean_spectrum_ro) ENABLED START #
        self.device.boolean_spectrum_ro
        # PROTECTED REGION END #    //  TangoTest.test_boolean_spectrum_ro

    def test_double_spectrum(self):
        """Test for double_spectrum"""
        # PROTECTED REGION ID(TangoTest.test_double_spectrum) ENABLED START #
        self.device.double_spectrum
        # PROTECTED REGION END #    //  TangoTest.test_double_spectrum

    def test_double_spectrum_ro(self):
        """Test for double_spectrum_ro"""
        # PROTECTED REGION ID(TangoTest.test_double_spectrum_ro) ENABLED START #
        self.device.double_spectrum_ro
        # PROTECTED REGION END #    //  TangoTest.test_double_spectrum_ro

    def test_float_spectrum(self):
        """Test for float_spectrum"""
        # PROTECTED REGION ID(TangoTest.test_float_spectrum) ENABLED START #
        self.device.float_spectrum
        # PROTECTED REGION END #    //  TangoTest.test_float_spectrum

    def test_float_spectrum_ro(self):
        """Test for float_spectrum_ro"""
        # PROTECTED REGION ID(TangoTest.test_float_spectrum_ro) ENABLED START #
        self.device.float_spectrum_ro
        # PROTECTED REGION END #    //  TangoTest.test_float_spectrum_ro

    def test_long64_spectrum_ro(self):
        """Test for long64_spectrum_ro"""
        # PROTECTED REGION ID(TangoTest.test_long64_spectrum_ro) ENABLED START #
        self.device.long64_spectrum_ro
        # PROTECTED REGION END #    //  TangoTest.test_long64_spectrum_ro

    def test_long_spectrum(self):
        """Test for long_spectrum"""
        # PROTECTED REGION ID(TangoTest.test_long_spectrum) ENABLED START #
        self.device.long_spectrum
        # PROTECTED REGION END #    //  TangoTest.test_long_spectrum

    def test_long_spectrum_ro(self):
        """Test for long_spectrum_ro"""
        # PROTECTED REGION ID(TangoTest.test_long_spectrum_ro) ENABLED START #
        self.device.long_spectrum_ro
        # PROTECTED REGION END #    //  TangoTest.test_long_spectrum_ro

    def test_short_spectrum(self):
        """Test for short_spectrum"""
        # PROTECTED REGION ID(TangoTest.test_short_spectrum) ENABLED START #
        self.device.short_spectrum
        # PROTECTED REGION END #    //  TangoTest.test_short_spectrum

    def test_short_spectrum_ro(self):
        """Test for short_spectrum_ro"""
        # PROTECTED REGION ID(TangoTest.test_short_spectrum_ro) ENABLED START #
        self.device.short_spectrum_ro
        # PROTECTED REGION END #    //  TangoTest.test_short_spectrum_ro

    def test_string_spectrum(self):
        """Test for string_spectrum"""
        # PROTECTED REGION ID(TangoTest.test_string_spectrum) ENABLED START #
        self.device.string_spectrum
        # PROTECTED REGION END #    //  TangoTest.test_string_spectrum

    def test_string_spectrum_ro(self):
        """Test for string_spectrum_ro"""
        # PROTECTED REGION ID(TangoTest.test_string_spectrum_ro) ENABLED START #
        self.device.string_spectrum_ro
        # PROTECTED REGION END #    //  TangoTest.test_string_spectrum_ro

    def test_uchar_spectrum(self):
        """Test for uchar_spectrum"""
        # PROTECTED REGION ID(TangoTest.test_uchar_spectrum) ENABLED START #
        self.device.uchar_spectrum
        # PROTECTED REGION END #    //  TangoTest.test_uchar_spectrum

    def test_uchar_spectrum_ro(self):
        """Test for uchar_spectrum_ro"""
        # PROTECTED REGION ID(TangoTest.test_uchar_spectrum_ro) ENABLED START #
        self.device.uchar_spectrum_ro
        # PROTECTED REGION END #    //  TangoTest.test_uchar_spectrum_ro

    def test_ulong64_spectrum_ro(self):
        """Test for ulong64_spectrum_ro"""
        # PROTECTED REGION ID(TangoTest.test_ulong64_spectrum_ro) ENABLED START #
        self.device.ulong64_spectrum_ro
        # PROTECTED REGION END #    //  TangoTest.test_ulong64_spectrum_ro

    def test_ulong_spectrum_ro(self):
        """Test for ulong_spectrum_ro"""
        # PROTECTED REGION ID(TangoTest.test_ulong_spectrum_ro) ENABLED START #
        self.device.ulong_spectrum_ro
        # PROTECTED REGION END #    //  TangoTest.test_ulong_spectrum_ro

    def test_ushort_spectrum(self):
        """Test for ushort_spectrum"""
        # PROTECTED REGION ID(TangoTest.test_ushort_spectrum) ENABLED START #
        self.device.ushort_spectrum
        # PROTECTED REGION END #    //  TangoTest.test_ushort_spectrum

    def test_ushort_spectrum_ro(self):
        """Test for ushort_spectrum_ro"""
        # PROTECTED REGION ID(TangoTest.test_ushort_spectrum_ro) ENABLED START #
        self.device.ushort_spectrum_ro
        # PROTECTED REGION END #    //  TangoTest.test_ushort_spectrum_ro

    def test_wave(self):
        """Test for wave"""
        # PROTECTED REGION ID(TangoTest.test_wave) ENABLED START #
        self.device.wave
        # PROTECTED REGION END #    //  TangoTest.test_wave

    def test_boolean_image(self):
        """Test for boolean_image"""
        # PROTECTED REGION ID(TangoTest.test_boolean_image) ENABLED START #
        self.device.boolean_image
        # PROTECTED REGION END #    //  TangoTest.test_boolean_image

    def test_boolean_image_ro(self):
        """Test for boolean_image_ro"""
        # PROTECTED REGION ID(TangoTest.test_boolean_image_ro) ENABLED START #
        self.device.boolean_image_ro
        # PROTECTED REGION END #    //  TangoTest.test_boolean_image_ro

    def test_double_image(self):
        """Test for double_image"""
        # PROTECTED REGION ID(TangoTest.test_double_image) ENABLED START #
        self.device.double_image
        # PROTECTED REGION END #    //  TangoTest.test_double_image

    def test_double_image_ro(self):
        """Test for double_image_ro"""
        # PROTECTED REGION ID(TangoTest.test_double_image_ro) ENABLED START #
        self.device.double_image_ro
        # PROTECTED REGION END #    //  TangoTest.test_double_image_ro

    def test_float_image(self):
        """Test for float_image"""
        # PROTECTED REGION ID(TangoTest.test_float_image) ENABLED START #
        self.device.float_image
        # PROTECTED REGION END #    //  TangoTest.test_float_image

    def test_float_image_ro(self):
        """Test for float_image_ro"""
        # PROTECTED REGION ID(TangoTest.test_float_image_ro) ENABLED START #
        self.device.float_image_ro
        # PROTECTED REGION END #    //  TangoTest.test_float_image_ro

    def test_long64_image_ro(self):
        """Test for long64_image_ro"""
        # PROTECTED REGION ID(TangoTest.test_long64_image_ro) ENABLED START #
        self.device.long64_image_ro
        # PROTECTED REGION END #    //  TangoTest.test_long64_image_ro

    def test_long_image(self):
        """Test for long_image"""
        # PROTECTED REGION ID(TangoTest.test_long_image) ENABLED START #
        self.device.long_image
        # PROTECTED REGION END #    //  TangoTest.test_long_image

    def test_long_image_ro(self):
        """Test for long_image_ro"""
        # PROTECTED REGION ID(TangoTest.test_long_image_ro) ENABLED START #
        self.device.long_image_ro
        # PROTECTED REGION END #    //  TangoTest.test_long_image_ro

    def test_short_image(self):
        """Test for short_image"""
        # PROTECTED REGION ID(TangoTest.test_short_image) ENABLED START #
        self.device.short_image
        # PROTECTED REGION END #    //  TangoTest.test_short_image

    def test_short_image_ro(self):
        """Test for short_image_ro"""
        # PROTECTED REGION ID(TangoTest.test_short_image_ro) ENABLED START #
        self.device.short_image_ro
        # PROTECTED REGION END #    //  TangoTest.test_short_image_ro

    def test_string_image(self):
        """Test for string_image"""
        # PROTECTED REGION ID(TangoTest.test_string_image) ENABLED START #
        self.device.string_image
        # PROTECTED REGION END #    //  TangoTest.test_string_image

    def test_string_image_ro(self):
        """Test for string_image_ro"""
        # PROTECTED REGION ID(TangoTest.test_string_image_ro) ENABLED START #
        self.device.string_image_ro
        # PROTECTED REGION END #    //  TangoTest.test_string_image_ro

    def test_uchar_image(self):
        """Test for uchar_image"""
        # PROTECTED REGION ID(TangoTest.test_uchar_image) ENABLED START #
        self.device.uchar_image
        # PROTECTED REGION END #    //  TangoTest.test_uchar_image

    def test_uchar_image_ro(self):
        """Test for uchar_image_ro"""
        # PROTECTED REGION ID(TangoTest.test_uchar_image_ro) ENABLED START #
        self.device.uchar_image_ro
        # PROTECTED REGION END #    //  TangoTest.test_uchar_image_ro

    def test_ulong64_image_ro(self):
        """Test for ulong64_image_ro"""
        # PROTECTED REGION ID(TangoTest.test_ulong64_image_ro) ENABLED START #
        self.device.ulong64_image_ro
        # PROTECTED REGION END #    //  TangoTest.test_ulong64_image_ro

    def test_ulong_image_ro(self):
        """Test for ulong_image_ro"""
        # PROTECTED REGION ID(TangoTest.test_ulong_image_ro) ENABLED START #
        self.device.ulong_image_ro
        # PROTECTED REGION END #    //  TangoTest.test_ulong_image_ro

    def test_ushort_image(self):
        """Test for ushort_image"""
        # PROTECTED REGION ID(TangoTest.test_ushort_image) ENABLED START #
        self.device.ushort_image
        # PROTECTED REGION END #    //  TangoTest.test_ushort_image

    def test_ushort_image_ro(self):
        """Test for ushort_image_ro"""
        # PROTECTED REGION ID(TangoTest.test_ushort_image_ro) ENABLED START #
        self.device.ushort_image_ro
        # PROTECTED REGION END #    //  TangoTest.test_ushort_image_ro


# Main execution
if __name__ == "__main__":
    main()
