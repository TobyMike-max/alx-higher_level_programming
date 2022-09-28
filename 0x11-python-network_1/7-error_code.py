#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the
    URL and displays the body of the response
Usage: ./7-error_code.py <URL>
"""
from sys import argv
import requests


if __name__ == "__main__":
    res = requests.get(argv[1])
    stat = res.status_code
    if stat >= 400:
        print("Error code: {}".format(stat))
