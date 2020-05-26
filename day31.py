# Operation in Pandas
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df)
# print the unique item in column 'col2'
print(df['col2'].unique())
# print the length of unique item in column 'col2'
print(df['col2'].nunique())
# print how many times the unique item in column 'col2' occured
print(df['col2'].value_counts())
# using operator for data selection
print(df[(df['col1']>1) & (df['col2']==444)])
# using operator for data selection using apply for finding length of string
print(df['col3'].apply(len))
# using operator for data selection using apply with lambda function
print(df['col1'].apply(lambda x:x+10))
# sorting the data frame
print(df.sort_values('col2'))
# check if there is value of null in Data Frame
print(df.isnull())
# Permanently Removing a Column
del df['col1']
print(df)
