import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

df = pd.read_csv("dados_mirante_santana.txt",
                    delimiter = ';',
                    skipinitialspace=True,
                    usecols=["Data", "Hora", "TempMaxima"],
                    skiprows=16) 

df_results = pd.read_csv('mlp_001_500.txt',
                    skipinitialspace=True,
                    skiprows=92,
                    skipfooter=12,
                    engine='python')

#for i in range(len(df)):
#    df1.loc[i:i+1,'TempMaxima'] = df.loc[i+1:i+2,'TempMinima']

df['Data'] = pd.to_datetime(df['Data'])
df = df[df.Hora == 0] 
df.set_index('Data', inplace=True)

#df_trinta_anos = df[(df['Data'].dt.year >= 2009) & 
#                    (df['Data'].dt.year <= 2010)] 

df_trinta_anos = df.loc['1980-01-01':'1982-01-01']
df_trinta_anos.plot(y='TempMaxima')
plt.show()
#df_1ano = df[df['Data'].year >= 2009]

#print(df['Data'])
#plt.plot(df_1ano['Data'], df_1ano['TempMaxima'])
#plt.show()



#fig, ax = plt.subplots()
#plt.bar(nan_columns, nan_values)
#plt.show()
#fig, ax = plt.figure()
#ax.plot(dados)
#plt.show()'''
a_list = df_real['TempMaxima'].dropna()
a_list = [7,2,1,2,3,4,2,1,2,3,4,9,9,1,2,3,4,7,4,3,1,2,3,5]
pat = [1,2,3,4]
res = [pat for i in range(len(a_list)) if a_list[i:i+len(pat)] == pat]


