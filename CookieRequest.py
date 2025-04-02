# from the cli this could look like this :
# curl http://ptl-5b154091-ec187f5f.libcurl.so/pentesterlab -H 'Cookie: key=please'
#this sends a cookie to the site

import requests
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
#parser.add_argument("key", help="enter a key")
args = parser.parse_args()


host = sys.argv[1]
#key = sys.argv[2]


response = requests.get(host, headers={'Cookie':"key=please"})

print(response.text)