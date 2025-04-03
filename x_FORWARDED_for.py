#curl http://ptl-0780b2e8-873dfba9.libcurl.so/pentesterlab -H 'X-Forwarded-For: 1.2.3.4'

import urllib
import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()

host = sys.argv[1]

headers = {'X-Forwarded-For': '1.2.3.4'}

response = requests.get(host, headers=headers)

print(response.text)