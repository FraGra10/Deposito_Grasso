import pandas as pd

#caricamento dataframes
df_1 = pd.read_csv("iscritti.csv")
df_2 = pd.read_csv("presenze.csv")
df_3 = pd.read_csv("costi_abbonamento.csv")

##### Parte 1 ###########
#Stampa degli iscritti originali 
print("Gli iscritti originali sono: \n", df_1["Nome"])
df_eta_35 = df_1[df_1["Eta"] > 35]

#Stampa degli iscritti con età maggiore di 35 anni 
print("\n Gli iscritti con età maggiore di 35 anni sono: \n", df_eta_35["Nome"])

#Valutazione della presenza dell'abbonamento premium nella colonna "Attivo"
df_1["Attivo"] = df_1["Tipo_Abbonamento"] == "Premium"

###### Parte 2 #############
#Rimuovo i duplicati dagli iscritti 
df_1 = df_1.drop_duplicates()

#Rimuovo le righe con almeno un valore nullo 
#df_1 = df_1.dropna()

#Se eta è mancante, sostituisco con la media 
df_1['Eta'] = df_1['Eta'].fillna(df_1['Eta'].mean(), inplace=True)


##################Parte 3 #####################################à
#Definisco ed applico funzione di fascia età
def fascia_eta(i): 
    
    if(i < 18):
        return "Junior"
    if(i >= 18 and i <= 44):
        return "Adulto"
    if(i >= 45):
        return "Senior"
    
df_1["Fascia_Eta"] = df_1["Eta"].apply(fascia_eta)

######### Parte 4 ###########################

#Ordino il dataframe presenze per citta e poi partecipanti 

df_sorted = df_2.sort_values(by='Partecipanti')

print("\nDataFrame ordinato per Partecipanti: \n")
print(df_sorted)

print("\nDataFrame ordinato per Citta: \n")
df_sorted = df_2.sort_values(by='Citta')
print(df_sorted)

#Group by per corso con somma totale dei partecipanti 
df_2_grouped_somma_partecipanti = df_2.groupby("Corso")["Partecipanti"].sum()

print("\n", df_2_grouped_somma_partecipanti, "\n")

#Group by per Città con media dei partecipanti 
df_2_grouped_media_partecipanti = df_2.groupby("Citta")["Partecipanti"].mean()

print("\n", df_2_grouped_media_partecipanti, "\n")

#pivot table 
df_2_pivot = df_2.pivot_table(index="Corso",columns="Citta",values="Partecipanti",aggfunc="mean")

print("\n", df_2_pivot, "\n")

#Parte 3 

new_df = df_1
new_df["Sede"] = ["Nord","Centro","Nord","Centro","Sud","Sud","Sud","Centro","Nord","Sud","Centro"]
new_df["Anno"] = [2024,2025,2025,2024,2025,2024,2024,2025,2024,2025,2024]

df_multi = new_df.set_index(["Sede", "Anno"])

print(df_multi)

#Da completare il merge ed il loc 