### 1) Definizione del problema #######################
#1. Indica il tipo di apprendimento e di problema (supervisionato/non supervisionato, 
#classificazione/regressione, binaria/multiclasse) e quale colonna è il **target**.

# Il tipo di apprendimento è supervisionato, dal momento che il modello 
# impara la relazione X------> y.
# Il problema è di classificazione binaria: y è una categoria che può 
# assumere valori pari a 1 o a 0 (benigno/maligno)
# Il target è la colonna che vogliamo prevedere quindi la colonna di 
# 0 e 1 per definire se un tumore è maligno o benigno in base alle features.


### 2) Esplorazione dei dati ##################################
#1. Carica il dataset con `as_frame=True`.
#2. Stampa:
#   - forma di X e di y;
#   - nomi delle feature e delle classi;
#   - le prime 5 righe;
#   - il contenuto di `DESCR` (leggi almeno origine e unità di misura).
#3. Controlla quanti campioni ci sono per classe con `value_counts()`: le classi sono bilanciate?
#4. Calcola con `describe()` minimo e massimo di tutte le feature. Individua la feature con scala più
#  grande e quella con scala più piccola, e annota perché saranno importanti più avanti.
#5. Separa chiaramente `X` e `y`, senza lasciare il target dentro `X`.

from sklearn.datasets import load_breast_cancer

#1)
#Caricamento dataset
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
### 3. Divisione dei dati *(1.5, 1.7, 2.2, 2.5)*
#1. Dividi in **training 60% / validation 20% / test 20%** con due chiamate a `train_test_split`.
#2. Usa `random_state=42` e `stratify=y` in entrambe.
#3. Stampa le dimensioni dei tre insiemi e la percentuale di maligni in ciascuno

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
#1. Addestra un `DummyClassifier(strategy="most_frequent")` e calcola l'accuratezza sul validation set.
#2. Calcola anche la recall sui maligni (`pos_label=0`, `zero_division=0`).
#3. Commenta: perché questa soglia minima va battuta e perché l'accuratezza da sola può ingannare?

from sklearn.dummy import DummyClassifier
from sklearn.metrics import recall_score

#Definizione ed addestramento DummyClassifier 
Dummy = DummyClassifier(strategy="most_frequent").fit(X_train,y_train)

#calcolo accuratezza del modello sul validation set 

val_accuracy = Dummy.score(X_val,y_val)
y_pred = Dummy.predict(X_val)

#Calcolo del recall sui maligni 
mal_recall = recall_score(y_val,y_pred, pos_label= 0, zero_division= 0)

print("Accuratezza sul validation set: ", val_accuracy)
print("recall sui maligni:", mal_recall)

#Il DummyClassifier predice sempre la classe più frequente senza imparare la relazione tra dati e target.
#Rappresenta quindi un livello minimo di prestazioni 
#L'accuratezza inganna perchè misura soltano la percentuale di predizioni corrette,senza considerare quali
#classi vengono riconosciute.
#Dobbiamo utilizzare le metriche aggiuntive come la recall per capire se il modello riconosce effettivamente
#entrambe le classi 


#################################5) Primo modello: KNN senza scaling ##################################
#1. Addestra un `KNeighborsClassifier(n_neighbors=5)` sui dati grezzi, usando la sequenza 
# `fit` → `predict` → `score`.
#2. Riporta l'accuratezza su training e su validation.
#3. Per un campione del validation set usa `kneighbors` per mostrare distanze, indici e classi
# dei 5 vicini, e `predict_proba` per mostrare la frazione di voti.
#4. Identifica la feature che pesa di più nel calcolo della distanza e spiega perché è un problema.
from sklearn.neighbors import KNeighborsClassifier

#Definizione ed addestramento di un KNN Classifier 
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

#Predict sul validation e training set 
y_train_pred = knn.predict(X_train)
y_val_pred = knn.predict(X_val)

#Misura dell'accuratezza sui due set 
acc_train = knn.score(X_train, y_train)
acc_val = knn.score(X_val, y_val)

