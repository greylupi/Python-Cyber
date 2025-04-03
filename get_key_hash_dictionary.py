#curl "http://ptl-8eeef5d8-b9ae76ad.libcurl.so/pentesterlab?key\[please\]=1"

import urllib
import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]

params = {'key[please]': '1'}

response = requests.get(host, params=params)

print(response.text)