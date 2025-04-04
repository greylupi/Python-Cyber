#curl 'http://ptl-fade2e07-858e72c3.libcurl.so/pentesterlab;pentesterlab'

#This type of request is extremely useful when testing applications with multiple layers of reverse proxies.


import urllib
import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()

host = sys.argv[1]
host = host + ";pentesterlab"

response = requests.get(host)

print(response.text)