#print(f"Accuracy training:{round(acc_train,3)}")
#print(f"Accuracy validation: {round(acc_val,3)}")

#Campione di indice 0 del validation set 
x = X_val[0].reshape(1, -1)

# Troviamo i 5 vicini più prossimi nel training set
distanze, indici = knn.kneighbors(x)

# Classi dei 5 vicini
classi_vicini = y_train[indici[0]]

#predict_proba
prob = knn.predict_proba(x)


#La feature che pesa di più nel calcolo della distanza è quella con la scala numerica più alta: 
#KNN utilizza le distanze tra i campioni per individuare i vicini più prossimi. 
# Se una feature ha valori numericamente molto più grandi rispetto alle altre, 
# può dominare il calcolo della distanza.

#Di conseguenza, le feature con scale più piccole rischiano di avere un'influenza trascurabile 
#sulla classificazione.

###### 6) Scaling e regola d'oro ########################################################

#1. Applica `StandardScaler` rispettando la regola d'oro:
#   - `fit` solo sul training;
#   - `transform` su training, validation e test (il test lo scali ora ma non lo usi ancora).
#2. Verifica che le colonne del training scalato abbiano media ≈ 0 e deviazione standard ≈ 1,
# e che quelle del validation **non** abbiano media esattamente 0. Spiega perché è corretto.
#3. Riaddestra il KNN con k = 5 sui dati scalati e confronta l'accuratezza di validation
# con quella del punto 5.
#4. Prova `MinMaxScaler` e confronta il risultato con `StandardScaler`.
#5. Commenta quali modelli di questo esercizio hanno bisogno dello scaling e quali no.

from sklearn.preprocessing import StandardScaler,MinMaxScaler
X,y = load_breast_cancer(return_X_y=True)

X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42,stratify=y_temp)

#Applicazione Standard Scaler con fit solo sul set di training ;  transform su tutti e tre 
scaler = StandardScaler().fit(X_train)
X_train_s = scaler.transform(X_train)
X_val_s = scaler.transform(X_val)
x_test_s = scaler.transform(X_test)

print("Le colonne del training scalato hanno media pari a :", X_train_s.mean(axis = 0))
print("Le colonne del training scalato hanno deviazione standard pari a :", X_train_s.std(axis = 0))
print("Le colonne del validation scalato hanno media pari a :", X_val_s.mean(axis = 0) )

#è corretto che la  media del validation non sia esattamente zero,
# perché ho applicato il transform() usando i parametri calcolati sul training

#Riaddestramento del modello sui dati scalati 
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_s, y_train)

acc_val_2 = knn.score(X_val_s, y_val)

#Print delle due accuratezze
print("L'accuratezza del validation senza scaling è:", acc_val)
print("L'accuratezza del validation con standard scaling è : ", acc_val_2)

#Lo scaling ha migliorato l'accuratezza del modello 
scaler = MinMaxScaler().fit(X_train)
X_train_mm = scaler.transform(X_train)
X_val_mm = scaler.transform(X_val)
x_test_mm = scaler.transform(X_test)

#Addestramento e scaling con Min-Max 
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_mm, y_train)
acc_val_3 = knn.score(X_val_mm, y_val)

print("L'accuratezza del validation con min-max scaling è : ", acc_val_3)

####

#KNN ha bisogno dello scaling perchè si basa sulle distanze tra le osservazioni, senza scaling
#la distanza tra due campioni sarebbe determinata quasi tutta dalla feature con valori maggiori 
#(se la sua scala è molto maggiore rispetto a quella delle altre features)

#Gli alberi decisionali no perchè le decisioni si basano su soglie delle singole features , e quindi 
#non risentono dello scaling. 

###### 7) Scelta di k e diagnosi del modello ########################################################
#1. Con i dati scalati, per k dispari da 1 a 41 calcola l'accuratezza su training e su validation.
#2. Disegna la **curva di complessità** (k sull'asse x, accuratezza sull'asse y, due linee).
#3. Individua sul grafico la zona di **overfitting** (k piccolo) e quella di **underfitting** (k grande).
#4. Scegli il miglior k **solo guardando il validation set**.

