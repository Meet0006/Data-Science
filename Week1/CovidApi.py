# https://data.covid19india.org/data.json

import requests

url = requests.get('https://data.covid19india.org/data.json')
response = url.json()

# All keys and number of keys
# print(response.keys())
# print(len(response))

# print(response['cases_time_series'][0]["date"])

# print(response['statewise'][1]['state'])

# print(len(response['tested']))

# print(len(response['statewise']))
