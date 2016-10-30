#!/usr/bin/env python3
import requests
import sys

API_URL = "http://api.macvendors.com/{}"

if len(sys.argv) < 2:
    print("usage: {0} <mac>".format(sys.argv[0]))
    sys.exit(1)

try:
    r = requests.get(API_URL.format(sys.argv[1]))

    if r.status_code == 200:
            print(r.text)
    else:
        print("[!] Non-200 Status Code")
        print(r.text)
except requests.exceptions.ConnectionError:
    print("[!] Error connecting to Macvendors API")
    sys.exit(1)
