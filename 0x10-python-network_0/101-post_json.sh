#!/bin/bash
# Script that sends a JSON POST request and displays response body
curl -s -X POST -d @"$2" "$1"