import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler,MinMaxScaler
X,y = load_breast_cancer(return_X_y=True)

X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42,stratify=y_temp)

scaler = StandardScaler().fit(X_train)
X_train_s = scaler.transform(X_train)
X_val_s = scaler.transform(X_val)
x_test_s = scaler.transform(X_test)

valori_k = range(1,43,2)

acc_train = []
acc_validation = []

#Calcolo dell'accuratezza di training e validazione su valori diversi di k 
for k in valori_k:
      knn = KNeighborsClassifier(n_neighbors=k).fit(X_train_s,y_train)
      acc_train.append(knn.score(X_train_s,y_train))
      acc_validation.append(knn.score(X_val_s,y_val))

#Plot della curva di complessità 

plt.plot(valori_k,acc_train, label = "training")
plt.plot(valori_k,acc_validation, label= "validation")

plt.xlabel("k")
plt.ylabel("accuratezza")

plt.legend(); plt.title("Curva di complessità con KNN")
plt.grid()
plt.xticks(valori_k)
plt.show()
      
best_val_accuracy = 0.0
index = 0

#Miglior valore di k guardando il validation set

for i in range(len(acc_validation)):
      if(acc_validation[i] > best_val_accuracy):
            best_val_accuracy = acc_validation[i]
            index = i
            
print("Il migliore k guardando il validation set è :", valori_k[index])


###### 8) Secondo modello: albero di decisione ########################################################
#1. Addestra un `DecisionTreeClassifier` per `max_depth` in `[1, 2, 3, 5, 8, None]`, **sui dati non scalati**.
#2. Per ogni valore stampa numero di foglie, accuratezza su training e su validation, in una tabella pandas.
#3. Scegli la profondità migliore sul validation e giustifica la scelta.
#4. Con quella profondità, mostra l'albero con `export_text` (e `plot_tree` se vuoi). Scrivi in italiano le prime due regole che l'albero applica.
#5. Calcola a mano l'indice di Gini del nodo radice dalle frazioni delle due classi e verificalo con `albero.tree_.impurity[0]`.
#6. Spiega perché per l'albero lo scaling non cambierebbe le decisioni. Per verificarlo, riaddestralo sui dati scalati e confronta.

from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

dep_values = [1, 2, 3, 5, 8, None]

risultati = []

for depth in dep_values:
    albero = DecisionTreeClassifier(max_depth=depth, random_state=42)
    albero.fit(X_train, y_train)

    foglie = albero.get_n_leaves()
    acc_train = albero.score(X_train, y_train)
    acc_val = albero.score(X_val, y_val)

    risultati.append({
        "max_depth": depth,
        "foglie": foglie,
        "accuracy_train": acc_train,
        "accuracy_validation": acc_val
    })
    
df = pd.DataFrame(risultati)

print(df)

#La profondità migliore è quella che produce la maggiore accuratezza sul validation set.
#Profondità troppo piccola: possibile underfitting.
#Profondità troppo grande:  possibile overfitting.
#Profondità intermedia: buon compromesso
#max_depth pari a 5 è la scelta

#Riaddestramento dell'albero con max_depth pari a 5 
albero = DecisionTreeClassifier(max_depth=5, random_state=42)
albero.fit(X_train, y_train)

regole = export_text(albero, feature_names=list(
    load_breast_cancer().feature_names
))

print(regole)
#Le prime due regole che l'albero applica sono:
#Valutare se worst concave points è minore o uguale a 0.15 e valutare se worst area è minore o uguale a 929.80.
#Se la condizione su worst area è soddisfatta, viene associata la classe 1 al campione considerato.

#Lo scaling non cambierebbe le decisioni per l'albero perchè se applichiamo uno scaling, 
# i valori della feature cambiano, ma anche la soglia viene trasformata di conseguenza.

#Calcolo dell'indice di gini sul nodo radice 

fraz = np.bincount(y_train)/len(y_train)

print("Gini radice (manuale):", round(1 - (fraz**2).sum(),3))
print("Gini radice (sklearn):", round(albero.tree_.impurity[0],3))

