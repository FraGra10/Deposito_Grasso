import pandas as pd 

# Creazione di un DataFrame con dati di esempio
data = {
'Nome': ['Alice', 'Bob', 'Carla'],
'Età': [25, 30, 22],
'Città': ['Roma', 'Milano', 'Napoli']
}

# aggiunta di una chiave al dizionario
data["Sesso"] = "F"
data["Exp"]   = ["120","35","71"]

df = pd.DataFrame(data)

print(df)
print("")

print(df.head()) #prime 5 righe 
print(df.tail()) # ultime 5 righe 
print(df.describe()) #descrizione dei dati numerici delle colonne del dataset,statistiche medie

print("Info del database:")
print(df.info()) #riporta descrizioni generali di tutte le colonne, tipo e quanti elementi non nulli 