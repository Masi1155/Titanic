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

# csv['Title'], csv['Name'] = csv['Name'].apply(lambda x: x.split("."))[1][0].split(",")
# print(csv['Title'])
# csv['Surname'], csv['Title'] = csv['Title'].apply(lambda x: x.split(","))
# print(temp[1][0])
csv['Title'] = csv['Name'].str.split('.', expand=True)[0].str.split(',', expand=True)[1]
csv['Surname'] = csv['Name'].str.split('.', expand=True)[0].str.split(',', expand=True)[0]
csv['Name'] = csv['Name'].str.split('.', expand=True)[1]
# csv[['Surname', 'Title']] = csv['Title'].str.split(',', 1, expand=True)

# title = csv.groupby('Title').describe()
print(csv[['Title', 'Surname', 'Name']])
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

title = csv.groupby('Title').agg({'Title':'count'})
#print(title)



def get_class_title(elems):
    titles = ["Capt", "Col", "Don", "Dr", "Jonkheer","Lady","Major","Master","Miss","Mlle","Mme","Mr","Mrs","Ms","Rev","Sir", "the Countess"]
    res = {}

    for title in titles:
        if elems:
            pass

titleSurvived = csv[['Title','Survived', 'Pclass']].groupby('Title').apply(lambda x: (x ['Survived']).sum())
pclass_title = csv[['Title','Pclass','Survived']].groupby(['Pclass', 'Title']).count()
print(pclass_title)
    #.apply(lambda x: pd.Series((x['Pclass']==1),index = ['First','Second','Third']))
titleSurvived = csv.groupby('Title').agg({'Survived':'count','Pclass':'count'})
titleSurvived['Total'] = title['Title']
#print(titleSurvived)

fig, axes = plt.subplots(nrows=3, ncols=2, squeeze= False)
plt.subplots_adjust(wspace= 0.2, hspace=0.8)
pclass_title.plot(label = '', subplots = True, legend = False, ax = axes[0,0])
axes[0,0].set_title('Titel Klasse Überlebt Verteilung')



plt.show()