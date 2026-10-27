# Scrivi qui la tua soluzione
import pandas as pd 

auto_usate = {
    "km": [50000, 80000, 120000, 45000, 95000, 70000],
    "anni": [3, 5, 8, 2, 7, 4],
    "cilindrata": [1200, 1600, 2000, 1000, 1400, 1800],
    "prezzo": [15000, 12000, 8500, 18000, 9000, 14000],
    "incidentata": ["no", "no", "si", "no", "si", "no"]
}
df = pd.DataFrame(auto_usate)

feature= ["km","anni","cilindrata"]
########################################Primo caso 

X = df[feature + ["incidentata"]]
y = df["prezzo"]

#Problema di Regressione 

print(X.shape)
print(y.shape)
print(" ")
########################################Secondo caso 

X = df[feature]
y = df["incidentata"]

print(X.shape)
print(y.shape)

#Problema di classificazione