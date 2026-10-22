import pandas as pd 

data = {'nome': ['Alice', 'Bob'],
        'età' : [25,30]}

df = pd.DataFrame(data)


#esploro i dati con describe 
print(df.describe())
#rimuovo i valori mancanti 
df = df.dropna()
#Selezione di una colonna 
ages = df['età']
adults = df[df["età"] > 25] 

#ordinamento dati per età , ordina i valori in base a una colonna
df_sorted = df.sort_values(by='età')

#unione di due dataframe in base ad una colonna che devono avere in comune,
#se non hanno colonne in comune dobbiamo inventarla oppure non possono essere uniti 

merged_df = pd.merge(df, df_csv, on='name')

#Le trasformazioni non si fanno in pandas di solito, servono a creare
#una colonna dove applico una modifica, ovvero operazione vettoriale
#Trasformare un dato lo cambia; la manipolazione tocca  i dati invece 

#Vedi esempi sulle slide su pivot 

#Infine esportazione su csv 