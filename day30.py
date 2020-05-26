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
#get a value via cross section level
print(df.xs(1,level='Number'))

# Create a DataFrame with simple dictionary
d = {'A':[1,2,np.nan],'B':[3,3,4],'C':[np.nan,1,np.nan]}
df = pd.DataFrame(d)
# Drop the item with atleast 1 whole number
print(df.dropna(thresh=1))
# Fill the NaN with mean of available column value
print(df.fillna(value=df['A'].mean()))
# Groupby
data = {
    'Company':['Google','Google','Amazon','Amazon','Tesla','Tesla'],
    'Person':['Tanny','Ram','Gopal','John','Bob','Robert'],
    'Sales':[200,200,450,251,584,785]
}

df=pd.DataFrame(data)
print(df)
# Return object only. Shows address untill method is called upon
print(df.groupby('Company'))
#return result of aggregate function like mean,sum,count,min,max of all data
print(df.groupby('Company').mean())
#return result of aggregate function like mean,sum of specific to amazon
print(df.groupby('Company').mean().loc['Amazon'])
# return Sales count   mean         std    min     25%    50%     75%    max
print(df.groupby('Company').describe())

# print(df.groupby('Company').describe().transpose()) --->transpose is used to view horizontally

# Concating a DataFrame

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

print(pd.concat([df1,df2,df3],axis=1))                        

# Merging a DataFrame on single key
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left,right,how='inner',on='key'))        

# Merging a DataFrame on multiple key
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
print(pd.merge(left,right,on=['key1','key2']))                       

# Joing a DataFrame
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])


left.join(right)                      