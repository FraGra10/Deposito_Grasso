#Utilizzo di if 
'''numero = int(input("Inserisci un numero:" ))

if(numero%2 == 0):
    print("Il numero è pari ")
else:
    print("Il numero è dispari")

#------------------------------------------------------------------------------
#Utilizzo di while e range

flag = True
while(flag):
    n = int(input("Inserisci numero intero positivo: "))

    for i in range(0,n+1,1):
        print(i)

    operazione = input("Vuoi ripetere? s o n: ")
    
    if(operazione == "n"):
        flag=False 
#------------------------------------------------------------------------------
#Utilizzo di for 

numero = int(input("inserisci numero elementi della lista: "))
lista_numeri = []

for i in range(numero):
    numero = int(input("inserisci elemento della lista: "))
    lista_numeri.append(numero)

for i in range(len(lista_numeri)):
    print(lista_numeri[i]**2) '''
#------------------------------------------------------------------------------
#Utilizzo di if,while,for insieme
numero = int(input("inserisci numero elementi della lista: "))
lista_numeri = []

for i in range(numero):
    numero = int(input("inserisci elemento della lista: "))
    lista_numeri.append(numero)

if(len(lista_numeri) > 0) :
    max_num = lista_numeri[0]

    for i in range(len(lista_numeri)):
        if(lista_numeri[i] > max_num):
            max_num = lista_numeri[i]

    cond = True
    cont = 0
    while(cond):
    
        cont += 1 
        if(cont == len(lista_numeri)):
            cond = False
    

if(len(lista_numeri) == 0):
    print("Lista Vuota!")
else:
    print("Numero massimo trovato: ", max_num, "Numero elementi: ", cont)