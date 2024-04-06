import requests

# 1)
# How many main keys are there in above API
# Print Grindlays Super Saver Income Fund-GSSIF-Half Yearly Dividend
# Print total number ( count ) of mutual fund in above API.

api = requests.get('https://api.mfapi.in/mf')
response = api.json()

print(response[0].keys())
print(response[0]['schemeName'])
print(response[0].items())
print(len(response))

# 2)
# Print total number of main keys ( count )
# Print name of all main keys
# Print disclaimer message and Name of the chart ( using key disclaimer and chartname respectively )
# Print current bitcoin rate in USD

api = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
response = api.json()

print(len(response.keys()))
print(response.keys())
print(response['disclaimer'] + ' ' + response['chartName'])
print(response['bpi']['USD']['rate'])

# 3)
# 1) How many main keys are there in the API ? count ?
# 2) Print names of all main keys.
# 3) Print 2021
# 4) How many years data available ?

api = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
response = api.json()

print(len(response['data'][0].keys()))
print(response['data'][0].keys())
print(response['data'][0]['ID Year'])
print(len(response['data']))

# 4)
# API 4 : http://universities.hipolabs.com/search?country=india
# 1) How many main keys are there ?
# 2) How many universities data is available ?
# 3) Allow user to insert the name of country. Print total number of universities of that country.

api = requests.get('http://universities.hipolabs.com/search?country=india')
response = api.json()

# 1)
print(len(response[0]))

# 2)
print(len(response))

# 3)
api = 'http://universities.hipolabs.com/search?country=' + input()
response = requests.get(api)
MainResponse = response.json()
output = len(MainResponse)
if output == 0:
    print("Country doesn't exist")
else:
    print(output)
