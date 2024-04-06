import pandas as pd
import numpy as np

# DATA CLEANING ( MIMP ) WITH PANDAS
# https://infolabz.in/resources/index.html

# 1) Fetch and print all data
newData = pd.read_excel('cleaningset.xlsx')
newdatadf = pd.DataFrame(newData)
# print(newdatadf)

# 2) Print rows and cols ( shape ) of the data
# print(newdatadf.shape)

# 3) Remove entire row if any of the fields are missing
missing_data = newdatadf.dropna()

# 4) Print shape
# print(missing_data.shape)

# 5) Remove entire row only if all fields are missing # Empty row
missing_row = newdatadf.dropna(axis=0, how="all")

# 6) Print shape
# print(missing_row.shape)

# 7) Print all city names without blank
all_city = newdatadf[newdatadf['city'].notnull()]['city']
# print(all_city)

# 8) Print shape
# print(all_city.shape)

# 9) Delete entire column if having all null values
# empty_colum = newdatadf.dropna(axis=1, how='all')
# print(empty_colum)

# 10) Print shape
# print(empty_colum.shape)

# 11) Delete entire column if having any null value
# null_col = newdatadf.dropna(axis=1, how='any')
# print(null_col)

# 12) Print shape
# print(null_col.shape)

# 13) Remove that row is any of email field is blank
# email_row = newdatadf[newdatadf['email'].notnull()]['email']
# email_row = newdatadf['email'].dropna(axis=0, how='any')
# print(email_row)

# 14) Convert all column names to uppar case
# print(newdatadf.columns.str.upper())

# 15) Apply in dataset ( when print data set column names must be in capital )
# newdatadf.columns = newdatadf.columns.str.upper()
# print(newdatadf)

# 16) Rename column name from city to processedcity
# newdatadf.rename(columns={'city': 'Processed City'}, inplace=True)
# print(newdatadf)

# 17) Find if any column having missing values or not. True or False
mi_tr_fa = newdatadf.isnull().any().any()
# print(mi_tr_fa)

# 18) Print any null value in entire data set ( print all columns wise boolean )
# OUTPUT
# Column name 1 False
# Column name 2 True
# Column name 3 False
# print(newdatadf.isnull().any())

# 19) Print sum of null values in each column
sum_col = newdatadf.isnull().sum()
# print(sum_col)

# 20) Print sum of all blank values in entire data frame
# print(newdatadf.isnull().sum().sum())

# 21) Allow user to insert column name. Print count of missing values in that column
# user_input = input("Enter column name: ")
# print(newdatadf[user_input].isnull().sum())

# 22) Allow user to insert column name. Print which index is having missing value.
# user_input = input("Enter column name: ")
# print(np.where(newdatadf[user_input].isnull()))

# 23) Print all rows in which anywhere in entire data rajkot is mentioned
# print((newdatadf[newdatadf.columns] == 'rajkot')) # This line does not work

# 24) Above question in city column only
# print(newdatadf[newdatadf['city'] == 'rajkot'])

# 25) Print all data from Rajkot or age is greate than 50
if newdatadf[newdatadf['city'] == 'rajkot']:
    print(newdatadf[newdatadf['age'] > 50])

# 26) Sort all data by name
# 27) Sort all data by name in descending order
# 28) Print first 2 rows ( without head )
# 29) Print last 2 rows ( without tail )
# 30) Print third and fourth row only
# 31) Fill blank values with 0
# 32) Fill blank values with mean of age
