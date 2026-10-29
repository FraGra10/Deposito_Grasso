import numpy as np
import pandas as pd 
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

from sklearn.tree import DecisionTreeClassifier

X,y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#knn 
knn = KNeighborsClassifier(n_neighbors=5)
knn = knn.fit(X_train,y_train)
print("Accuratezza senza nessuno scaling: ", round(knn.score(X_test,y_test),5))

#con  standard scaling
scaler = StandardScaler().fit(X_train)
X_train_s = scaler.transform(X_train)
X_test_s  = scaler.transform(X_test)
knn_ss =  KNeighborsClassifier(n_neighbors=5).fit(X_train_s,y_train)
print("Accuratezza con lo Standard Scaler:", round(knn_ss.score(X_test_s,y_test),5))

#con  min max scaling
scaler = MinMaxScaler().fit(X_train)
X_train_mm = scaler.transform(X_train)
X_test_mm  = scaler.transform(X_test)
knn_mm =  KNeighborsClassifier(n_neighbors=5).fit(X_train_mm,y_train)
print("Accuratezza con il MinMax Scaler:", round(knn_mm.score(X_test_mm,y_test),5))

#con Robust scaling 
scaler = RobustScaler().fit(X_train)
X_train_r = scaler.transform(X_train)
X_test_r  = scaler.transform(X_test)
knn_r =  KNeighborsClassifier(n_neighbors=5).fit(X_train_r,y_train)
print("Accuratezza con il RobustScaler:", round(knn_r.score(X_test_r,y_test),5))

############################Decision Tree Classifier###################################################
print(" ")
albero =DecisionTreeClassifier(random_state=0).fit(X_train,y_train)
print("Accuratezza senza nessuno scaling (DTC): ", round(albero.score(X_test,y_test),5))

#con  standard scaling
scaler = StandardScaler().fit(X_train)
X_train_s = scaler.transform(X_train)
X_test_s  = scaler.transform(X_test)
albero_s =DecisionTreeClassifier(random_state=0).fit(X_train_s,y_train)
print("Accuratezza con lo Standard Scaler (DTC):", round(albero_s.score(X_test_s,y_test),5))

#con  min max scaling
scaler = MinMaxScaler().fit(X_train)
X_train_mm = scaler.transform(X_train)
X_test_mm  = scaler.transform(X_test)
albero_mm =DecisionTreeClassifier(random_state=0).fit(X_train_mm,y_train)
print("Accuratezza con il MinMax Scaler (DTC):", round(albero_mm.score(X_test_mm,y_test),5))

#con Robust scaling 
scaler = RobustScaler().fit(X_train)
X_train_r = scaler.transform(X_train)
X_test_r  = scaler.transform(X_test)
albero_r =DecisionTreeClassifier(random_state=0).fit(X_train_r,y_train)
print("Accuratezza con il RobustScaler (DTC):", round(albero_r.score(X_test_r,y_test),5))

#Le soglie di divisione dell'albero si adattano alla nuova scala senza modificare le partizioni dei dati