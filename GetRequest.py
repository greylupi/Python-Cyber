import requests

url = '<enterURL>'

response = requests.get(url)

print(response.text)
