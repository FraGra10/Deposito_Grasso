from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd 


X, y = load_wine(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0, stratify=y)

gini_training_accuracy = []
gini_test_accuracy = []
entropy_training_accuracy = [] 
entropy_test_accuracy = [] 

for i in range(1,7):
    gini_tree = DecisionTreeClassifier(criterion= "gini", max_depth= i, random_state= 0).fit(X_train, y_train)
    gini_training_accuracy.append(gini_tree.score(X_train, y_train))
    gini_test_accuracy.append(gini_tree.score(X_test, y_test))
    
    
    entr_tree = DecisionTreeClassifier(criterion="entropy", max_depth= i, random_state= 0).fit(X_train, y_train)
    entropy_training_accuracy.append(entr_tree.score(X_train, y_train))
    entropy_test_accuracy.append(entr_tree.score(X_test, y_test))    


df = pd.DataFrame({
    "max_depth": range(1,7),
    "Gini Train": gini_training_accuracy,
    "Gini Test" : gini_test_accuracy,
    "Entr Train": entropy_training_accuracy,
    "Entr Test" : entropy_test_accuracy     
})

df = df.set_index("max_depth")
print(df)
print("")
print("Migliore Test con Gini:", df["Gini Test"].max())
print("Migliore depth con Gini:", df["Gini Test"].idxmax())
print("Migliore Test con Entr:", df["Entr Test"].max())
print("Migliore depth con Entr:", df["Entr Test"].idxmax())