# Load live data from API

import requests

url = requests.get('https://jsonplaceholder.typicode.com/comments')
print(type(url))
response = url.json()
print(response[0]['email'])
