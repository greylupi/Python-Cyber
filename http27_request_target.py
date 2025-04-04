#curl http://ptl-fac15428-6ae5b451.libcurl.so --request-target /pentesterlab#pentesterlab
#curl http://ptl-fac15428-6ae5b451.libcurl.so/pentesterlab%23pentesterlab

import urllib
import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()

host = sys.argv[1]
host = host + "#pentesterlab"

response = requests.get(host)

print(response.text)