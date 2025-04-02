#if using curl the url should be surrounded by quotes.
#domain and key will be asked when script is run.

import requests
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="enter a domain or IP address")
parser.add_argument("key", help="enter a key")
args = parser.parse_args()


url = sys.argv[1]
key = sys.argv[2]

fullRequest = url + "?key=" + key

response = requests.get(fullRequest)

print(response.text)