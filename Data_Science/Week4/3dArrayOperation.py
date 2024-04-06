import numpy as np

''' SLICING ( APPLY ALL METHODS ) '''

# Slicing in 1D array
mydata = np.array([1, 2, 3, 4, 'apple', 6, 7, 8, 9, 10])  # 2 5 8
# print(mydata[1:8:3])

# Slicing in 2D array
twoDArray = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])  # 3 4 6 7  # 2 7  # 3 10
# print(twoDArray)
# print(twoDArray[0:2, :3])
# print(twoDArray[0:2, 3:])

# Slicing in 3D array
arr = np.array([[[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]],

                [[10, 11, 12],
                 [13, 14, 15],
                 [16, 17, 18]],

                [[19, 20, 21],
                 [22, 23, 24],
                 [25, 26, 27]],
                ])
# print(arr[:2, :3, :2])

""" ITERATE ALL DATA ( FOR LOOP, NDITER BOTH ) """

# Printing all data of 1D array  ( element by element print(a) )
# for i in np.nditer:
#     print(i)

# Printing all data of 2D array ( row wise , column wise )
# row wise
# for i in np.nditer(twoDArray):
#     print(i)
# for i in twoDArray.T:
#     print(i)
#
# # column wise
# for i in np.nditer(twoDArray.T):
#     print(i)

# Printing all data of 3D array ( row wise , column wise )
# for i in arr:
#     print(i)
#
# for i in arr.T:
#     print(i)
#
# for i in np.nditer(arr.T):
#     print(i)

""" SPLITTING DATA ( APPLY ALL  METHODS ) """

# Splitting data of 1D array
# split_1 = np.split(mydata, 2)
# print(split_1)

# Splitting data of 2D array
# split_1 = np.split(twoDArray, 2)
# print(split_1)

# Splitting data of 3D array
# split_1 = np.split(arr, 3)
# print(split_1)

'''SEARCHING DATA  ( TAKE INPUT FROM USER AND SEARCH )'''

# Searching data of 1D array
# search_1 = np.where(mydata == 'apple')[0]
# print(search_1)

# Searching data of 2D array
search_1 = np.where(twoDArray == 'apple')[0]
print(search_1)

# searching data of 3D array
