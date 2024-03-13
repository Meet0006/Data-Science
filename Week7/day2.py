import pandas as pd
import re

# REGULAR EXPRESSION WITH EXCEL DATA SET
# Download data set CLIENT DATA from  : https://infolabz.in/resources/index.html

# 1) Load excel data in any of variable.
redata = pd.read_excel('clientdata.xlsx')
print(redata)

# 2) Create a column named cibilvalid based on regular expression
# 	validation :  a three-digit score between 300 and 900

CibilScore = []
for i in redata['CibilScore']:
    CibilScore.append(i)

int_str = [str(i) for i in CibilScore]

cibilbothData = []
for j in int_str:
    if re.match('[3-9][0-9][0-9]$', j):
        cibilbothData.append('Valid')
    else:
        cibilbothData.append('Not Valid')

redata['Cibilvalid'] = cibilbothData
print(redata)

# 3) Create a new column named score label
# 	poor average good excellent

scoreData = []
for j in int_str:
    if re.match('[3-4][0-9][0-9]|5[0-4][0-9]', j):  # 300 549
        scoreData.append('Poor')
    elif re.match('5[5-9][0-9]|6[0-4][0-9]', j):  # 550 649
        scoreData.append('Average')
    elif re.match('6[5-9][0-9]|7[0-4][0-9]', j):  # 650 749
        scoreData.append('Good')
    elif re.match('7[5-9][0-9]|8[0-9][0-9]|900', j):  # 750 900
        scoreData.append('Excellent')
    else:
        scoreData.append('Not Valid')

redata['ScoreLabel'] = scoreData
print(redata)

# 4) Email id validation based on regular expressin Create new column Email Validation
store_email = []
for i in redata['Email']:
    store_email.append(i)

valid_email = []
for i in store_email:
    # if re.match('\b[a-z]\b{10}[0-9]/d{10}[^(@gmail.com)]', i):
    # if re.match(r'[a-z0-9]+.[a-z0-9]+@[a-z]+.[a-z]', i):
    if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", i):
        valid_email.append("Valid")
    else:
        valid_email.append('Not Valid')
redata['Email Validation'] = valid_email
print(redata)

# 5) Phone Number validation based on regular expression Create new column mobile number validation
store_phone = []
for i in redata['Mobile']:
    store_phone.append(i)

str_phone = [str(i) for i in store_phone]

valid_phone = []
for i in str_phone:
    if re.match(r"^[6-9][0-9]{9}$", i):
        valid_phone.append("Valid")
    else:
        valid_phone.append('Not Valid')

redata['Phone Validation'] = valid_phone
print(redata)
