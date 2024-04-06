import requests
import numpy as np
import pandas as pd

# API TO LIST TO SERIES DATA :
api = requests.get('https://data.covid19india.org/data.json')
response = api.json()

# 4) PRINT DATA BASED ON LABEL.


# 1) FETCH EVERYDAY'S CASES FROM COVID API TO LIST
daily_cases = []
for i in range(0, len(response['cases_time_series'])):
    daily_cases.append(int(response['cases_time_series'][i]['dailyconfirmed']))

# print(daily_cases)
numpy_array = np.array(daily_cases)
# print(numpy_array)

# 2) CONVERT IT OT SERIES DATA
SERIES_DATA = pd.Series(numpy_array)
# print(SERIES_DATA)

# 3) ASSIGN LABELS AS BELOW
# a) BELOW 5000 CASES : LOW RISK
# b) 5001 TO 50,000 CASES : MODERATE RISK
# c) 50,001 TO 1,00,000 CASES : HIGH RISK
# d) ABOVE 1 LAC : VERY HIGH RISK

# here I used pandas
# df = pd.DataFrame(daily_cases)
# range = [0, 5000, 50000, 100000, float('inf')]
# labels = ['LOW RISK', 'MODERATE RISK', 'HIGH RISK', 'VERY HIGH RISK']
# df['risk_level'] = pd.cut(df[''], bins=range, labels=labels)
# print(df)

# here I used for loop
# corona_label = []
# for i in SERIES_DATA:
#     if 5000 > i >= 0:
#         corona_label.append('LOW RISK')
#     elif 50000 > i >= 5000:
#         corona_label.append('MODERATE RISK')
#     elif 100000 > i >= 50000:
#         corona_label.append('HIGH RISK')
#     else:
#         corona_label.append('VERY HIGH RISK')
#
# SERIES_DATA.index = corona_label
# print(SERIES_DATA)

# DAY 2 : PANDAS DATA FRAME

# # PYTHON LIST TO DATA FRAME
mydata = [15, 25, 35]

# 1) CONVERT ABOVE LIST TO DATA FRAME pddata
pddata = pd.DataFrame(mydata)

# 2) PRINT DATA FRAME pddata
# print(pddata)

# 3) PRINT TYPE OF DATA FRAME pddata
# print(type(pddata))


# # PYTHON TUPLE TO DATA FRAME
tupledata = (5, 15, 25, 35, 45)

# 1) CONVERT ABOVE LIST TO DATA FRAME pdtuple
pdtuple = pd.DataFrame(tupledata)

# 2) PRINT DATA FRAME pdtuple
# print(pdtuple)

# 3) PRINT TYPE OF DATA FRAME pdtuple
# print(type(pdtuple))


# # PYTHON DICTIONARY TO DATA FRAME
dictdata = {'a': [30], 'b': [40], 'c': [50]}

# 1) CONVERT ABOVE LIST TO DATA FRAME pddict
pddict = pd.DataFrame(dictdata)

# 2) PRINT DATA FRAME pddict
# print(pddict)

# 3) PRINT TYPE OF DATA FRAME pddict
# print(type(pddict))
# ----------------------------------------------------------------------------------------------

# 1) Create a dataframe f manually whose output should be as below. print(f)
f = ([10, 20, 30, np.nan], [40, 50, 60, np.nan], [70, 80, 90, np.nan], [55, 65, 75, 85.0])
fpd = pd.DataFrame(f)
# print(fpd)

# 2) Create a dataframe g manually whose output should be as below when it printed. Print(g)
g = [['ROHIT', 'BATSMAN', 50], ['KOHLI', 'BATSMAN', 80], ['BUMRAH', 'BOWLER', 25]]
gpd = pd.DataFrame(g, columns=['NAME', 'TYPE', 'SCORE'])
# print(gpd)

# 3) Print KOHLI from above data
# print(gpd.iloc[1, 0])

# 4) Print BOWLER from above data
# print(gpd.iloc[2, 1])

# 5) Print 50 from above data
# print(gpd.iloc[0, 2])

# # PRACTICE OF PRINTING, ROW, COLUMN ETC WITH PANDAS
h = pd.DataFrame([[100, 200, 300], [400, 500, 600]], index=["ONE", "TWO"], columns=['A', 'B', 'C'])

# 1) Print above data
# print(h)

# 2) Print third column only
# print(h['C'])

# 3) Print 200 from above data
# print(h.iloc[0, 1])

# 4) Print first row only
# print(h.loc['ONE'])

# 5) Print first element of second column
# print(h['B'][0])
# print(h.iloc[0, 1])

# 6) Print last element of last row ( check above output )
# print(h.iloc[-1, -1])


# Numpy + Pandas

empdata = np.array([[8000, 10000, 18000], [15000, 18000, 25000]])

# 1) Convert above data to pandas dataframe ( employee salary data ) and print dataframe.
emp_dataframe = pd.DataFrame(empdata)
# print(emp_dataframe)

# 2) Add column names 2020,2021,2022 and print data and print dataframe.
emp_colom = pd.DataFrame(empdata, columns=[2020, 2021, 2022])
# print(emp_colom)

# 3) Add row names RAMESH and MAHESH above data and print dataframe.
emp_row = pd.DataFrame(empdata, columns=[2020, 2021, 2022], index=['RAMESH', 'MAHESH'])
# print(emp_row)

# 4) Create a new column (name it ADD ) which should be addition of 2020 and 2021 year's salary and print dataframe.
emp_row['ADD'] = emp_row[[2020, 2021]].sum(axis=1)
# print(emp_row)

# 5) Create a new column which gives total of all years salary provided to employe
# ( name column TOTAL ) and print dataframe.
# emp_row['TOTAL'] = emp_row.sum(axis=1)  # sum of all colom
emp_row['TOTAL'] = emp_row.drop(columns='ADD').sum(axis=1)
# print(emp_row)

# 6) Increment new column 2023, it should be 30% increment in 2022 salary and print dataframe.
emp_row[2023] = emp_row[2022] + (emp_row[2022] * (30 / 100))
# print(emp_row)

# 7) Delete column ADD and print dataframe.
# del emp_row['ADD'] #using del keyword
emp_row = emp_row.drop(columns='ADD')  # using drop keyword
# print(emp_row)

# 8) In 2022 column deduct 1000 rs and print dataframe.
emp_row[2022] = emp_row[2022] - 1000
# print(emp_row)

# 9) Remove employee mahesh and print dataframe.
# emp_row = emp_row.rename(index={'MAHESH': 'MAHESH'})
emp_row = emp_row.drop(index='MAHESH')
# print(emp_row)

# 10) Store final data to excel name it one.xlsx and print dataframe.
emp_row.to_excel('one.xlsx')
