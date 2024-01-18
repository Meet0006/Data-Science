import requests

# API 1 : https://api.mfapi.in/mf
# Print all data in following pattern ( data of all mutualfunds )
# ( Sr no: ____ , Mutual fund Scheme name : ___ Mutual Fund Scheme code : ___ )

url = requests.get('https://api.mfapi.in/mf')
response = url.json()

SrNo = range(1, len(response))
for i in SrNo:
    print('Sr no: ', i, 'Mutual fund Scheme name : ', response[i]['schemeName'], ' Mutual Fund Scheme code : ',
          response[i]['schemeCode'])

# API 2 : https://datausa.io/api/data?drilldowns=Nation&measures=Population
# Print all data in following pattern ( Year in Ascending format : means 2013 first )
# ( Sr no: ____ , Year : ___ Population : ___ )

url = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
response = url.json()

SrNo = range(0, len(response['data']))
for i in SrNo:
    print('Sr no: ', i + 1, 'Year : ', response['data'][-i - 1]['Year'], ' Population : ',
          response['data'][i]['Population'])

# API 3 : http://universities.hipolabs.com/search?country=india
# Print all data in following pattern ( data of all universities )
# Sr No :___  University name : ___ URL : ___ ( clickable )
# Allow user to enter country name and print all data in following format
# Sr No :___  University name : ___ URL : ___ ( clickable )

url = requests.get('http://universities.hipolabs.com/search?country=india')
response = url.json()

SrNo = range(0, len(response))
for i in SrNo:
    print('Sr No : ', i + 1, '  University name : ', response[i]['name'], ' URL : ', response[i]['web_pages'][0])


def uniList():
    SrNo = range(0, len(response))
    for i in SrNo:
        print('Sr No : ', i + 1, '  University name : ', response[i]['name'], ' URL : ',
              response[i]['web_pages'][0])


userInput = input("Enter country name: ")
for j in response:
    if j['country'] == userInput:
        uniList()
        break
    else:
        print("Country not found")
        break
