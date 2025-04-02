#in the cli... a post could be like this:
#curl http://ptl-2af4e971-cbb647de.libcurl.so/pentesterlab -X POST --data 'key=please' 

import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]


response = requests.post(host, data={'key':"please"}
                         
print(response.text)