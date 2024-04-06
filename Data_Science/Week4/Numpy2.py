import numpy as np

# Create python list
data = [1, 2, 3, 9, 0]

# Convert list to numpy array and store it in variable mydata
mydata = np.array(data)
print(mydata)

# Shuffle above variable mydata ( use random.shuffle )
np.random.shuffle(mydata)
print(mydata)

# Perform permutation of variable data and store it in newdata
# Use random.permutation
# ( learn what is permutation and understand the concept )
# Usecase of permutation is create new array with shuffle and keep old array as it is
newdata = np.random.permutation(mydata)
print(newdata)

# Create 2 One Dimensional Arrays. data1 and data2
# Merge two 1D array ( data3 = data1 + 2*data2 )
data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([6, 7, 8, 9, 10])
data3 = data1 + 2 * data2
print(data3)

# Create 2 Two Dimensional Arrays data4 and data5
# Merge two 2D array horizontally store in data6
# Merge two 2D array horizontally store in data7
data4 = np.random.randint(0, 10, size=(3, 3))
data5 = np.random.randint(0, 10, size=(3, 3))
data6 = np.hstack((data4, data5))
data6 = np.vstack((data4, data5))
print(data6)
print(type(data6))

# Create one 2D array data8 copy data and save it to data9
data8 = np.random.randint(0, 10, size=(3, 3))
data9 = np.copy(data8)
print(data9)

# Create a view from one (2X2) 2D array to other 2D array
data10 = data9.view()
print(data10)

# Create 10x10 numpy array from random numbers between 0 to 9 and soter in variable e
e = np.random.randint(0, 9, size=(10, 10))

# Print e
print(e)

#  Process each and every element and place true for even number and false for odd number
# topic name numpy mask , print mask
print('------------------')
range_of_number = np.random.randint(0, 100, size=(10, 10))
print(range_of_number)
mask = range_of_number % 2 == 0
print(mask)
print('------------------')

# Print only even numbers from above array
print(range_of_number[mask])

# Print total count of generated even numbers from above array
print(len(range_of_number[mask]))

# Create a new variable furnituredata to generate 100rows X 100cols of bill data ( total 10000 data ) matrix between 15000 to 250000
# And print furniture data
furnituredata = np.random.randint(15000, 250000, size=(100, 100))
print(furnituredata)

# Create masks of more than 125000 ( place true or false ) and apply mask on furniture data.
print('---------------**---')
new_mask = furnituredata % 2 == 0
print(125000 < new_mask)
