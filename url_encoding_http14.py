#curl 'http://ptl-0a45b3e8-c556a871.libcurl.so/pentesterlab?%3fkey=please'

import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]

#when in python, dont need to url_encode

params = {'\x3f' + 'key':"please"}
#data = {'key':"please"}

response = requests.post(host, params=params)

print(response.text)