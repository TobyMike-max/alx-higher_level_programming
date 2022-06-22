#!/usr/bin/python3
# 101-safe_function.py

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The fucntion to execute.
        args: Arguments for fct.

    Return:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        res = fct(*args)
        return (res)
    except Exception as e:
        print("Exception: {}".format(e.__class__), file=sys.stderr)
        return (None)
