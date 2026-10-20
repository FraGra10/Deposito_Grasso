import numpy as np 

def functions():
    
#Esercizio1
    array_1 = np.random.randint(1,101,15)

    print("La somma di tutti gli elementi dell'array è: ", np.sum(array_1))
    print("La media di tutti gli elementi dell'array è: ", np.mean(array_1))

#Esercizio2
    matrix = np.array([np.arange(1,6), np.arange(6,11), np.arange(11,16),np.arange(16,21),np.arange(21,26)])

    print("La matrice presa in considerazione è: \n", matrix)
    print("La seconda colonna della matrice è: ", matrix[:,1])
    print("La terza riga della matrice è : ", matrix[2,:])

    pri_diag = np.diag(matrix)
    print("La somma degli elementi della diagonale principale della matrice è : ", np.sum(pri_diag))


#Esercizio3
    matrix1 = np.random.randint(10,50, size = (4,4))

#Utilizzo di fancy indexing per stampare indici (0,1)  (1,3)  (2,2) (3,0)

    print("La matrice generata è: \n", matrix1)

    print("Gli elementi stampati agli indici: (0,1),(1,3),(2,2),(3,0) sono: ")
    print(matrix1[[0,1,2,3],[1,3,2,0]])

    print("Le righe dispari sono: ")
    print(matrix1[[1,3]])

    print("La matrice iniziale modificata aggiungendo 10 al loro valore è : ")
    print(matrix1 + 10 )


#while(True):
    
    #operazione = input("Scegli se procedere con gli esercizi oppure uscire: S o N: ")
    
    #if(operazione.lower() == "s"):
        