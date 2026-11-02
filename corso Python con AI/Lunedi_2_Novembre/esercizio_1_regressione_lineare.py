# Scrivi qui la tua soluzione
import numpy as np
from sklearn.linear_model import LinearRegression


temp = np.array([[18],[21],[24],[27],[30],[33]])
gel_venduti = np.array([[120],[150],[190],[230],[260],[310]])

modello = LinearRegression().fit(temp, gel_venduti)
print("Coefficiente w:", round(modello.coef_[0][0],3))                    
print("Intercetta b:", round(modello.intercept_[0]))               
print("Previsione 29°:", modello.predict([[29]]))

#il coefficiente ci dice quanti gelati vengono venduti in base ad una variazione unitaria della temperatura
