#send a GET request to /pentesterlab with the following GET parameter: key with the value please&
#URL-encoding is extremely important to make sure that you are sending the right value or parameter to the server, when using special characters.

# & = %26

#curl 'http://ptl-e52a7ba5-b64ee16d.libcurl.so/pentesterlab?key=please%26'

import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]

params = {'key':"please&"}
#data = {'key':"please"}

response = requests.post(host, params=params)

print(response.text)