#Confronto tra l'albero scalato e quello non scalato 
albero_s = DecisionTreeClassifier(max_depth=5,random_state=42)

albero_s.fit(X_train_s, y_train)

acc_train_scalato = albero_s.score(X_train_s, y_train)
acc_val_scalato = albero_s.score(X_val_s, y_val)

print("Albero non scalato:")
print("Training:", albero.score(X_train, y_train))
print("Validation:", albero.score(X_val, y_val))

print("\nAlbero scalato:")
print("Training:", acc_train_scalato)
print("Validation:", acc_val_scalato)

####9) Valutazione Finale ####################
#1. Riaddestra i due modelli scelti (KNN con il k scelto, albero con la profondità scelta) su
# **training + validation** uniti, con lo scaler rifatto sul nuovo training per il KNN. 
# Poi valutali sul test set.
#2. Per ciascun modello e per il Dummy calcola, con la classe positiva = **maligno** (`pos_label=0`):
#   - accuratezza, precision, recall, F1;
#   - `classification_report` con i nomi delle classi.
#3. Disegna la matrice di confusione dei due modelli (`ConfusionMatrixDisplay` o heatmap seaborn).
#4. Calcola a mano TP, TN, FP, FN dalla matrice del modello migliore e verifica precision e recall con le formule.
#5. Scegli il modello finale secondo il criterio clinico (i falsi negativi sono più gravi) e motiva la scelta in 4–5 righe.
#6. Riporta la stima finale che comunicheresti alla direzione e spiega perché è affidabile.

#Punto 1 
import numpy as np 
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,classification_report,confusion_matrix

X_train_f = np.concatenate((X_train, X_val), axis=0)
y_train_f = np.concatenate((y_train, y_val), axis=0)

#Scaler sul nuovo insieme train + validation
scaler_f = StandardScaler()

scaler_f.fit(X_train_f)

X_train_f_s = scaler_f.transform(X_train_f)
X_test_s = scaler_f.transform(X_test)

#Knn finale sul nuovo training set 

knn_f = KNeighborsClassifier(n_neighbors=3)
knn_f.fit(X_train_f_s, y_train_f)

y_pred_knn = knn_f.predict(X_test_s)


#DecisionTreeClassifier sul nuovo training set 
tree_final = DecisionTreeClassifier(max_depth=5,random_state=42)

tree_final.fit(X_train_f, y_train_f)

# Predizioni sul test
y_pred_tree = tree_final.predict(X_test)

#Dummy 
Dummy = DummyClassifier(strategy="most_frequent")
Dummy.fit(X_train_f, y_train_f)

y_pred_dummy = Dummy.predict(X_test)

########################################################################################################
#Punto 2 
#Definizione della funzione per ottenere le metriche dei tre modelli 
def metriche_modello(y_test, y_pred, nome):
      
    print("")
    print(f"--- {nome} ---")

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, pos_label=0, zero_division=0)
    recall = recall_score(y_test, y_pred, pos_label=0, zero_division=0)
    f1 = f1_score(y_test, y_pred, pos_label=0, zero_division=0)

    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1:", f1)

    print("\nClassification Report:")
    print(classification_report(
        y_test,
        y_pred,
        labels=[0, 1],
        target_names=["Maligno", "Benigno"],
        zero_division=0
    ))
    
metriche_modello(y_test,y_pred_dummy,"Dummy")
metriche_modello(y_test,y_pred_knn,"KNN")
metriche_modello(y_test,y_pred_tree,"DTC")


###########################################################
#Punto 3 
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#Confusion matrix dei due modelli 
cm_knn = confusion_matrix(y_test,knn_f.predict(X_test_s))
cm_alb = confusion_matrix(y_test,tree_final.predict(X_test))

#Visualizzazione della confusion matrix per knn 
disp = ConfusionMatrixDisplay(confusion_matrix=cm_knn, display_labels=["Maligno", "Benigno"] )

disp.plot(cmap="Blues")
plt.title("Matrice di confusione - KNN")
plt.show()

