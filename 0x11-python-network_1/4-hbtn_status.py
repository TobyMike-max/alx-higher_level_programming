#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import request


if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
