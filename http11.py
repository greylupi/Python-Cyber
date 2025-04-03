#same as : curl http://ptl-88022ce7-7360029c.libcurl.so/pentesterlab?key=please --data 'key=please' 

import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]

params = {'key':"please"}
data = {'key':"please"}

response = requests.post(host, params=params, data=data)

print(response.text)