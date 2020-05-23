
# Numpy Excercise
#1.Import
import numpy as np
# 2.Create an array of 10 zeros
array_ten_zeros = np.zeros((10),dtype=int)
print(array_ten_zeros)

# Create an array of 10 ones
array_ten_ones = np.ones(10)
print(array_ten_ones)


# Create an array of 10 fives
array_ten_fives = np.full(10,5)
print(array_ten_fives)


# Create an array of the integers from 10 to 50
arr_10_50 = np.arange(10,51)
print(arr_10_50)



# Create an array of all the even integers from 10 to 50
arr_even_int = np.arange(10,51,2)
print(arr_even_int)

# Create a 3x3 matrix with values ranging from 0 to 8
arr_3_3 = np.arange(0,9).reshape(3,3)
print(arr_3_3)

# Create a 3x3 identity matrix
arr_idt = np.eye(3)
print(arr_idt)

# Use NumPy to generate a random number between 0 and 1
ran_num = np.random.rand(1)
print(ran_num)

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
ran_std = np.random.randn(25)
print(ran_std)

# Create the following matrix:
# array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
#        [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
#        [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
#        [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
#        [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
#        [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
#        [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
#        [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
#        [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
#        [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]])
import numpy as np
arr_res = np.arange(1,101).reshape(10,10)
print(arr_res/100)
      
# Create an array of 20 linearly spaced points between 0 and 1:

arr_lin = np.linspace(0,1,20)
print(arr_lin)

# Numpy Indexing and Selection
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:


mat = np.arange(1,26).reshape(5,5)
print(mat)
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
# array([[12, 13, 14, 15],
#        [17, 18, 19, 20],
#        [22, 23, 24, 25]])
print(mat[2:,1:])

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
print(mat[3:4,4:])

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
print(mat[0:3,1:2])
# array([[ 2],
#        [ 7],
#        [12]])

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE

print(mat[4])
# array([21, 22, 23, 24, 25])



# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
print(mat[3:])
var=mat[:]
print(np.sum(var))

# array([[16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])
# Now do the following
# Get the sum of all the values in mat
# Out[50]:
# 325


# Get the standard deviation of the values in mat
print(np.std(mat))

# Out[51]:
# 7.2111025509279782


# Get the sum of all the columns in mat
print(np.sum(mat,axis=0))
# Out[53]:
# array([55, 60, 65, 70, 75])
