# from the cli this could look like this :
# curl <enterurl> -H 'Accept-Language: key-please'
#this sets the content-type

import requests
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]


response = requests.get(host, headers={'Accept-Language':"key-please"})

print(response.text)