# 1) Create Histogram from below Data. Add title, x axes, y axes label etc. (Histogram)

from matplotlib import pyplot as plt
import numpy as np
import requests

# stock_price = [100, 111, 120, 125, 130, 135, 145, 160, 155, 180, 187, 165, 170, 174, 170, 160, 155, 157, 148, 145, 155,
#                150, 150, 150, 147, 142, 142]
#
# plt.xlabel('Stock Price')
# plt.ylabel('Year')
# plt.title('Stock Market Price')
# plt.hist(stock_price)
# plt.show()

# 2) scatter plot
# matches = [1, 2, 3, 4, 5]
# rohit = [25, 15, 45, 70, 65]
# kohli = [17, 12, 55, 42, 35]
# dhavan = [10, 47, 23, 17, 94]
# x_axis = np.arange(len(matches))
#
# plt.scatter(matches, rohit, label='rohit', marker='*')
# plt.scatter(matches, kohli, label='kohli', marker='+')
# plt.scatter(matches, dhavan, label='dhavan', marker='^')
# plt.xlabel('Player name')
# plt.ylabel('Average')
# plt.title('Cricket Player Score')
# plt.legend(title='Player name')
# plt.xticks(x_axis + 1, matches)
# plt.show()

# 3)
# Generate bar graph of state vs cases from following dictionary ( json ) data
# Mydata = {'states': ['Maharashtra', 'Gujarat', 'Rajasthan', 'Punjab'], 'cases': [1575, 290, 450, 780]}
# x = Mydata['states']
# y = Mydata['cases']
# plt.bar(x, y)
# plt.xlabel("India's States")
# plt.ylabel('Corona Cases')
# plt.title('Corona Cases in INDIA')
# plt.show()

# 4) Generate pie chart from following data
# Newdata = {"college": "Shree Raviraj",
#            "seats": 890,
#            "branches": 7,
#            "data": [
#                {"name": "CE", "allocated": 90},
#                {"name": "IT", "allocated": 120},
#                {"name": "MECH", "allocated": 40},
#                {"name": "CSE", "allocated": 100},
#                {"name": "CIVIL", "allocated": 70},
#                {"name": "EC", "allocated": 15},
#                {"name": "ELECTRONICS", "allocated": 45}
#            ]
#            }
# x = []
# y = []
# for i in range(0, len(Newdata['data'])):
#     x.append(Newdata['data'][i]['allocated'])
#     y.append(Newdata['data'][i]['name'])
#
# plt.title("Student's sheet")
# plt.pie(x, labels=y, autopct='% .1f %%')
# plt.show()

# 5) Generate Multiple bar graph from below data
# Matchdata = {"Format": "ODI", "MATCHES": 5, "data": [
#     {"Match": "Match 1", "ROHIT": 75, "KOHLI": 21, "DHAVAN": 40},
#     {"Match": "Match 2", "ROHIT": 15, "KOHLI": 111, "DHAVAN": 10},
#     {"Match": "Match 3", "ROHIT": 25, "KOHLI": 4, "DHAVAN": 70},
#     {"Match": "Match 4", "ROHIT": 45, "KOHLI": 15, "DHAVAN": 80},
#     {"Match": "Match 5", "ROHIT": 5, "KOHLI": 78, "DHAVAN": 20},
# ]}
#
# x_axis = np.arange(len(Matchdata['data']))
#
# x = []
# a = []
# b = []
# c = []
#
# for i in range(len(Matchdata['data'])):
#     x.append(Matchdata['data'][i]['Match'])
#     a.append(Matchdata['data'][i]['ROHIT'])
#     b.append(Matchdata['data'][i]['KOHLI'])
#     c.append(Matchdata['data'][i]['DHAVAN'])
#
# l = plt.bar(x_axis - 0.2, a, 0.2, label='ROHIT')
# m = plt.bar(x_axis, b, 0.2, label='KOHLI')
# n = plt.bar(x_axis + 0.2, c, 0.2, label='DHAVAN')
#
# plt.bar_label(l, a)
# plt.bar_label(m, b)
# plt.bar_label(n, c)
#
# plt.title("PLayer's runs multiple bar graph")
# plt.xlabel("Matches")
# plt.ylabel("Player's Score")
# plt.legend(title="Player's Name")
# plt.show()

# 6) API LINK : https://api.rootnet.in/covid19-in/stats/latest
# Develop Horizontal BAR Graph, Y Axes State names, X Axes Confirmed Cases.

# api = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
# response = api.json()
#
# x = []
# y = []
# SrNu = range(len(response['data']['regional']))
#
#
# def addLabel(x, y):
#     for i in SrNu:
#         plt.text(i, x[i], y[i])
#
#
# for i in SrNu:
#     x.append(response['data']['regional'][i]['loc'])
#     y.append(response['data']['regional'][i]['totalConfirmed'])
#
# plt.barh(x, y)
# addLabel(x, y)
# plt.show()

# 7)API LINK : https://data.covid19india.org/data.json
# Develop Horizontal BAR Graph, Y Axes State names, X Axes Confirmed Cases.

# api = requests.get('https://data.covid19india.org/data.json')
# response = api.json()
#
# x = []
# y = []
# SrNu = range(len(response['statewise']))
# print(SrNu)
#
#
# def addLabel(x, y):
#     for i in SrNu:
#         plt.text(i+1, x[i], y[i])
#
#
# for i in SrNu:
#     x.append(response['statewise'][i]['state'])
#     y.append(response['statewise'][i]['confirmed'])
#
# plt.barh(x, y)
# addLabel(x, y)
# plt.show()

# Develop line chart of daily confirmed cases, x axes dates
# ( as total 565 days data are available it won’t be printed properly )
# and y axes confirmed cases on that day.

api = requests.get('https://data.covid19india.org/data.json')
response = api.json()

x = []
y = []
SrNu = range(len(response['cases_time_series']))

for i in SrNu:
    x.append(response['cases_time_series'][i]['dailyconfirmed'])
    y.append(response['cases_time_series'][i]['totalconfirmed'])

plt.plot(x, y)
plt.show()
