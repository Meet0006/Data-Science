import pandas as pd
import numpy as np
import xlrd

# LIST TO SERIES DATA
mylist = [1, 2, 3, 4, 5]

# # 1) print above list
# print(mylist)
#
# # 2) print type of above list
# print(type(mylist))
#
# # 3) print length of above list
# print(len(mylist))
#
# # 4) convert above data in series data and store in mydata variable
# mydata = pd.Series(mylist)
#
# # 5) print mydata
# print(mydata)
#
# # 6) print type of mydata
# print(type(mydata))

# TUPLE TO PANDAS SERIES DATA
mytuple = (10, 20, 30, 40, 50)

# # 1) convert above tuple to pandas series data name it sdtuple
# sdtuple = pd.Series(mytuple)
#
# # 2) print sdtuple
# print(sdtuple)
#
# # 3) print type of sdtuple
# print(type(sdtuple))

# DICTIONARY TO SERIES DATA
mydict = {"a": 1, "b": 2, "c": 3}

# 1) Convert above dictionary to series data addict
# sddict = pd.Series(mydict)
#
# # 2) print sddict
# print(sddict)
#
# # 3) print type sddict
# print(type(sddict))

newdata = [15, 17, 12, 10, 5, 17, 18, 9]

# # 1) add custom index ( a to h ) to above data, this is called data labelling. Store it in series data variable : newseries
# se = pd.Series(newdata, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
#
# # 2) Print data by index 2
# print(se.iloc[2])
#
# # 3) Print data by label ‘b’
# print(se['b'])

dictdata = {"AHMEDABAD": [120, 15, 1], "SURAT": [150, 17, 2], "RAJKOT": [117, 25, 3]}

# Convert above data in pandas series data
# pdData = pd.Series(dictdata)
# print(pdData)

# Print by index ‘SURAT’
# print(pdData.loc['SURAT'])

# Print by index 1 ( observe the output to understand concept )
# print(pdData.iloc[1])

# Assign index 1,2,3 in above dictdata and print all data
# dcSR = pd.Series(dictdata)
# dcSR.index = ['1', '2', '3']
# print(dcSR)

# Assign index AHMEDABAD,SURAT,AHMEDABAD to dictdata  and print all data
# dcSR.index = ['AHMEDABAD', 'SURAT', 'AHMEDABAD']
# print(dcSR)

# Assign same index AHMEDABAD, AHMEDABAD to dictdata  and AHMEDABAD in
# !!

newdictionary = {"AHMEDABAD": 150, "AHMEDABAD": 200, "AHMEDABAD": 600, "AHMEDABAD": 500, "SURAT": 400}
# print(newdictionary["AHMEDABAD"])  # 150
# print('..................')

seriesdict = pd.Series(newdictionary)
# print(seriesdict)

# Create a list of 1 to 1000 data using numpy / any other
new_list = pd.Series(range(1, 1001))
# print(new_list)
# print(type(new_list))

# Create a list of Label even, odd and five
storeData = []
for i in new_list:
    if i % 5 == 0:
        storeData.append('divfive')
    elif i % 2 == 0:
        storeData.append('even')
    else:
        storeData.append('odd')

# print(storeData)

# Convert it to series data assign label to all data like ['odd','even','odd','even','divfive','even','odd','even','odd','divfive']
new_list.index = storeData
# print(new_list)

# Print even numbers by accessing label, print odd number by accessing label and print divisible by 5 via accessing label
# print(new_list.loc['even'])
# print(new_list.loc['odd'])
# print(new_list.loc['divfive'])

# XLRD TO LIST TO SERIES DATA :
loc = ('mydata.xlsx')
work_book = xlrd.open_workbook(loc)
sheet = work_book.sheet_by_index(0)

# FETCH DATA OF ALL RUNS OF VIRAT TO A LIST
# print(":::VIRAT's DATA:::")
VIRAT_LIST = []
for i in range(1, sheet.nrows):
    VIRAT_LIST.append(int(sheet.cell_value(i, 2)))
# print(VIRAT_LIST)

# CONVERT THAT LIST TO SERIES DATA
virat_pandas_data = pd.Series(VIRAT_LIST)
# print(virat_pandas_data)

# ASSIGN LABELS AS BELOW
# 0-15 RUNS : POOR
# 16-35 RUNS : AVERAGE
# 36 OR ABOVE : GOOD

runs_label = []
for i in virat_pandas_data:
    if 15 >= i >= 0:
        runs_label.append('POOR')
    elif 35 >= i >= 16:
        runs_label.append('AVERAGE')
    else:
        runs_label.append('GOOD')

# print(runs_label)

# PRINT DATA BASED ON LABEL.
# virat_pandas_data.index = runs_label
# print(virat_pandas_data)
