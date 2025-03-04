"""Detect information about the system to support contextualization of experimental results."""

import inspect
import os
import platform
import socket
from datetime import datetime
from typing import Dict, List

import psutil

from systemsense import constants, execute, util


def detect() -> Dict[str, str]:
    """Run all of the sub-detects."""
    # execute all of the run functions defined in this module
    # and then return their output in a list of dictionaries
    # that contain a key-value pair where both are a string;
    # with each entry in the list is an output of one run
    run_output: List[Dict[str, str]] = []
    run_output = execute.execute_by_name_filter(
        constants.project.Detect_Module, constants.project.Detect_Filter
    )
    # combine all of the dictionaries into a single dictionary
    return util.union_list_of_dicts(run_output)


def get_battery():
    """Return information about the current power/battery in the system."""
    # TODO: refer to the writing/reflection.md file for
    # an implementation of this function; please replace
    # the "return None" statement with the actual implementation
    return None


def get_cpu() -> Dict[str, str]:
    """Return information about the current CPU in the system."""
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}


def get_cpucores() -> Dict[str, str]:
    """Return information about CPU cores within the system."""
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}


def get_cpufrequencies() -> Dict[str, str]:
    """Return information about CPU frequency for the system."""
    # detect the name of the function in
    # which this source code exists
    function_name = inspect.stack()[0][3]
    # parse out the second part of the name after
    # the underscore character
    function_name = function_name.split("_")[1]
    # create a dictionary with the function's
    # purpose as the key and the value as
    # the return of the function that collects it
    # performing the detection running on an Apple
    # Silicon leads to crashes even with the most
    # recent versions of psutil, thus return no
    # information only on this platform
    # Reference: https://github.com/giampaolo/psutil/issues/1892
    if platform.processor() == constants.system.Arm:
        cpu_freqs_display = "Min: Unknown Mhz, Max: Unknown Mhz"
    # otherwise, perform the detection on all other platforms
    else:
        # try to detect the CPU frequencies and
        # if there is an error, then return a message
        try:
            cpu_freqs = psutil.cpu_freq()
            cpu_freqs_display = (
                f"Min: {cpu_freqs.min} Mhz, Max: {cpu_freqs.max} Mhz"
            )
        # detection of CPU frequencies failed, which is
        # possible for a wide variety of reasons
        except Exception as _:
            cpu_freqs_display = "Min: Unknown Mhz, Max: Unknown Mhz"
    # return the final dictionary with the
    # function's name and the min/max CPU frequencies
    return {function_name: str(cpu_freqs_display)}


def get_datetime() -> Dict[str, str]:
    """Return the current datetime on the system."""
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}


def get_disk() -> Dict[str, str]:
    """Return disk space usage."""
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}


def get_hostname() -> Dict[str, str]:
    """Return the hostname of the system."""
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}


def get_memory() -> Dict[str, str]:
    """Return the hostname of the system."""
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}


def get_platform() -> Dict[str, str]:
    """Return the current platform of the system."""
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}


def get_pythonversion() -> Dict[str, str]:
    """Return the current python version on the system."""
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}


def get_runningprocesses() -> Dict[str, str]:
    """Return the total number of processes running on the system."""
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}


def get_system() -> Dict[str, str]:
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}


def get_systemload() -> Dict[str, str]:
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}


def get_swap():
    """Return information about swap space usage."""
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}


def get_virtualenv():
    """Return the virtual environment hosting this process."""
    # TODO: provide a complete implementation of this function
    function_name = ""
    function_value = ""
    return {function_name: function_value}
