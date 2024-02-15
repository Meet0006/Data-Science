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
corona_label = []
for i in SERIES_DATA:
    if 5000 > i >= 0:
        corona_label.append('LOW RISK')
    elif 50000 > i >= 5000:
        corona_label.append('MODERATE RISK')
    elif 100000 > i >= 50000:
        corona_label.append('HIGH RISK')
    else:
        corona_label.append('VERY HIGH RISK')

corona_cases = pd.Series(SERIES_DATA, index=[corona_label])
print(corona_cases)
