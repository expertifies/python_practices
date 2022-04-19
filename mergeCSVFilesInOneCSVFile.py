import pandas as pd
import glob
import os

# setting the path for joining multiple files
files = os.path.join("C:\\Users\\m.usman\\Desktop\\python-practice\\", "2 Year IBM Stock Data Batch-*.csv")

print(files)
# list of merged files returned
files = glob.glob(files)

print("Resultant CSV after joining all CSV files at a particular location...")

# joining files with concat and read_csv
df = pd.concat(map(pd.read_csv, files), ignore_index=True)

# creating new file after concatination
df.to_csv('C:/Users/m.usman/Desktop/python-practice/concatination.csv', index=False)
print(df)

