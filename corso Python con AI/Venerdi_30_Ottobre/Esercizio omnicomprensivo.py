### 1) Definizione del problema #######################

# Il tipo di apprendimento è supervisionato, dal momento che il modello 
# impara la relazione X------> y.
# Il problema è di classificazione binaria: y è una categoria che può 
# assumere valori pari a 1 o a 0 (benigno/maligno)
# Il target è la colonna che vogliamo prevedere quindi la colonna di 
# 0 e 1 per definire se un tumore è maligno o benigno in base alle features.


### 2) Esplorazione dei dati ##################################

from sklearn.datasets import load_breast_cancer

breast_cancer = load_breast_cancer(as_frame=True)

X = breast_cancer.data 
y = breast_cancer.target 

print("La forma di X è:", X.shape)
print("")
print("La forma di y è:", y.shape)
print("")
print("I nomi delle features sono: ", breast_cancer.feature_names)
print("")
print("I nomi delle classi sono: ", breast_cancer.target_names)
print("")
print("Le prime cinque righe sono: ", X[:5])
print("")
print("Descrizione di breast cancer:" , breast_cancer.DESCR[:249])
print("")
print("Il numero di campioni per classe è pari a : \n ", y.value_counts())
#Le classi sono leggermente sbilanciate

print(X.describe().loc[["min", "max"]])

scale = X.max() - X.min()

print("Feature con scala più grande:")
print(scale.idxmax(), ":", scale.max())

print("\nFeature con scala più piccola:")
print(scale.idxmin(), ":", scale.min())
print("")

#La presenza di questa differenza così grande nelle scale, porterà a un processo di standardizzazione
#dal momento che alcune feature potrebbero pesare di più sulla validazione del modello, portando il 
#modello ad essere meno bravo a predire . 

##################################3) Divisione dei dati ########################################
from sklearn.model_selection import train_test_split

X,y = load_breast_cancer(return_X_y=True)

X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42,stratify=y_temp)

#Dimensioni dei tre insiemi
print("Dimensione di X_test: ", X_test.shape)
print("Dimensione di X_train: ", X_train.shape)
print("Dimensione di X_val: ", X_val.shape )
print("")

# Percentuale di maligni (classe 0)
print("Percentuale di maligni nel training:",
      (y_train == 0).mean() * 100, "%")

print("Percentuale di maligni nella validation:",
      (y_val == 0).mean() * 100, "%")

print("Percentuale di maligni nel test:",
      (y_test == 0).mean() * 100, "%")


#################################4) Baseline #########################################################
#################################5) Primo modello: KNN senza scaling ##################################

