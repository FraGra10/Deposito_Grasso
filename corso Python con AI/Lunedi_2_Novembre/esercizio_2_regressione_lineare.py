from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd 

data = fetch_california_housing(as_frame=True)
X, y = data.data, data.target              
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modello = LinearRegression().fit(X_train, y_train)

#coefficienti del modello non scalato 
coefficienti = pd.Series(modello.coef_, index=X.columns).sort_values()
#print("Coefficienti non scalati: \n", coefficienti.round(1))

#Score del modello non scalato                          
print("R² sul test:", round(modello.score(X_test, y_test), 3))  

#####################
scaler = StandardScaler().fit(X_train)
X_train_s = scaler.transform(X_train)
X_test_s = scaler.transform(X_test)
modello_1 = LinearRegression().fit(X_train_s, y_train)

#coefficienti del modello scalato
coefficienti_s = pd.Series(modello_1.coef_, index=X.columns).sort_values()
#print("Coefficienti scalati: \n", coefficienti_s.round(1))

#Score del modello scalato                          
print("R² sul test:", round(modello_1.score(X_test_s, y_test), 3))   


confronto = pd.DataFrame({
    "Non scalati": coefficienti,
    "Scalati": coefficienti_s
})

print(confronto.round(2))

############################################################################################################
#Nel modello senza standardizzazione, la feature con il coefficiente di maggior valore assoluto è AveBedrms (0,78). 
#Nel modello con StandardScaler, invece, il coefficiente maggiore in valore assoluto è quello di Latitude (-0,90), 
#seguito da Longitude (-0,87) e MedInc (0,85).

#Senza scaling, i coefficienti non sono direttamente confrontabili perché dipendono dalle unità di misura delle feature. 
#Con la standardizzazione, invece, i coefficienti permettono di valutare meglio 
#l'importanza relativa delle variabili nel modello.