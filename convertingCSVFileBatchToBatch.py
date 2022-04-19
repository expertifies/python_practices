from wsgiref import headers
import pandas as pd
import numpy as nm
from datetime import timedelta, datetime
from dateutil.relativedelta import *

# df2 = pd.read_csv('C:/Users/m.usman/Desktop/python-practice/2 Year IBM Stock Data.csv', header=[1], nrows=20, parse_dates=['time'])
filePath = "C:/Users/m.usman/Desktop/python-practice/2 Year IBM Stock Data.csv"
filePath1 = "C:/Users/m.usman/Desktop/python-practice/2 Year IBM Stock Data Copy From Default.csv"
mainFileHeaders = pd.read_csv(filePath).columns.tolist()
mainFile = pd.read_csv(filePath, parse_dates=['time'])
csvfile_count = len(mainFile.index)
print(f"Total Rows in CSV File: {csvfile_count}")
mainFile["symbols"] = "my_symbols"

mainFile['date-first'] = pd.to_datetime(mainFile['time']) + pd.DateOffset(months=1)+ pd.DateOffset(days=1)
mainFile['date-first'] = mainFile['date-first'].dt.strftime('%d/%m/%Y')

mainFile['month-first'] = pd.to_datetime(mainFile['time']) + pd.DateOffset(months=2)+ pd.DateOffset(days=1)
mainFile['month-first'] = mainFile['month-first'].dt.strftime('%m/%d/%Y')

mainFile['minutes'] = mainFile['time'].dt.strftime('%I:%M:%S %p')
mainFile.to_csv(filePath1, index=False)

secondaryFile = pd.read_csv(filePath1)
secondaryFileColumns = secondaryFile.columns.tolist()

# print(secondaryFileColumns)

csvfile_count = len(secondaryFile.index)
getLimit = int(input("pleaes provide the number of rows in one batach: "))

getCounts = int((csvfile_count/getLimit)+1)
newLimit = 0
i = 1
for i in range(getCounts):
    df2 = pd.read_csv(filePath1, skiprows=newLimit, nrows=getLimit)
    df2.to_csv('C:/Users/m.usman/Desktop/python-practice/2 Year IBM Stock Data Batch-'+str(i+1)+'.csv', header=secondaryFileColumns, index=False)
    newLimit = newLimit+getLimit

newfile = pd.read_csv('C:/Users/m.usman/Desktop/python-practice/2 Year IBM Stock Data Batch-1.csv',header=[1], nrows=10)
print(newfile.to_string())

# print(df2.info())
