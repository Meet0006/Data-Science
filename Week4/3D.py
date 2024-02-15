import numpy as np

# Create your first 3D matrix, Create 4 planes each plane should have 5 rows and 5 columns.
threeDData = np.array([[[1, 2, 3, 4, 5], [5, 6, 7, 8, 5], [9, 10, 11, 12, 5], [1, 23, 3, 64, 5], [1, 2, 3, 84, 5]],
                       [[10, 20, 30, 40, 5], [50, 60, 70, 80, 5], [90, 100, 110, 120, 5], [1, 25, 3, 4, 5],
                        [1, 2, 93, 4, 5]],
                       [[21, 22, 237, 24, 5], [25, 226, 27, 28, 5], [295, 210, 211, 212, 5], [1, 22, 3, 40, 5],
                        [1, 26, 3, 4, 5]],
                       [[1, 2, 389, 4, 5], [5, 36, 7, 78, 5], [9, 10, 1501, 12, 58], [1, 42, 3, 46, 5],
                        [1, 82, 3, 24, 5]]])

# Print Entire 3D matrix
print(threeDData)

# Print First plane.
print(threeDData[0])

# Print Third plane.
print(threeDData[2])

# Print first data of first row of third plane.
print(threeDData[2][0][0])

# Print Third data of third row of fourth plane.
print(threeDData[3][2][2])

# Print all data of first row of second plane
print(threeDData[1][0])

# Print all data of fourth column of third plane.
print(threeDData[2, :, 3])

# Print Min, max and sum of all data
print(np.min(threeDData))
print(np.max(threeDData))
print(np.sum(threeDData))

# Print Min max and sum of third plane only.
print(np.min(threeDData[2]))
print(np.max(threeDData[2]))
print(np.sum(threeDData[2]))

# 3D array data Search
#
# 1) Allow user to insert a number. Print number is found in 3D array or not.
user_input = int(input("Enter a number: "))
final_result = np.any(threeDData == user_input)
if final_result:
    print('Number is found in 3D array')
else:
    print('Number is not found')

# 2) Allow user to insert a number. Print number is found in second plane or not.
user_input = int(input("Enter a number: "))
final_result = np.any(threeDData[1] == user_input)
if final_result:
    print('Number is found in 3D array')
else:
    print('Number is not found')

# 3D array data pre-processing
#
# 1) Print how many (count )even numbers are there in entire 3D array.
mask = threeDData % 2 == 0
print(len(threeDData[mask]))

# 2) Print how many ( count )  odd numbers are there in fourth plane.
fourth_plane = threeDData[3]
mask = fourth_plane % 2 != 0
print(len(fourth_plane[mask]))

# 3) Print all even numbers from first plane.
first_plane = threeDData[0]
mask = first_plane % 2 == 0
print(first_plane[mask])
