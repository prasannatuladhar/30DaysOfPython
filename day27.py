#  Numpy --- Data Analysis
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
arr.shape

#find data type
arr.dtype