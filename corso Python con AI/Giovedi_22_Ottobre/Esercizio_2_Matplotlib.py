import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


#Genero un array di 365 elementi, costituito da numero visitatori casuali
#La media della distribuzione è 2000 e la deviazione è pari a 500

visitatori = np.random.normal(loc=2000,scale = 500, size = 365)

visitatori = visitatori.round().astype(int)


#Genero il dataframe con colonne "giorno" e "visitatori" precedentemente calcolati
df = pd.DataFrame({ "giorno": range(1, 366), "visitatori": visitatori})

#Groupby per raggruppare in base al giorno
df_v_grouped = df.groupby("giorno")["visitatori"].mean().astype(int)

#Calcolo media, deviazione standard e media mobile su 7 giorni dei visitatori
media_visitatori =df_v_grouped.mean()
dev_visitatori  = df_v_grouped.std()
media_mobile_7 = df_v_grouped.rolling(window=7).mean()


#Plot sullo stesso grafico dei visitatori e della media a 7 giorni 
x = df["giorno"]
y = df["visitatori"]
z = media_mobile_7

#Plot 
plt.plot(x,y)
plt.plot(x, z)

#Titolo 
plt.title("Visitatori Giornalieri")

#X label e Y label 
plt.ylabel("Numero Visitatori")
plt.xlabel("Giorni Considerati")
plt.show()

