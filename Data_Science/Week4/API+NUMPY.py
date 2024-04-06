import requests
import numpy as np

# ADVANCE : API + NUMPY

# Load covid api, store every day’s cases in python list dailydata
api = requests.get('https://data.covid19india.org/data.json')
response = api.json()
dailydata = []
for i in range(0, len(response['cases_time_series'])):
    dailydata.append(int(response['cases_time_series'][i]['dailyconfirmed']))
# print(dailydata)

# Convert python list to numpy array dailynp
dailynp = np.array(dailydata)
# print(dailynp)

# Convert it to 5 rows and 113 matrix
new_matrix = dailynp.reshape(5, 113)
# print(new_matrix)

# Create mask of cases greater or equal to 100000
# numpy_array = []
# new_mask = np.greater_equal(numpy_array, 100000)

# Apply it on dailynp
result = np.greater_equal(dailynp, 100000)
print(dailynp[result])

# Print how many days (count) in india where cases were greater or equal to 1 lac
print(len(dailynp[result]))
