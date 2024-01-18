# Solve following 1 API Question:
# API  : https://isro.vercel.app/api/spacecrafts

# How many main keys are there in above API
# Print name of all main keys
# Print Aryabhata
# Print total number ( count ) of spacecrafts [using length]

import requests

api = requests.get('https://isro.vercel.app/api/spacecrafts')
response = api.json()

print(len(response.keys()))

print(response.keys())

print(response['spacecrafts'][0]['name'])

print(len(response['spacecrafts']))
