from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


acc_wrong = []

#vettore di random state 
random_state = [0,10,20,30,40,50,60,70,80,90]

X,y = load_breast_cancer(return_X_y= True)

#Scaling fatto sull'intero dataset di partenza 
X = MinMaxScaler().fit_transform(X)


#Calcolo dell'accuracy score per diversi valori di random state con scaling prima dello split 
for i in random_state:
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=i)
    knn_wrong = KNeighborsClassifier(n_neighbors=3).fit(X_train,y_train)
    acc_wrong.append(knn_wrong.score(X_test,y_test))


X,y = load_breast_cancer(return_X_y= True)

acc_score_right= []

#Calcolo dell'accuracy score per diversi valori di random state con split prima dello scaling

for i in random_state:
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=i)
    scaler = MinMaxScaler()
    X_train_mm = scaler.fit_transform(X_train)
    X_test_mm  = scaler.transform(X_test)
    
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train_mm,y_train)
    acc_score_right.append(knn.score(X_test_mm,y_test))

    
print("Media dell'accuratezza con scaling prima dello split: ", sum(acc_wrong)/len(acc_wrong))
print("Media dell'accuratezza con split prima dello scaling: ", sum(acc_score_right)/len(acc_score_right))
