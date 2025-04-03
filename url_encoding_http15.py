#curl 'http://ptl-fec3a20a-4db9b0c9.libcurl.so/pentesterlab?key=pretty%20please'

import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]

#when in python, dont need to url_encode

params = {'key':"pretty please"}
#data = {'key':"please"}

response = requests.post(host, params=params)

print(response.text)