import numpy as np


#Esercizio 1 

#Creazione matrice casuale con numero righe e colonne date dall'utente

righe   = int(input("Inserisci numero righe della matrice: "))
colonne = int(input("Inserisci numero colonne della matrice: "))

matrix = np.random.randint(0,200,size = (righe,colonne))

with open("esercizio_4.txt","w") as file:
    file.write("La matrice casuale con righe e colonne generate dall'utente è: \n")
    file.write( str(matrix) + "\n" + "\n")

#Menu con varie operazioni disponibili 
while(True):

    operazione = int(input("Scegli 1 per estrarre la sotto-matrice centrale, 2 per la trasposta, 3 per la somma degli elementi, 4 per aggiungere una matrice, 5 per la media, 6 per il determinante della matrice, 7  per uscire: "))


    if(operazione == 1):

        #Estrazione e stampa della sotto-matrice centrale 

        sotto_matrice = matrix[1:righe-1,1:colonne-1]
        print("La sotto matrice centrale è: ",sotto_matrice)

        with open("esercizio_4.txt","a") as file:
            file.write("La sotto matrice centrale è: \n")
            file.write(str(sotto_matrice) + "\n"+ "\n")

#-----------------------------------------------------------------------
    
    elif(operazione == 2):
        #Trasposizione e stampa della matrice 

        matrix_trasposta = np.transpose(matrix)

        print("La matrice trasposta è : \n", matrix_trasposta)

        with open("esercizio_4.txt","a") as file:
            file.write("La matrice trasposta è: \n")
            file.write(str(matrix_trasposta) + "\n"+ "\n")

#-----------------------------------------------------------------------
   
    elif(operazione == 3):
        
        #Calcolo e stampa  della somma di tutti gli elementi della matrice 

        somma_elementi = np.sum(matrix)
        print("La somma di tutti gli elementi della matrice è: ", somma_elementi)

        with open("esercizio_4.txt","a") as file:
            file.write("La somma di tutti gli elementi della matrice è: \n")
            file.write(str(somma_elementi) + "\n"+ "\n")

#-----------------------------------------------------------------------
    
    elif(operazione == 4):
        #Calcolo della moltiplicazione della matrice originaria con un'altra matrice 
        matrix2 =  np.random.randint(0,200,size = (righe,colonne))
        
        matrice_molt = matrix*matrix2
        
        print("La moltiplicazione delle due matrici da come risultato: ", matrice_molt)

        with open("esercizio_4.txt","a") as file:
            file.write("La matrice moltiplicata con righe e colonne generate dall'utente è: \n")
            file.write(str(matrice_molt) + "\n"+ "\n")

#-----------------------------------------------------------------------
    
    elif(operazione == 5):
        #Calcolo media elementi della matrice 
        media = np.mean(matrix) 
        print("La media degli elementi della matrice è: ", media)
    
        with open("esercizio_4.txt","a") as file:
            file.write("La media degli elementi della matrice è: \n")
            file.write(str(media) + "\n"+ "\n")

#-----------------------------------------------------------------------
    
    elif(operazione == 6):
        #Calcolo determinante della matrice 
        #Controllo se la matrice è quadrata
        if(righe == colonne):
            determinante = np.linalg.det(matrix)
            print("Il determinante della matrice è: ", determinante)

            with open("esercizio_4.txt","a") as file:
                file.write("Il determinante della matrice è : \n")
                file.write(str(determinante) + "\n"+ "\n")
            
        else:
            print("Impossibile procedere con l'operazione, matrice non quadrata!")

#-----------------------------------------------------------------------
        
    else:
        break
    
#Parte3