import requests

# 1)
# API 1 : https://data.covid19india.org/data.json
# Allow user to insert date. Print new cases , recovered cases , death cases etc.

url = requests.get('https://data.covid19india.org/data.json')
response = url.json()

user_input = input("Enter date : ")
SrNu = range(0, len(response['cases_time_series']))
for i in SrNu:
    if response['cases_time_series'][i]['date'] == user_input:
        print(i, ' :: ', 'Print new cases: ', response['cases_time_series'][i]['dailyconfirmed'],
              ' recovered cases: ', response['cases_time_series'][i]['dailyrecovered'], ' death cases: ',
              response['cases_time_series'][i]['dailydeceased'])
        break
else:
    print("Date not found")

# 2)
# API 2 : https://isro.vercel.app/api/spacecrafts
# Allow user to enter ID. Print that spacecraft’s name
# Allow user to insert name of spacecraft. Print that spacecraft is launched by isro or not.

# ** 1)
url = requests.get('https://isro.vercel.app/api/spacecrafts')
response = url.json()

user_input = int(input("Enter ID: "))
SrNu = range(0, len(response['spacecrafts']))
for i in SrNu:
    if response['spacecrafts'][i]['id'] == user_input:
        print('Spacecraft’s name: ', response['spacecrafts'][i]['name'])

# ** 2)
url = requests.get('https://isro.vercel.app/api/spacecrafts')
response = url.json()

user_input = input("Enter spacecraft: ")
SrNu = range(0, len(response['spacecrafts']))
for i in SrNu:
    if response['spacecrafts'][i]['name'] == user_input:
        print("Spacecraft is launched by isro")
        break
else:
    print("Spacecraft is not launched by isro")

# 3)
# API 3 : https://datausa.io/api/data?drilldowns=Nation&measures=Population
# Allow user to insert year. print population of that year.

url = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
response = url.json()

user_input = input("Enter year: ")
SrNu = range(0, len(response['data']))
for i in SrNu:
    if response['data'][i]['Year'] == user_input:
        print(response['data'][i]['Population'])
else:
    print('Year not exist')

# 4)
# API 4 : http://universities.hipolabs.com/search?country=india
# Allow user to insert university name. Print website of that university.

api = requests.get('http://universities.hipolabs.com/search?country=india')
response = api.json()

userInput = input("Enter university name: ")
for j in response:
    if j['name'] == userInput:
        print(j['web_pages'][0])
        break
else:
    print("University not found")
