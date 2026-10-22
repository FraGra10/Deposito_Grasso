import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


#Generazione del dataset 

temperature = np.random.uniform(14,26, size = 30)
temperature = temperature.round(1)


df = pd.DataFrame({"Temperatura": temperature})

media = df["Temperatura"].mean()
massima = df["Temperatura"].max()
minima = df["Temperatura"].min()
mediana = df["Temperatura"].median()


# Grafico con Matplotlib
x =         ["Media", "Massima", "Minima", "Mediana"]
y =         [media, massima, minima, mediana]
colori =    ["green", "red", "blue", "orange",]


plt.plot(x, y)
plt.title("Statistiche delle temperature del mese")
plt.ylabel("Temperatura (°C)")
plt.grid()
plt.show()


