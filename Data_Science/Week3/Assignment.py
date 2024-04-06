import xlrd
from matplotlib import pyplot as plt
import numpy as np

loc = ('mydata.xlsx')
work_book = xlrd.open_workbook(loc)
sheet2 = work_book.sheet_by_index(1)

# 1) PRINT TOTAL NUMBER OF ROWS
print(sheet2.nrows)

# 2) PRINT TOTAL NUMBER OF COLUMNS
print(sheet2.ncols)

# 3) PRINT 61
for i in range(1, sheet2.nrows):
    for j in range(1, sheet2.ncols):
        if 61 == sheet2.cell_value(i, j):
            print(61)
            break

# 4) PRINT NAMES OF ALL MONTHS
for i in range(1, sheet2.ncols):
    print(sheet2.cell_value(0, i))

# 5) PRINT NAMES OF ALL PRODUCTS
for i in range(1, sheet2.nrows):
    print(sheet2.cell_value(i, 0))

# 6) PRINT TOTAL NUMBER OF PRODUCTS SOLD IN MARCH MONTH
product = []
for i in range(1, sheet2.nrows):
    product.append(sheet2.cell_value(i, 3))
print(len(product))

# 7) WHICH PRODUCT SOLD HIGHEST IN MARCH MONTH. ( ANS MOBILES )
high_price = 0
price_array = []
for i in range(1, sheet2.nrows):
    if high_price < int(sheet2.cell_value(i, 3)):
        high_price = int(sheet2.cell_value(i, 3))
        price_array.append(int(sheet2.cell_value(i, 3)))

final_high_price = price_array[-1]

for i in range(1, sheet2.nrows):
    if final_high_price == sheet2.cell_value(i, 3):
        print(sheet2.cell_value(i, 0))

# 8) ALLOW USER TO INSERT NAME OF THE MONTH PRINT NAME OF HIGHEST AND LOWEST NUMBER OF PRODUCTS SOLD IN THAT MONTH
user_input = input('Enter month name: ')
user_input_month = ''
store_first_value = []
high_price_array = []
low_price_array = []

# find user input month
for i in range(1, sheet2.ncols):
    if user_input == sheet2.cell_value(0, i):
        user_input_month = sheet2.cell_value(0, i)

# find first user input month
for i in range(1, sheet2.ncols):
    if user_input_month == sheet2.cell_value(0, i):
        for j in range(1, sheet2.nrows):
            store_first_value.append(int(sheet2.cell_value(j, i)))
            break

high_price = store_first_value[0]
low_price = store_first_value[0]

# find the highest user input month
for i in range(1, sheet2.ncols):
    if user_input_month == sheet2.cell_value(0, i):
        for j in range(1, sheet2.nrows):
            if high_price < sheet2.cell_value(j, i):
                high_price = sheet2.cell_value(j, i)
                high_price_array.append(int(high_price))

# find the lowest user input month
for i in range(1, sheet2.ncols):
    if user_input_month == sheet2.cell_value(0, i):
        for j in range(1, sheet2.nrows):
            if low_price > sheet2.cell_value(j, i):
                low_price = sheet2.cell_value(j, i)
                low_price_array.append(int(low_price))

final_high_price = high_price_array[-1]
final_low_price = low_price_array[-1]

for i in range(1, sheet2.nrows):
    for j in range(0, sheet2.ncols):
        if user_input_month == sheet2.cell_value(0, j):
            if final_high_price == sheet2.cell_value(i, j):
                print('HIGHEST NUMBER OF PRODUCTS SOLD IN:', user_input, ' :is:-> ', sheet2.cell_value(i, 0))
                break

for i in range(1, sheet2.nrows):
    for j in range(1, sheet2.ncols):
        if user_input_month == sheet2.cell_value(0, j):
            if final_low_price == sheet2.cell_value(i, j):
                print('LOWEST NUMBER OF PRODUCTS SOLD IN:', user_input, ' :is:-> ', sheet2.cell_value(i, 0))
                break

# 9) IN WHICH MONTH REFRIGERATOR SOLD HIGHEST.
high_price = 0
price_array = []
for i in range(1, sheet2.ncols):
    if high_price < int(sheet2.cell_value(5, i)):
        high_price = int(sheet2.cell_value(5, i))
        price_array.append(int(sheet2.cell_value(5, i)))

final_high_price = price_array[-1]

for i in range(1, sheet2.ncols):
    if final_high_price == sheet2.cell_value(5, i):
        print(sheet2.cell_value(0, i))

# 10) ALLOW USER TO INSERT NAME OF ELECTRONIC DEVICE. PRINT IN WHICH MONTH IT SOLD HIGHEST.
user_input = input("ENTER NAME OF ELECTRONIC DEVICE: ")

high_price = 0
price_array = []

for i in range(1, sheet2.ncols):
    for j in range(1, sheet2.nrows):
        if user_input == sheet2.cell_value(j, 0):
            if high_price < int(sheet2.cell_value(j, i)):
                high_price = int(sheet2.cell_value(5, i))
                price_array.append(int(sheet2.cell_value(5, i)))

final_high_price = price_array[-1]

for i in range(1, sheet2.ncols):
    if final_high_price == sheet2.cell_value(5, i):
        print(sheet2.cell_value(0, i))

# 11) PRINT PIE CHART OF JULY MONTHS SALES.
price_array = []
product_name = []
for i in range(1, sheet2.nrows):
    price_array.append(int(sheet2.cell_value(i, 7)))
    product_name.append(sheet2.cell_value(i, 0))

plt.pie(price_array, autopct='%.2f%%', labels=product_name)
plt.title('JULY MONTHS SALES')
plt.show()

# 12) PRINT BAR GRAPH OF SEPTEMBER MONTH’S SALES. ( X AXES NAME OF PRODUCT Y AXES UNIT SOLD )
price_array = []
product_name = []
for i in range(1, sheet2.nrows):
    price_array.append(int(sheet2.cell_value(i, 9)))
    product_name.append(sheet2.cell_value(i, 0))

plt.bar(product_name, price_array)
plt.title('SEPTEMBER MONTHS SALES')
plt.show()

# 13) ALLOW USER TO INSERT NAME OF THE MONTH, PRINT SUB PLOT OF PIE CHART AND BAR GRAPH OF THAT MONTH.
user_input = input("ENTER NAME OF THE MONTH: ")
price_array = []
product_array = []
for i in range(1, sheet2.ncols):
    if user_input == sheet2.cell_value(0, i):
        for j in range(1, sheet2.nrows):
            product_array.append(sheet2.cell_value(j, 0))
            price_array.append(sheet2.cell_value(j, i))

# Create subplots
fig, Axes = plt.subplots(1, 2, figsize=(21, 7))

# Bar chart
Axes[0].bar(product_array, price_array)
Axes[0].set_xlabel('Product Name')
Axes[0].set_ylabel('Sold Product Number')
Axes[0].set_title('Bar Graph')
Axes[1].pie(price_array, labels=product_array, autopct='%.2f%%')
Axes[1].set_title('Pie Chart')
plt.tight_layout()
plt.show()

# 14) PRINT PIE CHART OF MONTH WISE SALES OF AC
month_name = []
sold_product = []
for i in range(1, sheet2.ncols):
    sold_product.append(sheet2.cell_value(4, i))
    month_name.append(sheet2.cell_value(0, i))

plt.pie(sold_product, labels=month_name, autopct='%.1f%%')
plt.title('SALES OF AC')
plt.show()

