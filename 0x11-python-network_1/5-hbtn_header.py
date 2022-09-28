#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./5-hbtn_header.py <URL>
"""
import sys
import request


if __name__ == "__main__":
    url = sys.argv[1]

    r = request.get(url)
    print(r.headers.get("X-Request-Id"))
