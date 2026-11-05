#L'errore in questo codice è dovuto al fatto che eseguiamo prima il fit_transform sull'intero dataset X 
#e solo successivamente eseguiamo lo split in X_train ed X_test. Questo è un problema perchè in questo modo
#le statistiche sono imparate anche su dati appartenenti a X_test, causando data leakage.

from sklearn.datasets import load_digits
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y= True)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

scaler = MinMaxScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)