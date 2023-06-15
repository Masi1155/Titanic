import pandas as pd
import spicy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

csv = pd.read_csv("TitanicData.csv")
csv["Survived"].replace(to_replace=0, value=False, inplace=True)
csv["Survived"].replace(to_replace=1, value=True, inplace=True)
survivors = csv.groupby("Survived").agg({"PassengerId": "count"})

csv['Title'] = csv['Name'].str.split('.', expand=True)[0].str.split(',', expand=True)[1]
csv['Surname'] = csv['Name'].str.split('.', expand=True)[0].str.split(',', expand=True)[0]
csv['Name'] = csv['Name'].str.split('.', expand=True)[1]

title = csv.groupby('Title').agg({'Title': 'count'})


def get_class_title(elems):
    titles = ["Capt", "Col", "Don", "Dr", "Jonkheer", "Lady", "Major", "Master", "Miss", "Mlle", "Mme", "Mr", "Mrs",
              "Ms", "Rev", "Sir", "the Countess"]
    res = {}

    for title in titles:
        if elems:
            pass


titleSurvived = csv[['Title', 'Survived', 'Pclass']].groupby('Title').apply(lambda x: (x['Survived']).sum())
pclass_title = csv[['Title', 'Pclass', 'Survived']].groupby(['Pclass', 'Title']).count()
titleSurvived = csv.groupby('Title').agg({'Survived': 'count', 'Pclass': 'count'})
titleSurvived['Total'] = title['Title']

fig, axes = plt.subplots(nrows=3, ncols=2, squeeze=False, figsize=(18, 10))
plt.subplots_adjust(wspace=0.2, hspace=0.8)

# Title zu Überlebt zu Klasse
pclass_title.plot(label='', subplots=True, legend=False, ax=axes[0, 0])
axes[0, 0].set_title('Titel Klasse Überlebt Verteilung')

# Überlebende zu Fare
survive_fare_survived = csv.groupby('Fare').apply(lambda x: pd.Series((x['Survived']).sum(), index=['Überlebt']))
survive_fare_died = csv.groupby('Fare').apply(lambda x: pd.Series((x['Survived'] == False).sum(), index=['Gestorben']))
# survive_fare_survived = pd.merge(survive_fare_died, survive_fare_survived, how="left", on="Fare")
survive_fare_died["Gestorben"][survive_fare_died["Gestorben"] == 0] = None
survive_fare_survived["Überlebt"][survive_fare_survived["Überlebt"] == 0] = None

survive_fare_survived.plot(style=".", ax=axes[1, 1], legend=False, xlim=(-10, 520), ylim=(-1, 30))
axes[1, 1].set_title("Überlebt")
survive_fare_died.plot(style=".", ax=axes[1, 0], legend=False, color="c", xlim=(-10, 520), ylim=(-1, 30))
axes[1, 0].set_title("Gestorben")

# Age to Fare

# age_fare =

plt.show()
