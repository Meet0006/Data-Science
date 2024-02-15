import numpy as np

mydata = [10, 20, 30, 40, 50]

# 1) print above python list
# print(mydata)

# 2) print type of above list
# print(type(mydata))

# 3) convert above list to numpy array store in variable a
a = np.array(mydata)

# 4) print converted numpy array a
print(a)

# 5) print data type of above converted numpy array a
print(type(a))

# 6) print shape of above numpy array [it will be (5,) means 5 rows cols undefined ]
np_shape = a.shape
print(np_shape)

# 7) create numpy array with 5 rows and 3 cols ( 5, 3 ) store in variable b. values 1,2,3....15
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
e = b.shape
c = b.reshape(5, 3)
print('---------------------------------', c)
d = c.shape

# 8) print that numpy array b
print(b)

# 9) print type of numpy array b
print(type(b))

# 10) print shape of numpy array b
print(e)

# 11) create numpy array  ( name : newarray ) with 3 rows and 5 cols, elements are 10,20,30,40....150
newarray = np.arange(10, 155, 10)
newarray_rc = newarray.reshape(3, 5)

# 12) print newarray ( output will be as below )
print(newarray_rc)

# 13) print data type of newarray
print(type(newarray_rc))

# 14) print shape of newarray
print(newarray_rc.shape)

# 15) find maximum number from newarray
print(newarray.max())

# 16) find minimum number from newarray
print(newarray.min())

# 17) print sum of all numbers of newarray
print(newarray.sum())

# 18) print 80
print(np.where(newarray == 80))
print(newarray[7])

# 19) print 140
print(np.where(newarray == 140))
print(newarray[13])

# 20) printing first row
print(newarray_rc[0])

# 21) printing max in third row
print(newarray_rc[2].max())

# 22) print sum of first row
print(np.sum(newarray_rc[0]))

# 23) addition of each  rows  answer should be [150 400 650]
new_b = np.array([[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]])
print(np.sum(new_b, axis=1))

# 24) addition of second row [answer should be 400 ]
print([np.sum(new_b[1])])

# 25) addition of all cols answer should be [180 210 240 270 300]
print(np.sum(new_b, axis=0))

# 26) addition of third col answer should be 240
print(np.sum(new_b[:, 2], axis=0))

# 27) arrange np array ( i ) with 9 elements answer should be [0 1 2 3 4 5 6 7 8]
i = np.arange(9)

# 28) print i
print(i)

# 29) print type of i
print(type(i))

# 30) convert above array in 3 by 3 matrix name it b
b = i.reshape(3, 3)

# 31) print b
print(b)

# 32) Develop 3 by 3 matrix filled with all zeroes
print(np.zeros((3, 3)))

# 33) Develop 3 by 3 matrix filled with all ones
print(np.ones((3, 3)))

# 34) Develop 3 by 3 identity matrix
print(np.identity(3))

# 35) generate random number from 0 to 10 (10 not included ) using numpy store it in variable e
e = np.random.uniform(0, 10, )

# 36) print e
print(e)

# 37) generate 5*5 matrix filled with all random numbers from 0 to 10 ( 10 not included ) store it in var f
f = np.random.randint(0, 10, size=(5, 5))

# 38) print f
print(f)

# 39) matrix multiplication ( first solve using mathematics pen and paper and than numpy )
# # random matrix 1 ( 2 * 3 ) dot random matrix 2 ( 3 * 2 ) => output matrix 3 shape ?
# # step 1) create random matrix 2 * 3 store in var x
# # step 2) create random matrix 3 * 2 store in vay y
# # step 3) multiplication z -> shape

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8], [9, 10], [11, 12]])
z = np.dot(x, y)
print(z)
print(np.shape(z))
