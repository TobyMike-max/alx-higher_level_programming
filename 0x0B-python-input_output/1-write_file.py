#!/usr/bin/python3
# 1-write_file.py
"""Defines a function that writes to a text file."""


def read_file(filename="", text=""):
    with open(filename, r+, encoding="utf-8") as f:
        return (f.write(text))
