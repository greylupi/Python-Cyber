import urllib
import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()

host = sys.argv[1]

headers = {'X-Forwarded-Host': "pentesterlab.com"}

response = requests.get(host, headers=headers)

print(response.text)