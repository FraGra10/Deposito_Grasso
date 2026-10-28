from sklearn.datasets import load_digits 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd 

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  #split del Training e Test Set


modelli = {
    "KNN": KNeighborsClassifier(n_neighbors=5),                       #dict dei modelli considerati 
    "Albero": DecisionTreeClassifier(random_state=42),
    "Random_Forest": RandomForestClassifier(random_state=42)
}


for nome, modello in modelli.items():
    modello.fit(X_train, y_train)                  
    print(f" accuratezza test: {modello.score(X_test, y_test):.2f}") #Addestro il modello su tutti e tre gli algoritmi


random_state = [0,30,60]    #Creo una lista con tre valori diversi di random_state 
knn = []
decision_tree = []
random_forest = []


for rs in random_state:
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rs)
    
    for nome, modello in modelli.items():
        modello.fit(X_train, y_train)
        accuratezza = modello.score(X_test, y_test)     #Salvo i tre valori di accuratezza relativi ad ogni modello                
        print(f"accuratezza test: {accuratezza:.2f}")
        
        if(nome == "KNN"):
            knn.append(accuratezza)
        elif(nome == "Albero"):
            decision_tree.append(accuratezza)
        else:
            random_forest.append(accuratezza)


df = pd.DataFrame({
#Creo dataframe con chiavi i tre alogoritmi e con righe i valori associati al random_state 
    "KNN": knn,
    "Albero": decision_tree,
    "Random_Forest": random_forest
    
})

df.index = random_state

print(df)