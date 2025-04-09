#curl http://ptl-c047bbfb-c6c6d9d4.libcurl.so/pentesterlab -X POST --data '<key><value>please</value></key>'


import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]
data = '<key><value>please</value></key>'

response = requests.post(host, data=data)

print(response.text)