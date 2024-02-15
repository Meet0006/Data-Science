import numpy as np
import requests
from matplotlib import pyplot as plt

# 1) Create a 3D matrix with random numbers between 1 to 100 ( 100 not included ). It should have 4 planes with 5 rows and 5 columns.
d3Matrix = np.random.randint(1, 100, size=(4, 5, 5))

# 2) Print all Data.
print(d3Matrix)

# 3) Print last plane.
print(d3Matrix[-1])

# 4) Print all data of last plane using for loop.
for i in d3Matrix[-1]:
    print(i)

# 5) Print Maximum number from last column of third row in second plane.
print(np.max(d3Matrix[1, 0:3, 4:]))

# 6) Print addition of all numbers from second row of last plane.
print(np.sum(d3Matrix[-1, 1]))

# 7) Print Lowest number from first and second plane only.
print(np.min(d3Matrix[:1]))

# 8) Print highest number from second and last plane.
print(np.max(d3Matrix[1:-1]))

# 9) Print sum of third column of first plane.
print(np.sum(d3Matrix[0, 0:5, 2]))

# 10) Print sum of third columns of all planes. ( accessing multiple plane, multiple var or loop allowed ).
print(np.sum(d3Matrix[:4, :, 2]))

# 11) Print highest number from third row of all planes. ( accessing multiple plane, multiple var or loop allowed ).
print(d3Matrix[:4, 2])

# 12) Apply mask on 3D data : Mask of even number
mask = d3Matrix % 2 == 0

# 13) Print total number of even numbers from entire 3D data.
print(np.sum(d3Matrix[mask]))

# 14) Print mask ( true false ).
print(mask)

# 15) Print all even numbers from entire 3D data.
print(d3Matrix[mask])

# 16) Print total number of odd numbers in third plane only.
new_mask = d3Matrix[2] % 2 != 0
print(len(d3Matrix[2][new_mask]))

# 17) CONCEPT : Conditional mask / Multiple mask can be applied
# Mask of numbers between 25 to 60 ( 60 included ).
mask_25To60 = (25 <= d3Matrix) & (60 >= d3Matrix)

# 18) Print count of all numbers between 25 to 60 ( apply above mask in 3D data ) from data.
print(len(d3Matrix[mask_25To60]))

# 19) Print all data between 25 to 60.
print(d3Matrix[mask_25To60])

# API + NUMPY
api = requests.get('https://dummy.restapiexample.com/api/v1/employees')

employeedata = {
    "status": "success",
    "data": [
        {
            "id": 1,
            "employee_name": "Tiger Nixon",
            "employee_salary": 320800,
            "employee_age": 61,
            "profile_image": ""
        },
        {
            "id": 2,
            "employee_name": "Garrett Winters",
            "employee_salary": 170750,
            "employee_age": 63,
            "profile_image": ""
        },
        {
            "id": 3,
            "employee_name": "Ashton Cox",
            "employee_salary": 86000,
            "employee_age": 66,
            "profile_image": ""
        },
        {
            "id": 4,
            "employee_name": "Cedric Kelly",
            "employee_salary": 433060,
            "employee_age": 22,
            "profile_image": ""
        },
        {
            "id": 5,
            "employee_name": "Airi Satou",
            "employee_salary": 162700,
            "employee_age": 33,
            "profile_image": ""
        },
        {
            "id": 6,
            "employee_name": "Brielle Williamson",
            "employee_salary": 372000,
            "employee_age": 61,
            "profile_image": ""
        },
        {
            "id": 7,
            "employee_name": "Herrod Chandler",
            "employee_salary": 137500,
            "employee_age": 59,
            "profile_image": ""
        },
        {
            "id": 8,
            "employee_name": "Rhona Davidson",
            "employee_salary": 327900,
            "employee_age": 55,
            "profile_image": ""
        },
        {
            "id": 9,
            "employee_name": "Colleen Hurst",
            "employee_salary": 205500,
            "employee_age": 39,
            "profile_image": ""
        },
        {
            "id": 10,
            "employee_name": "Sonya Frost",
            "employee_salary": 103600,
            "employee_age": 23,
            "profile_image": ""
        },
        {
            "id": 11,
            "employee_name": "Jena Gaines",
            "employee_salary": 90560,
            "employee_age": 30,
            "profile_image": ""
        },
        {
            "id": 12,
            "employee_name": "Quinn Flynn",
            "employee_salary": 342000,
            "employee_age": 22,
            "profile_image": ""
        },
        {
            "id": 13,
            "employee_name": "Charde Marshall",
            "employee_salary": 470600,
            "employee_age": 36,
            "profile_image": ""
        },
        {
            "id": 14,
            "employee_name": "Haley Kennedy",
            "employee_salary": 313500,
            "employee_age": 43,
            "profile_image": ""
        },
        {
            "id": 15,
            "employee_name": "Tatyana Fitzpatrick",
            "employee_salary": 385750,
            "employee_age": 19,
            "profile_image": ""
        },
        {
            "id": 16,
            "employee_name": "Michael Silva",
            "employee_salary": 198500,
            "employee_age": 66,
            "profile_image": ""
        },
        {
            "id": 17,
            "employee_name": "Paul Byrd",
            "employee_salary": 725000,
            "employee_age": 64,
            "profile_image": ""
        },
        {
            "id": 18,
            "employee_name": "Gloria Little",
            "employee_salary": 237500,
            "employee_age": 59,
            "profile_image": ""
        },
        {
            "id": 19,
            "employee_name": "Bradley Greer",
            "employee_salary": 132000,
            "employee_age": 41,
            "profile_image": ""
        },
        {
            "id": 20,
            "employee_name": "Dai Rios",
            "employee_salary": 217500,
            "employee_age": 35,
            "profile_image": ""
        },
        {
            "id": 21,
            "employee_name": "Jenette Caldwell",
            "employee_salary": 345000,
            "employee_age": 30,
            "profile_image": ""
        },
        {
            "id": 22,
            "employee_name": "Yuri Berry",
            "employee_salary": 675000,
            "employee_age": 40,
            "profile_image": ""
        },
        {
            "id": 23,
            "employee_name": "Caesar Vance",
            "employee_salary": 106450,
            "employee_age": 21,
            "profile_image": ""
        },
        {
            "id": 24,
            "employee_name": "Doris Wilder",
            "employee_salary": 85600,
            "employee_age": 23,
            "profile_image": ""
        }
    ],
    "message": "Successfully! All records has been fetched."
}

