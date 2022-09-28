#!/usr/bin/python3
"""Script that takes GitHub credentials and uses the Github API
    to display id
Usage: ./10-my_github.py <username> <password>
"""
import requests
from sys import argv


if __name__ == "__main__":
    payload = {"username": argv[1], "password": argv[2]}

    res = requests.post("https://api.github.com/user", data=payload)
    print(res.text["id"])
