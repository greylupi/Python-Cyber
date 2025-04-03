#curl 'http://ptl-3cd89473-b5721f20.libcurl.so/pentesterlab?key=please%23'

import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]

#when in python, dont need to url_encode

params = {'key':"please" + '\x23'}
#data = {'key':"please"}

response = requests.post(host, params=params)

print(response.text)