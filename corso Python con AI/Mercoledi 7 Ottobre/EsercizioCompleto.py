#esercizio completo con for,while,if

lista_totale = []

while(True):
    
    n = int(input("Inserisci un numero intero positivo n: "))
    
    while(n<=0):
        n = int(input("Numero non valido, inserisci un numero positivo: "))
    
    numeri_pari    = []
    numeri_dispari = []
    
    for i in range(n):
        if(i%2 == 0):
            numeri_pari.append(i)
    print("La somma dei numeri pari è: ", sum(numeri_pari))
    
    for i in range(n):
        if(i%2 != 0):
            numeri_dispari.append(i)
    print("I numeri dispari sono:", numeri_dispari)
        
    
    if n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
        print("Il numero da te è inserito è un numero primo!")
    else:
        print("Il numero da te inserito non è primo!")
    
    lista_totale.append(n)
    lista_totale.append(sum(numeri_pari))
    lista_totale.append(numeri_dispari)
    
    if n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
        lista_totale.append("Numero Primo")
    else:
        lista_totale.append("Numero non Primo")
        
    
    print("Risultati:")
    print(lista_totale)
              

    operazione = input("vuoi continuare? S o N: ")
    if(operazione.lower() == "n"):
        break