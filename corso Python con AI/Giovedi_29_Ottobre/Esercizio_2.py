import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler


df = pd.DataFrame({
    "eta" : [20, 25, 32, 38, 45, 52, 61, 70],
    "reddito_annuo" : [15000, 22000, 35000, 48000, 65000, 80000, 100000, 120000],
    "figli"         : [0, 0, 1, 2, 2, 3, 1, 4]
})

ss = StandardScaler().fit(df).set_output(transform="pandas")

df_s = ss.transform(df) 

#print(df_s)

#Un valore di 1.5 nella colonna reddito_annuo indica che quel valore è circa 1.5*deviazione standard della colonna di reddito_annuo sopra la media

