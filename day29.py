# Pandas-(build in top of Numpy) used for fast analysis and data cleaning and preparation
import numpy as np
import pandas as pd

person = ['ram','shyam','hari','rahul']
age = [20,32,43,53]
d={'sun':1,'mon':2,'tues':3,'wed':4}
arr = np.array(age)
#create a series with person as data and age as index
res = pd.Series(person,age)
res = pd.Series(data=person,index=age)
#create a series with dictionary
day = pd.Series(d)
data = pd.Series(arr,index=person)
print(day)
print(data)

#create a series with two list, first is considered as data and second as index
country=pd.Series(['kathmandu','Thimpy','dhaka'],['Nepal','Bhutan','Bangladesh'])
print(country)
#selecting a item from series(must be index)
print(country['Nepal'])


num1 =pd.Series([1.2,3,2],['tomato','potato','cabbage'])
num2 =pd.Series([2,3,5],['potato','chillis','cauliflower'])
#adding a common item in series(must be index)
print(num1+num2)

from numpy.random import randn
#for common random number seed is used
np.random.seed(101)
#creating a dataframe with 5 row and 4 column
data= pd.DataFrame(randn(5,4),['A','B','C','D','E'],['V','W','X','Y'])
print(data)
#selecting from single column
print(data['X'])
#selecting from multiple column
print(data[['V','Y']])
#create new column with new as name adding two other colums
data['new']=data['W']+data['X']
#drop a df according to column
data.drop('new',axis=1,inplace=True)
#drop a df according to row
data.drop('E',axis=0,inplace=True)

print(data)
#checking for shape
print(data.shape)
#selecting a value according to index (must be first index)
print(data.loc['C'])
#selecting a value according to index location (must be first index location)
print(data.iloc[2])
#selecting a multiple value according to index (must be first index)
print(data.loc['C','W'])


