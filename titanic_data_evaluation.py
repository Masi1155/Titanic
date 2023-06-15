import pandas as pd
import spicy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

csv = pd.read_csv("TitanicData.csv")
# print(csv)
csv["Survived"].replace(to_replace=0, value=False, inplace=True)
csv["Survived"].replace(to_replace=1, value=True, inplace=True)
survivors = csv.groupby("Survived").agg({"PassengerId": "count"})

# csv[['Title', 'Name']] = csv['Name'].str.split('.', 1, expand=True)
# csv[['Surname', 'Title']] = csv['Title'].str.split(',', 1, expand=True)
#
# title = csv.groupby('Title').describe()
# print(csv[['Title', 'Name']])
# print(title)

survive_fare_survived = csv.groupby('Fare').apply(lambda x: pd.Series((x['Survived']).sum(), index=['Überlebt']))
survive_fare_died = csv.groupby('Fare').apply(lambda x: pd.Series((x['Survived'] == False).sum(), index=['Gestorben']))
# survive_fare_survived = pd.merge(survive_fare_died, survive_fare_survived, how="left", on="Fare")
survive_fare_died["Gestorben"][survive_fare_died["Gestorben"] == 0] = None
survive_fare_survived["Überlebt"][survive_fare_survived["Überlebt"] == 0] = None
print(survive_fare_survived)
fig, axes = plt.subplots(figsize=(16, 6), ncols=2, nrows=1, squeeze=False)

survive_fare_survived.plot(style=".", ax=axes[0, 1], legend=False, xlim=(-10, 520), ylim=(-1, 30))
axes[0, 1].set_title("Überlebt")
survive_fare_died.plot(style=".", ax=axes[0, 0], legend=False, color="c", xlim=(-10, 520), ylim=(-1, 30))
axes[0, 0].set_title("Gestorben")

plt.show()
