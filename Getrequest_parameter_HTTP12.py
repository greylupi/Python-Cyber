#URL-encoding is extremely important to make sure that you are sending the right value or parameter to the server, when using special characters.
# curl http://ptl-1d0ab853-a0658f92.libcurl.so/pentesterlab?key==please
#proper encoding: curl http://ptl-1d0ab853-a0658f92.libcurl.so/pentesterlab?key=%3dplease

# %3d is an equal

import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]

params = {'key':"=please"}
#data = {'key':"please"}

response = requests.post(host, params=params)

print(response.text)