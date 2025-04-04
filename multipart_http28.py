#curl http://ptl-afd095ab-891701d5.libcurl.so/pentesterlab -H "Content-Type: multipart/form-data"



import urllib
import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()

host = sys.argv[1]
headers = {'Content-Type': 'multipart/form-data'}

response = requests.get(host, headers=headers)

print(response.text)