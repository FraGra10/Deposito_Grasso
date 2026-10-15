#Creazione variabili 
nome  = input("Inserisci il nome :")
eta   = int(input("Inserisci l'età :"))
sesso = input("Inserisci il sesso :")
premium = input("Inserisci valore booleano :").lower() == "true"

lista = [nome,eta,sesso,premium]
lista_2 = []

posizione = input("quale posizione vuoi modificare? 0 , 1 ,2 3; 4 per creare una nuova lista, 5 per rimuovere un elemento: ")

match posizione:
    case "0":
        nome = input("Inserisci nuovo nome:")
        if(len(nome) == 0 or type(nome) != str):
            print("operazione non consentita")
        else:
            lista[0] = nome
    case "1":
        eta = int(input("Inserisci la nuova età:"))
        if(type(eta) != int):
            print("operazione non consentita")
        else:
            lista[1] = eta
    case "2":
        sesso = input("Inserisci nuovo sesso:")
        if(len(sesso) > 1):
            print("elemento non valido")
        else:
            lista[2] = sesso
    case "3":
        premium = input("Inserisci nuovo valore booleano:").lower() == "true"
        lista[3] = premium
    case "4":
        lista_2.append(input("Inserisci nuovo nome: "))
        lista_2.append(int(input("Inserisci nuova età:")))
        lista_2.append(input("Inserisci nuovo sesso:"))
        lista_2.append(bool(input("Inserisci nuovo valore booleano:")))
    case "5":
        posizione = int(input("inserisci la posizione dell'elemento da eliminare:"))
        lista.pop(posizione)    
    case _:
        print("posizione non disponibile!")

        
print(lista)
print(lista_2)