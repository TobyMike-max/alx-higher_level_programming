#!/bin/bash
# Script that displays only the status code of a response from URL request.
curl -s -w "%{http_code}\n" "$1"
