from pandas import Series, DataFrame

x1 = Series([1,2,3,4])

data = {'A': [23, 235, 65, 72, 4], 'B': [33, 432, 21, 163, 76], 'C': [153, 322, 62, 5, 65]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['1', '2', '3', '4', '5'], columns=['A', 'B', "C"])
print(df1)
print(df2)

