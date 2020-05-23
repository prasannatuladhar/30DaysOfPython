#  Numpy ---  general-purpose array-processing package of Python
# -Come with two Choices:Vecor(1D) and matrices(2D)

import numpy as np
list_number = [1,2,3]


# creating array
a = np.array(list_number)
print(a)
print(type(a))

b=np.array([(1,2,3),(4,5,6)],dtype=float)
print(b)


# initial placeholder
za=np.zeros(3)
print(za)

zb=np.zeros((3,2),dtype=int)
print(zb)

zc = np.zeros((3,2,2))
print(zc)

zf = np.full((3,4),3)
print(zf)

zr = np.random.rand(2,3)
print(zr)

zo = np.ones((3,3))
print(zo)

ze = np.eye(5)
print(ze)

#get array from 1 to 10 where (starting,End-1,step)
ga= np.arange(1,11)
print(ga)

#get array of number where (starting,Ending,number of items)
gl = np.linspace(1,11,10)
print(gl)


#get array reshape with whatever you want dimension
aga = ga.reshape(5,2)
print(aga)

# find the maximum value of number
res = aga.max()
print(res)

# find the minimum value of number
res_min = aga.min()
print(res_min)

# find the location of  minimum value of number
res_min_loc = aga.argmin()
print(res_min_loc)

#find the shape of array
nine_nine = np.arange(1,10)
new = nine_nine.reshape(3,3)
print(new)
print(new.shape) #checks the shape

#find data type
print(res.dtype)


# Numpy Indexing and Selection 1D array
array_list = np.arange(0,11)
copy_array_list = array_list.copy()
copy_array_list[5:11]=5
print(array_list)
print(copy_array_list)

# Numpy Indexing and Selection 2D array(Matrixes)
array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2d)
print(array_2d[1,1])
print(array_2d[1:,1:])


num_list = np.arange(1,11)
grt_5 = num_list>5
print(grt_5)
print(num_list)
print(num_list[grt_5])
print(num_list<5)

#mini exercise 
num_50 = np.arange(50).reshape(5,10)
print(num_50)
print(num_50[1:3,4:6])

#Numpy Operations

# Array with array
num_5 = np.arange(1,6)
num_5_copy = num_5.copy()
print(num_5+num_5_copy)
print(num_5*num_5_copy)

# Array with Scalar
print(num_5+10)
# print(num_5/0) gives warning and print infinite
print(num_5**2)

#Universal Array function
print(np.sqrt(num_5))
print(np.exp(num_5))
print(np.min(num_5))
print(np.max(num_5))
print(np.sin(num_5))
print(np.log(num_5))





