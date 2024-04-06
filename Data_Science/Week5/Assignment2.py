import pandas as pd
import numpy as np

# AMAZON PRODUCTS DATASET

# 1) Load amazon products data set.
amazon_product = pd.read_excel('amazon_products.xlsx')
# print(amazon_product)

# 2) Print total number of rows.
# 3) Print total number of columns.
# print(amazon_product.shape)

# 4) Print names of all colums.
# print(np.column_stack(amazon_product))

# 5) Apply Knowledge of Numpy Masks - Any other method not allowed as it is not covered yet !
#    Allow user to insert number of stars ( rating ) print total number of products with similar rating.
#    ( condition : user can insert stars >= 1 and <= 5 )
user_input = float(input("Enter number of star: "))
rating_star = list(map(lambda x: 1 <= amazon_product['stars'] <= 5, amazon_product['stars']))
print(rating_star)
# rating_star = 1 <= amazon_product['stars'] <= 5
# for i in rating_star:
#     if user_input == rating_star[i]:
#         print('is valid')
#     else:
#         print('nothing')

# 6) Print count of Maximum Reviews.
# max_review = amazon_product['reviews']

# 7) Print count of products which got reviews greater than 1000 products ( In future we will consider it as popular product. )


# 8) Allow user to insert product number. Save image of that product as myimage in same folder


# 9) Print rating wise bar graph.
#
# >= 1 to < 2 stars : count
# >= 2 to < 3 stars : count
# >= 3 to < 4 stars : count
# >= 4 to <= 5 stars : count
#


# 10) Print highest and lowest priced product price.


# 11) Print higest bought in last month.


# 12) Allow user to insert category number. Print count of total number of items in that category. ( for example No 81 is for computer, check from category dataset ).
