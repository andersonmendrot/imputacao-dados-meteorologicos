import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

df = pd.read_csv("dados_mirante_santana.txt",
                    delimiter = ';',
                    skipinitialspace=True,
                    usecols=["Data", "Hora", "TempMaxima"],
                    skiprows=16) 

df['Data'] = pd.to_datetime(df['Data'])
df = df[df.Hora == 0] 
df.set_index('Data', inplace=True)
df.plot(y='TempMaxima')
plt.show()