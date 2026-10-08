#Esercizio completo
import random

    
#Creazione di una lista random a partire dal numero inserito in ingresso
def lista_random(n):
    
    lista_numeri = []
    
    for i in range(n):
        num = random.randint(1,n)
        lista_numeri.append(num)
        
    return lista_numeri

#Calcolo e somma dei numeri pari della lista

def somma_pari(lista):
    
    somma = 0
    
    for i in lista:
        
        if(i%2 == 0):
            somma +=i
    
    print("La somma dei numeri pari della lista è:",somma)
    
#Stampa numeri dispari della lista

def stampa_dispari(lista):
    print("Numeri dispari presenti nella lista: ")
    for i in lista:
        if(i%2 != 0):
            print(i)

#Ricerca numero primo 

def cerca_primo(lista):
    
    for i in lista:
        if i >= 2 and all(i % n != 0 for n in range(2, int(i**0.5) + 1)):
            return True
        
    return False

#Stampa numeri primi 

def stampa_primi(lista):
    print("Numeri primi presenti nella lista: ")
    for i in lista:
        if i >= 2 and all(i % n != 0 for n in range(2, int(i**0.5) + 1)):
            print(i)

#controllo se la somma di tutti gli elementi è un numero primo

def somma_totale(lista):
    
    somma = sum(lista)
    
    if somma >= 2 and all(somma % n != 0 for n in range(2, int(somma**0.5) + 1)):
        print("La somma di tutti i numeri della lista è  un numero primo")
    else:
        print("La somma di tutti i numeri della lista non è un numero primo")


#----------------------------------------------------------------------------
#Main  
    
n = int(input("Inserisci un numero intero positivo n: "))
while(n <= 0):
    n = int(input("Numero non valido, inserisci un intero positivo: "))    


lista_numeri = [] 

while(True):
    
    operazione = int(input("Scegli 1,2,3,4,5,6 o 7 per uscire: "))
    
    if(operazione == 1):
        lista_numeri = lista_random(n)
        print("Generata una lista di: ", len(lista_numeri), "elementi")
        print("La lista generata è: ", lista_numeri)
    
    if(operazione == 2):
        somma_pari(lista_numeri)
        
    if(operazione == 3):
        stampa_dispari(lista_numeri)
        
    if(operazione == 4):
        
        if(cerca_primo(lista_numeri) == True):
            print("Nella lista è presente un numero primo!")
        else:
            print("Nella lista non è presente un numero primo")
    
    if(operazione == 5):
        stampa_primi(lista_numeri)
        
    if(operazione == 6):
        somma_totale(lista_numeri)
        
    
    if(operazione ==7):
        break
    