# 1) Fetch salary of all employees and store it in numpy array.
employeer_salary = []
for i in range(0, len(employeedata['data'])):
    employeer_salary.append(employeedata['data'][i]['employee_salary'])

numpy_array = np.array(employeer_salary)

# 2) Print Highest, Lowest and Average salary from above array.
print(np.max(numpy_array))
print(np.min(numpy_array))
print(np.average(numpy_array))

# 3) Convert above numpy to 6 X 4 numpy 2D matrix.
reshape_matrix = numpy_array.reshape(6, 4)
print(reshape_matrix)

# 4) Convert above numpy to 2 rows X 4 Cols X 3 Planes , 3D matrix.
matrix_3d = numpy_array.reshape(3, 2, 4)
print(matrix_3d)

# 5) Apply mask on above 3D matrix to find count of salary between 3 lacs to 6 lacs.
salary_mask = (300000 < matrix_3d) & (600000 > matrix_3d)
print(matrix_3d[salary_mask])

# API + NUMPY + PLOTTING

# 1) Create masks in such a way it should generate the count of salary in group wise
# GROUP1 : Count of people Salary below 2 lacs
# GROUP2 : Count of people Salary between 2 to 3.5 lacs
# GROUP3 : Count of people Salary between 3.5 to 4 lcas
# GROUP4 : Count of people Salary between 4 to 5.5 lacs
# GROUP5 : Count of people Salary between 5.5 to 7 lacs

GROUP1 = []
GROUP2 = []
GROUP3 = []
GROUP4 = []
GROUP5 = []

group_one = numpy_array <= 200000
group_two = (numpy_array >= 200000) & (350000 > numpy_array)
group_three = (numpy_array >= 350000) & (400000 > numpy_array)
group_four = (numpy_array >= 400000) & (550000 > numpy_array)
group_five = (numpy_array >= 550000) & (700000 > numpy_array)

for i in range(0, len(numpy_array)):
    GROUP1.append(len(numpy_array[group_one]))
    GROUP2.append(len(numpy_array[group_two]))
    GROUP3.append(len(numpy_array[group_three]))
    GROUP4.append(len(numpy_array[group_four]))
    GROUP5.append(len(numpy_array[group_five]))
    break

# 2) Print all above data in bar graph. ( x axes GROUP1,GROUP2... and y axes salary )

Salary_lenght = [GROUP1[0], GROUP2[0], GROUP3[0], GROUP4[0], GROUP5[0]]
print(Salary_lenght)
Labels = ['GROUP1', 'GROUP2', 'GROUP3', 'GROUP4', 'GROUP5']

plt.bar(Labels, Salary_lenght)
plt.xlabel('Groups')
plt.ylabel("Employee Salary's")
plt.title('Employee Salary barchart')
plt.show()

# 3) Find age wise mass count from above data using appropriate mask and generate a Pie chart.
# MASS1 : Age below 25 years
# MASS2 : Age between 25 to 40 years
# MASS3 : Age between 40 to 55 years
# MASS4 : Age between 55 to 70 years

employeer_age = []
for i in range(0, len(employeedata['data'])):
    employeer_age.append(employeedata['data'][i]['employee_age'])
age_array = np.array(employeer_age)

MASS1 = []
MASS2 = []
MASS3 = []
MASS4 = []

MASS_1 = age_array < 25
MASS_2 = (age_array >= 25) & (40 > age_array)
MASS_3 = (age_array >= 40) & (55 > age_array)
MASS_4 = (age_array >= 55) & (70 > age_array)

for i in range(0, len(age_array)):
    MASS1.append(len(age_array[MASS_1]))
    MASS2.append(len(age_array[MASS_2]))
    MASS3.append(len(age_array[MASS_3]))
    MASS4.append(len(age_array[MASS_4]))
    break

chart_value = [MASS1[0], MASS2[0], MASS3[0], MASS3[0]]
Labels = ['Below 25', '25 to 40', '40 to 55', '55 to 70']
plt.pie(chart_value, autopct='%.2f%%', labels=Labels)
plt.legend(title='Age')
plt.title('Age wise pie chart')
plt.show()
