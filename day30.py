import numpy as np 
import pandas as pd 

from numpy.random import randn
np.random.seed(101)

# creating a dataframe
data= pd.DataFrame(randn(4,5),['A','B','C','D'],['V','W','X','Y','Z'])
print(data)
# Using single condition in dataframe
print(data[data['V']>0][['X','Y']])
# Using multiple condition in dataframe
print(data[(data['V']>0)&(data['Y']<1)][['X','Y']])
# Reseting with new index start from 0,1,2,3....
new_data = data.reset_index()
print(new_data)

# Multilayer DataFrame
outside = ['G1','G2','G1','G2','G1','G2']
inside = [1,2,3,1,2,3]
newdf = list(zip(outside,inside))
newdf = pd.MultiIndex.from_tuples(newdf)
df = pd.DataFrame(randn(6,2),newdf,['A','B'])
print(df)
# Geting value of DataFrame- outside
print(df.loc['G1']['A'])
# Geting value of DataFrame- inside
print(df.loc['G1'].loc[1])
# Naming DataFrame indexces
df.index.names=['Group','Number']
print(df)
#get a value of b 0.3905278427
print(df.loc['G1'].loc[3]['B'])




