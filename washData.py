import pandas as pd
import math
from pandasql import sqldf
from pandas import Series, DataFrame
Ogl = DataFrame(pd.read_excel('foodinformation.xlsx'))
Ogl.index
print(Ogl)

'''Lower alphabet in column food'''
#print(Ogl.isnull())
Ogl['food'] = Ogl['food'].apply(str.lower)
Ogl.index = range(len(Ogl))

'''Clean blank'''
Ogl.loc[2,'ounces'] = Ogl[Ogl['food'].isin(['bacon'])].mean()['ounces']
Ogl.index = range(len(Ogl))

'''Change the minus value to real'''
Ogl.loc[6,'ounces'] = abs(Ogl.loc[6,'ounces'])
Ogl.index = range(len(Ogl))

print(Ogl)
