#This send a get request with POST parameters
#curl http://ptl-549bcd73-4fb1b5a8.libcurl.so/pentesterlab --data 'key=please' -X GET

import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]


response = requests.get(host, data={'key':"please"})

print(response.text)