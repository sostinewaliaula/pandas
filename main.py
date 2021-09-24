import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

labels = ['a', 'b', 'c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}
print(arr)

print(pd.Series(my_data, labels))
print(pd.Series(arr))
print(arr[0])
print(pd.Series(data = my_data, index = labels))
ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
print(ser1)
ser2 = pd.Series([1,2,5,4], ['USA', 'Germany', 'Italy', 'Japan'])
print(ser2)
print(ser1 + ser2)

#Data frame
df = pd.DataFrame(randn(5,4),['a','b','c','d','e'],['w','x','y','z'])
print(df)
print(df[['w','x']])
df['new'] = df['w'] + df['x']
print(df)
df.drop('new', axis=1, inplace = True)
print(df)
print(df.shape)
df.drop('e', axis = 0, inplace = True)
print(df)
print(df.loc['a'])
print(df.iloc[1])
print(df.loc['c','y'])
print(df.iloc[2,2])
print(df.iloc[[2,2],[2,3]])
print(df>0)
booldf = df>0
print(df[booldf])
print(df[['w']] > 0)

arr = np.array([1, 2, 3, 5])
