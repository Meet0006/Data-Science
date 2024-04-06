import numpy
import pandas as pd
import numpy as np

# 1) Load amazon categories dataset.
amazon_data = pd.read_excel('amazon_categories.xlsx')
# print(amazon_data)

# 2) Print total number of rows.
# 3) Print total number of columns.
# print(amazon_data.shape)

# 4) Print names of all columns.
# print(np.column_stack(amazon_data))

# 5) Create a new column 'lattercount', count number of latters in that category.
# Solution 1
# Latter_Count = []
# for i in amazon_data['category_name']:
#     Latter_Count.append(len(i))
# amazon_data['lattercount'] = Latter_Count
# print(amazon_data)

# Solution 2
amazon_data['lattercount'] = list(map(lambda x: len(x), amazon_data['category_name']))
# print(amazon_data)

# Extra:
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)

# 6) Create a new column 'newid', prepare random 10 digit ID and assign it to each category.
ran_int = []
con_int = []
for i in amazon_data['category_name']:
    ran_int.append(np.random.randint(0, 9, size=10, dtype=int))

for i in ran_int:
    con_int.append(' '.join(ran_int[0][i].astype(str)))
#
amazon_data['newid'] = con_int
# print(amazon_data)

# 7) Arrange category Alphabatically ( A to Z format )
amazon_data.sort_values('category_name')

# 8) Store final output in below format and save it to categories.xlsx / csv any.
# 	a) All categories alphabetically
# 	b) id | newid | category_name | lattercount

amazon_data.to_excel('categories.xlsx')