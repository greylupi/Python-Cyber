#curl 'http://ptl-68e4c25a-71287f4b.libcurl.so/pentesterlab?key=please%2500'

import urllib
import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]
path = "%00"

code = urllib.parse.quote(path)

params = {'key':"please" + code}

response = requests.get(host, params=params)

print(response.text)
