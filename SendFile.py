#curl http://ptl-c52bdb37-47699438.libcurl.so/pentesterlab -F "filename=@filename"

import urllib
import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()

host = sys.argv[1]
#headers = {'Content-Type': 'multipart/form-data'}
files = {'filename':'atleastonebyte'}

response = requests.get(host, files=files)

print(response.text)