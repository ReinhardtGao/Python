from pandas import DataFrame
from pandasql import sqldf

# Create table

score = {'Name':['Zhang Fei', 'Guan Yu', 'Zhao Yun', 'Huang Zhong', 'Dian Wei', 'Dian Wei'],'Chinese': [66, 95, 95, 90, 80, 80], 'English': [65, 85, 92, 88, 90, 90], 'Mathematics': [None, 98, 96, 77, 90, 90]}
spreadsheet = DataFrame(score)
print(spreadsheet)

# Data Preparation

spreadsheet.drop_duplicates()
print(spreadsheet.isnull())
spreadsheet.fillna(spreadsheet['Mathematics'].mean(),inplace=True)
print(spreadsheet.isnull())


'''
Has problem with this code. WHen executing this part, interpreter throws out exception 
as "sqlite3.OperationalError: no such table: spreadsheet". 
But if we run "Select * from spreadsheet" here, no exception throw out.
pysql = lambda sql: sqldf(sql, globals())
sql1 = "update spreadsheet " \            
       "set Mathematics = 0 " \
       "where Name = 'Zhang Fei'"
print(pysql(sql1))
'''
# Add new column

spreadsheet['Total'] = spreadsheet[u'Chinese'] + spreadsheet[u'English'] + spreadsheet[u'Mathematics']
print(spreadsheet)
