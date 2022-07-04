#!/usr/bin/python3
# 2-is_same_class.py
"""Define function that checks if obj isinstance of class."""


def is_same_class(obj, a_class):
    """Function that checks if obj isinstance of a_class.

    Args:
        obj (object): The object
        a_class (class): The class

    Return:
        True: On success
        False: Otherwise
    """
    if isinstance(obj, a_class) == True:
        return (True)
    else:
        return (False)
