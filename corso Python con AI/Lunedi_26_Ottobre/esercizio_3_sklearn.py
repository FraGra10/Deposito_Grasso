from sklearn.datasets import load_breast_cancer

breast_cancer = load_breast_cancer()
#print(breast_cancer.keys())

print(len(breast_cancer.data))             #Numero di campioni
print(len(breast_cancer.feature_names))   #Numero di features
print(breast_cancer.target_names)         #Nomi delle due classi 
print(breast_cancer.feature_names[0:5])   #nomi primi 5 features
