#primo esercizio

flag = True

while(flag):
    
    numero = int(input("Inserisci un numero: "))

    for i in range(numero,-1,-1):
        print (i)
    
    operazione= input("scrivi 'ripetere' o 'uscire'")
    
    if(operazione.lower() == "uscire"):   
        flag = False
        
#----------------------------------------------------------------
#secondo esercizio
'''
flag = True
lista_pari    =   []
lista_dispari =   []

while(flag):
    
    numero = int(input("Inserisci un numero: "))
    
    if(numero%2 == 0):
        lista_pari.append(numero)
        print("Il numero è pari")
    else:
        lista_dispari.append(numero)
        print("Il numero è dispari")
        
    if(len(lista_pari) == 5 ):
        flag = False
        print("Lista pari:", lista_pari)
        print("Lista dispari:", lista_dispari) '''
        
#----------------------------------------------------------------
# terzo esercizio 

flag = True
lista_primi    =   []

while(flag):
    
    n = int(input("Inserisci un numero: "))
    
    if n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
        lista_primi.append(n)
        print("Il numero è primo")
    else:
        print("Il numero non è primo")
        
    if(len(lista_primi) == 5 ):
        flag = False
        print("Lista numeri primi:", lista_primi)
  
  #----------------------------------------------------------------
