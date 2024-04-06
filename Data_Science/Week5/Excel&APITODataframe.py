from matplotlib import pyplot as plt
import pandas as pd

# Load first file Result1 store in variable file1data and print
file1data = pd.read_excel('RESULT1.xlsx')

# Load second file Result2 store in variable file2data and print
file2data = pd.read_excel('RESULT2.XLSX')

# Merge to file data , store in variable all data and print
all_data = pd.concat([file1data, file2data], ignore_index=True)

# Check type of all data ( it should be data frame, so we can perform all type of operations on this file )
# print(type(all_data))

# From all data print bar graph of name of students and total
# ( names on x axes and total on y axes )
# name_x = all_data['NAME']
# total_y = all_data['TOTAL']
# plt.bar(name_x, total_y)
# plt.xlabel('Name of students')
# plt.ylabel('Total of students')
# plt.title('Students data')
# plt.show()

# Print total of first student from merged data ( all data )
# print(all_data['TOTAL'][0])

# Print highest total and lowest total
# print(' highest total is: ', all_data['TOTAL'].max(), '\n', 'Lowest total is: ', all_data['TOTAL'].min())

# Print data of first three students from merged data
# print(all_data.iloc[0:3])

# Print data of last three students from merged data
# print(all_data[-3:])

#  Print all data in descending order ( generating merit list - topper first )
# print(all_data.sort_values(by='PERCENTAGE', ascending=False))

#  Print first 3 toppers
topper_3 = all_data.sort_values(['PERCENTAGE'], ascending=False)
# print(topper_3[0:3])

#  Print all student names in alphabetical order
# print(all_data.sort_values(['NAME']))

# Generate merit file ( total first ) and store it in merit.xlsx
merit = pd.DataFrame(all_data, columns=['SRNO', 'TOTAL', 'BRANCH', 'NAME', 'PERCENTAGE', 'PASSFAIL'])
# merit.to_excel('merit.xlsx')

# Print all data with total greater than 200
greater = merit['TOTAL'] > 200
# print(merit[greater])

# Print all data with total less than 100 and store in weakstudents.xlsx
# less = merit['TOTAL'] < 100
# less_merit = merit[less]
# less_merit.to_excel('weakstudents.xlsx')

# Create one column 'CATEGORY' based on following condition AND store in result.xlsx file
# percentage 80 - 100 : SCHOLER
# percentage 50 - 79 : AVERAGE
# percentage below 50 : WEAK

result = merit['PERCENTAGE'].apply(lambda x: 'WEAK' if x < 50 else ('AVERAGE' if 50 <= x <= 79 else 'SCHOLER'))
merit['CATEGORY'] = result
# merit.to_excel('result.xlsx')
