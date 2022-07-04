#!/usr/bin/python3
# 7-base_goemetry.py
"""Defines a class called BaseGeometry."""


class BaseGeometry:
    """A BaseGeometry class that does nothing."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
