from sklearn.datasets import load_wine
from sklearn.datasets import load_diabetes

wine = load_wine()
X = wine.data            
y = wine.target  

if(y.dtype == "float64"):
    print("Problema di regressione")
else:
    print("Problema di classificazione")

diabetes = load_diabetes()
X = diabetes.data            
y = diabetes.target 

if(y.dtype == "float64"):
    print("Problema di regressione")
else:
    print("Problema di classificazione")