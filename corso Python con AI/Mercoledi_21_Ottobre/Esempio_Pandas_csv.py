import pandas as pd 

df_scv = pd.read_csv("studenti.csv")

#come aggiungere nuova colonna 

df_scv["Sesso"] = ["F","M","F","F","M","F","F","M","F","E"]
print(df_scv)


#caricamento del contenuto del file 

df_scv["promosso"] = df_scv["voto"] >= 6

# è il broadcasting, 6 ha solo una dimensione, df_scv["voto"] ha 10 dimensioni
#sto creando una colonna promosso nel mio cvs dove assegno a True i voti >=6 e False i minori 

print("")
print(df_scv)

print("")
#stampa media dei voti 
print("La media dei voti è:",df_scv["voto"].mean())
print("Il maggiore dei voti è:",df_scv["voto"].max())

print(df_scv[df_scv["voto"] > 7])

#questo non è una funzione universale 

#Salvare il file in un nuovo CSV 
df_scv.to_csv("Studenti_aggiornato.csv", index =False )