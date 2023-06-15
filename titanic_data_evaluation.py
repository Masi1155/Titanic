import pandas as pd
import spicy
import numpy as np
import matplotlib.pyplot as plt

csv = pd.read_csv("TitanicData.csv")
# print(csv)
csv["Survived"].replace(to_replace=0, value=False, inplace=True)
csv["Survived"].replace(to_replace=1, value=True, inplace=True)
survivors = csv.groupby("Survived").agg({"PassengerId": "count"})

csv[['Title','Name']] = csv['Name'].str.split('.',1, expand = True)
csv[['Surname', 'Title']] = csv['Title'].str.split(',',1,expand = True)

title = csv.groupby('Title').describe()
print(csv[['Title','Name']])
print(title)