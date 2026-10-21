import pandas as pd 


#Caricamento dati da file csv in un dataframe
df_scv = pd.read_csv("dataset_esempio_1.csv")

#Visualizzazione prime ed ultime cinque righe del dataframe 
print("Prime 5 righe del dataframe: ")
print(df_scv.head())
print("")
print("Ultime 5 righe del dataframe: ")
print(df_scv.tail())
print("")

#Visualizzazione tipo di dati di ciascuna colonna 
print("Il tipo di ciascuna colonna è: ")
print(df_scv.dtypes)
print("")

#Calcolo la media per le colonne numeriche 
print("La media dell'età nel dataframe è: ")
print(df_scv["Età"].mean())
print("")

print("La media dei salari nel dataframe è: ")
print(df_scv["Salario"].mean())
print("")

#Calcolo la mediana per le colonne numeriche 
print("La mediana dell'età nel dataframe è: ")
print(df_scv["Età"].median())
print("")

print("La mediana dei salari nel dataframe è: ")
print(df_scv["Salario"].median())
print("")

#Calcolo la deviazione standard per le colonne numeriche 
print("La deviazione standard dell'età nel dataframe è: ")
print(df_scv["Età"].std())
print("")

print("La deviazione standard dei salari nel dataframe è: ")
print(df_scv["Salario"].std())
print("")

# Identifico e rimuovo eventuali duplicati 
df = df_scv.drop_duplicates()

#Gestisco i valori mancanti sostituendoli con la mediana dei rispettivi valori 

print(df_scv["Età"].fillna(df_scv["Età"].mean()))
print(df_scv["Età"].fillna(df_scv["Salario"].mean()))

#Aggiungo una nuova colonna categoria

df_scv['Categoria'] = "None"


        
print(df_scv)