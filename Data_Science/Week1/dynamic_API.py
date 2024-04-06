import requests

# API 1 : http://universities.hipolabs.com/search?country=india

# LEVEL 1 :
# Print all data in following pattern ( data of all universities ) from above API
# Sr No :___  University name : ___ URL : ___ ( clickable )
# Allow user to enter country name and print all data in following format
# Sr No :___  University name : ___ URL : ___ ( clickable )

# LEVEL 2 :
# 1) Allow user to insert a country name
# 2) Allow user to insert a university name. If a university found - display official link of that university to user.
# otherwise not found

# For example :
# Enter Country name : India  ( user will insert )
# Enter University name : Gujarat Technological University Ahmedabad ( user will insert )
# University found. Visit gtu.ac.in

# Level 1 Que1.
api = requests.get('http://universities.hipolabs.com/search?country=india')
response = api.json()

SrNu = range(0, len(response))
for i in SrNu:
    print('Sr No : ', i + 1, '  University name : ', response[i]['name'], '  URL : ', response[i]['web_pages'][0])

# Level 1 Que2.
api = 'http://universities.hipolabs.com/search?country=' + input()
main_api = requests.get(api)
response = main_api.json()

SrNu = range(0, len(response))
for i in SrNu:
    print('Sr No : ', i + 1, '  University name : ', response[i]['name'], '  URL : ', response[i]['web_pages'][0])

# Level 2 Que1 & Que2.
country_name = input("Enter Country name: ")
api = 'http://universities.hipolabs.com/search?country=' + country_name
main_api = requests.get(api)
response = main_api.json()
if response == []:
    print('!Enter valid country name.')
else:
    university_name = input('Enter University name: ')
    SrNu = range(0, len(response))
    for i in SrNu:
        if response[i]['name'] == university_name:
            print('University found. Visit ', response[i]['web_pages'][0])
            break
    else:
        print('University not found.')

# Example:
# Country -> India,
# University -> University of Health Sciences Andhra Pradesh
# (Found)

# API 2::  https://inshortsapi.vercel.app/news?category=sports

# 1) How many main keys are there in this API? Extract and print all keys.
# 2) How much news are available in this API?
# 3) Print all news in bellow format.

# 1. News content , Author: AUTHOR NAME, DATE: Date of news
# 2. News content , Author: AUTHOR NAME, DATE: Date of news
# 3. News content , Author: AUTHOR NAME, DATE: Date of news

api = requests.get('https://inshortsapi.vercel.app/news?category=sports')
response = api.json()

print('Total main keys in this API is : ', len(response.keys()), ' ', response.keys())
print('Total available news is :', len(response['data']))
SrNu = range(0, len(response['data']))
for i in SrNu:
    print(i + 1, 'News content: ', response['data'][i]['content'], ' Author: ', response['data'][i]['author'],
          ' DATE: ',
          response['data'][i]['date'])

# API 3 : https://api.dictionaryapi.dev/api/v2/entries/en/hello
# https://api.dictionaryapi.dev/api/v2/entries/en/{Your Word}
#
# ( Powerful API for dictionary projects )
# Allow user to insert word. Print meaning of that word.

error = {
    "title": "No Definitions Found",
    "message": "Sorry pal, we couldn't find definitions for the word you were looking for.",
    "resolution": "You can try the search again at later time or head to the web instead."
}

user_input = input("Enter any word: ")
api = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + user_input
main_api = requests.get(api)
response = main_api.json()

if response == error:
    print("Sorry, we couldn't find definitions for the word you were looking for.")
else:
    print('Mining of this word is: ')
    SrNu = range(0, len(response[0]['meanings']))
    for i in SrNu:
        print(i + 1, ' ', response[0]['meanings'][i]['definitions'][0]['definition'])