#Visualizzazione della confusion matrix per DTC 
disp = ConfusionMatrixDisplay(confusion_matrix=cm_alb, display_labels=["Maligno", "Benigno"] )

disp.plot(cmap="Blues")
plt.title("Matrice di confusione - DTC")
plt.show()

###########################################################
#Punto 4 

# TP, TN, FP, FN del KNN
TP = 40
TN = 72 
FP = 0
FN = 2

#Calcolo di Precision e Recall 

print("Precision per il KNN:", TP/(TP + FP))
print("Recall per il KNN",     TP/(TP + FN))  

###########################################################
#Punto 5 
#Ho scelto KNN come modello finale perché presenta prestazioni superiori rispetto al Decision Tree, 
# soprattutto nella classificazione dei tumori maligni. 
# KNN individua 40 tumori maligni su 42, commettendo 2 falsi negativi,
# mentre il Decision Tree ne commette 3. 
# Questo aspetto è particolarmente importante dal punto di vista clinico, 
# poiché un falso negativo comporta la classificazione di un tumore maligno come benigno. 
# Inoltre, KNN presenta una recall del 95,24%, una precision del 100%.

###########################################################
#Punto 6
#Il modello KNN è quello selezionato e presenta un'accuratezza finale del 98,25% sul test set. 
#Particolarmente rilevante è la recall del 95,24% sulla classe maligna, 
#che indica la capacità di individuare 40 tumori maligni su 42. 
#La stima è attendibile perché ottenuta su un test set indipendente,
#mai utilizzato durante l'addestramento. 
#La precision è del 100%: nessun caso di tumore benigno è stato classificato come tumore maligno.


###Extra
#1. Aggiungi il modello `KNeighborsClassifier(weights="distance")` e confrontalo con quello standard.

#Creazione dell'istanza del modello
knn_2 = KNeighborsClassifier(weights="distance",n_neighbors=3).fit(X_train_f_s,y_train_f)

y_pred_knn_2 = knn_2.predict(X_test_s)

print("")
print("accuratezza del KNN-weights-distance:", accuracy_score(y_test,y_pred_knn_2))
print("precision del KNN-weights-distance:", precision_score(y_test,y_pred_knn_2, pos_label=0, zero_division=0))
print("recall  del KNN-weights-distance:", recall_score(y_test, y_pred_knn_2, pos_label=0, zero_division=0))

#L'utilizzo di weights="distance" non ha prodotto miglioramenti rispetto al KNN standard. 
# Le metriche ottenute sono identiche: entrambi i modelli presentano un'accuratezza del 98,25%
# e una recall del 95,24% sulla classe maligna. 

#2) Ripeti la scelta di k con 5 valori di `random_state` diversi nello split e 
# disegna le 5 curve di validation sullo stesso grafico: 
# quanto cambia il k "migliore"? 
# Cosa suggerisce sull'affidabilità di un singolo split? *(anticipazione della cross-validation)*

X,y = load_breast_cancer(return_X_y=True)

random_state = [ 0 , 10, 30, 42, 80 ]

acc_val_list = []
for i in random_state:
    
    X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=i,stratify=y)
    X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=i,stratify=y_temp)

    scaler = StandardScaler().fit(X_train)
    X_train_s = scaler.transform(X_train)
    X_val_s = scaler.transform(X_val)
    x_test_s = scaler.transform(X_test)

    valori_k = range(1,43,2)
    
    acc_validation = []

#Calcolo dell'accuratezza di training e validazione su valori diversi di k 
    for k in valori_k:
        knn = KNeighborsClassifier(n_neighbors=k).fit(X_train_s,y_train)
        acc_validation.append(knn.score(X_val_s,y_val))

    acc_val_list.append(acc_validation)


#Plotting validation curves 

for i in range(len(random_state)):
    plt.plot(valori_k, acc_val_list[i],
             label=f"Random state {random_state[i]}")

plt.xlabel("Valore di k")
plt.ylabel("Accuracy validation")
plt.title("Confronto KNN con 5 random state")
plt.legend()
plt.grid()
plt.xticks(valori_k)

plt.show()

#Il k migliore può cambiare molto , anche fino a 10.