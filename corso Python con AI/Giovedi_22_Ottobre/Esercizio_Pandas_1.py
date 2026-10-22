import pandas as pd


#Caricamento dataframe
df_v = pd.read_csv("vendite_esempio.csv")

#Elimino righe con almeno un elemento nullo 
df_v = df_v.dropna()

#esplorazione dati 
print(df_v.describe())

#pivot table per analizzare vendite medie di ciascun prodotto per città 

df_v_pivot = df_v.pivot_table(index="città",columns="prodotto",values="vendite",aggfunc="mean")

print(df_v_pivot)

#Applicazione Group by per calcolare le vendite totali per prodotto
df_v_grouped = df_v.groupby("prodotto")["vendite"].sum()

print(df_v_grouped)