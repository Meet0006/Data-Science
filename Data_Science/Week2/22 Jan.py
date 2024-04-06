import requests

# TASK 1 :
# API : https://www.gov.uk/bank-holidays.json

api = requests.get('https://www.gov.uk/bank-holidays.json')
response = api.json()

# Print total number ( count ) of main keys
print(len(response.keys()))

# Print all main keys
print(response.keys())

# Print total number ( count ) of holidays mentioned in this API.
main_string = (response['england-and-wales']['events'] + response['scotland']['events'] +
               response['northern-ireland']['events'])
print(len(main_string))

# Allow user to insert date in ( “YYYY-MM-DD” ) format. Print it is holiday or not.

api = requests.get('https://www.gov.uk/bank-holidays.json')
response = api.json()

user_input = input("Enter date in ( “YYYY-MM-DD” ) format: ")

string1 = range(len(response['england-and-wales']['events']))
string2 = range(len(response['scotland']['events']))
string3 = range(len(response['northern-ireland']['events']))


def firstCountry(string1):
    for i in string1:
        bank_holiday1 = response['england-and-wales']['events'][i]['date']
        if user_input == bank_holiday1:
            print('England and Wales has holiday')
            break
    else:
        print('In this day not a holiday')


def secondCountry(string2):
    for i in string2:
        bank_holiday2 = response['scotland']['events'][i]['date']
        if user_input == bank_holiday2:
            print('Scotland has holiday')
            break
    else:
        print('In this day not a holiday')


def thirdCountry(string3):
    for i in string3:
        bank_holiday3 = response['northern-ireland']['events'][i]['date']
        if user_input == bank_holiday3:
            print('Northern-Ireland has holiday')
            break
    else:
        print('In this day not a holiday')


firstCountry(string1)
secondCountry(string2)
thirdCountry(string3)

# Allow user to insert name of holiday print all years date.
# For example user will insert : Good Friday
# Print as below
# 1 2018-03-30
# 2 2019-04-19
# 3 2020-04-10
# If holiday  not found print : no such holiday in this API

api = requests.get('https://www.gov.uk/bank-holidays.json')
response = api.json()

user_input = input("Enter holiday for find dates: ")


def firstCountry(string1):
    for i in string1:
        bank_holiday1 = response['england-and-wales']['events'][i]['title']
        bank_date = response['england-and-wales']['events'][i]['date']
        if user_input == bank_holiday1:
            print(bank_date)
    else:
        print('No such holiday in this API')


def secondCountry(string2):
    for i in string2:
        bank_holiday2 = response['scotland']['events'][i]['title']
        bank_date = response['scotland']['events'][i]['date']
        if user_input == bank_holiday2:
            print(bank_date)
    else:
        print('No such holiday in this API')


def thirdCountry(string3):
    for i in string3:
        bank_holiday3 = response['northern-ireland']['events'][i]['title']
        bank_date = response['northern-ireland']['events'][i]['date']
        if user_input == bank_holiday3:
            print(bank_date)
    else:
        print('No such holiday in this API')


string1 = range(len(response['england-and-wales']['events']))
string2 = range(len(response['scotland']['events']))
string3 = range(len(response['northern-ireland']['events']))

firstCountry(string1)
secondCountry(string2)
thirdCountry(string3)

# Task 2 :
# API : https://isro.vercel.app/api/centres

api = requests.get('https://isro.vercel.app/api/centres')
response = api.json()

# # Print total number ( count ) of centers.
print(len(response['centres']))

# # Allow user to insert name of place ( city ) and print name of the center at that place.
# # If place not found print Center not found.

user_input = input('Enter place name: ')

for i in range(len(response['centres'])):
    if user_input == response['centres'][i]['Place']:
        print(response['centres'][i]['name'])
        break
else:
    print('Center not found.')

# Task 3 :
# API : https://api.postalpincode.in/pincode/380009

# Allow user to insert pin code…
# https://api.postalpincode.in/pincode/{userinput}

user_input = input('Enter pincode:-: ')

url = 'https://api.postalpincode.in/pincode/' + user_input
api = requests.get(url)
response = api.json()

# How many areas ( count ) that falls under this Pincode
print(response[0]['Message'])

# Print name of all areas as Sr No. Area Name. If invalid pincode print:  No records found
if response[0]['Message'] != "No records found":
    for i in range(len(response[0]['PostOffice'])):
        print(i + 1, ' ', response[0]['PostOffice'][i]['Name'])
else:
    print(response[0]['Message'])
