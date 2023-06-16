import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv = pd.read_csv('flag.csv')
language = csv.groupby('language').agg({'language':'count'})
language.rename(index= {1:'Englisch', 2:'Spanisch',3:'Französisch', 4:'Deutsch',
                        5:'Slavic',6:'Andere Europäische', 7:'Chinesisch',
                        8:'Arabisch', 9:'Japanese/Turkish/Finnish/Magyar', 10:'Andere'}, inplace = True)
print(language['language'])
language.plot.pie(subplots = True, legend = False, ylabel = '')



plt.show()