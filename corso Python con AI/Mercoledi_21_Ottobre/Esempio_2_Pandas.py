import pandas as pd 

data_multi = { 
              
    'Paese': ['Italia', 'Italia', 'Francia', 'Francia'],
    'Anno' : [2023,2024,2023,2024],
    'Vendite':[120,135,110,118]
    
    }


df_multi = pd.DataFrame(data_multi)

df_multi = df_multi.set_index(['Paese'])

#print(" ")
#print(df_multi)



# Dati di esempio
data = {
'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
'Vendite': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

# Creazione della tabella pivot
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')

print(pivot_df)

grouped_df = df.groupby('Data').sum()
print(grouped_df)