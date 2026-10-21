import pandas as pd


#caricamento dati in un dataframe 
df_pr = pd.read_csv("dataset_prodotti.csv")

#aggiunta colonna Totale Vendite

df_pr["totale vendite"] = df_pr["quantità"]*df_pr["prezzo unitario"]

#print(df_pr)

#Calcolo il totale delle vendite raggrupprando per prodotto 
grouped_df_pr_1 = df_pr.groupby("prodotto")["totale vendite"].sum()
#print(grouped_df_pr)

#Calcolo il prodotto più venduto in termini di quantità 
grouped_df_pr_2 = df_pr.groupby("prodotto")["quantità"].sum()
max_quantità = grouped_df_pr_2.max()
prodotto = grouped_df_pr_2.loc[grouped_df_pr_2 == max_quantità].index[0]

print("La massima quantità venduta è:", max_quantità , "ed appartiene all'oggetto:", prodotto)
print("")

grouped_df_pr_3 = df_pr.groupby("città")["totale vendite"].sum()
print(grouped_df_pr_3)

#Citta con il maggior numero di vendite 
max_vendita = grouped_df_pr_3.max()
citta_max_vendita = grouped_df_pr_3.loc[grouped_df_pr_3 == max_vendita].index[0]
print("La città con il maggior volume di vendite totali è:", citta_max_vendita)
print("")

#Nuovo dataframe con vendite superiori ad un certo valore 

new_df = df_pr[df_pr["totale vendite"] > 1000]

print(new_df)