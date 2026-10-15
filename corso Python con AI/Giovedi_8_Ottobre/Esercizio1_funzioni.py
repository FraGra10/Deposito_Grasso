#----------------------------------------------------------------------------
import random 

#Funzione dell'esercizio 1, indovina_numero  
def Indovina_numero():
    
    flag = True
    numero_ind =random.randint(1, 100)

    while(True):
        
        numero = int(input("Inserisci il numero: "))
        
        if(numero > numero_ind):
            print("Numero da indovinare più basso")
            flag = False
        elif(numero < numero_ind):
            print("Numero da indovinare più alto")
            flag = False
        else:
            print("Numero indovinato!")
            flag = True
    
        if(not flag):
            operazione = input("Vuoi riprovare? S o N ")
    
        if(operazione.lower() == "n" or flag == True):
            break
        

#----------------------------------------------------------------------------
#Funzione dell'esercizio 2 , sequenza di fibonacci
def Print_Fibonacci(N):
    
    a = 0
    b = 1
    while a <= N:
        print(a)
        a = b
        b = a+b
        
#----------------------------------------------------------------------------


#MAIN

while True:
    operazione = input("Vuoi fare il primo esercizio o il secondo?, metti uno, due o esc: ")
    
    if(operazione == "uno"):
        Indovina_numero()
    elif(operazione == "due"):
        N = int(input("Inserisci un numero N: "))
        Print_Fibonacci(N)
    else:
        break
