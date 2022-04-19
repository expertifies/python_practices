import pandas as pd
import numpy as nm
from datetime import datetime

# mydateparser = lambda x: pd.datetime.strptime(x, "%Y %m %d %H:%M:%S")
# df2 = pd.read_csv('C:/Users/m.usman/Desktop/python-practice/2 Year IBM Stock Data.csv', header=[1], nrows=20, parse_dates=['time'])
mainFile = pd.read_csv('C:/Users/m.usman/Desktop/python-practice/2 Year IBM Stock Data.csv')

csvfile_count = len(mainFile.index)
getLimit = int(input("pleaes provide the number of chunks: "))

getCounts = int((csvfile_count/getLimit)+1)
newLimit = 0
for i in range(getCounts):
    df2 = pd.read_csv('C:/Users/m.usman/Desktop/python-practice/2 Year IBM Stock Data.csv', skiprows=newLimit, nrows=getLimit)
    df2["symbols"] = "my_symbols"+str(i)
    # df2['date-first'] = df2['time'].dt.strftime('%d/%m/%Y')
    # df2['month-first'] = df2['time'].dt.strftime('%m/%d/%Y')
    # df2['minutes'] = df2['time'].dt.strftime('%I:%M:%S %p')
    df2.to_csv('C:/Users/m.usman/Desktop/python-practice/cities'+str(i)+'.csv', index=False)
    newLimit = newLimit+getLimit




# df2["year"] = df2['time'].dt.year
# df2["mohth"] = df2['time'].dt.month
# df2['date-first'] = df2['time'].dt.strftime('%d/%m/%Y')
# df2['month-first'] = df2['time'].dt.strftime('%m/%d/%Y')
# df2['minutes'] = df2['time'].dt.strftime('%I:%M:%S %p')

# csvfile_count = len(df2.index)
# print(csvfile_count)
print(df2.to_string())



# print(df2.info())
