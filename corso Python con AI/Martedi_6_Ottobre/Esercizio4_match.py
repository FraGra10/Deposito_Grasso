eta = int(input("Inserisci la tua età: "))

if(eta >= 18):
    eta = "maggiorenne"
else:
    eta = "minorenne"

#Controllo dell'età 
match eta:
    case "maggiorenne":
        print("Puoi vedere questo film")
        
    case "minorenne":
        print("Mi dispiace, non puoi vedere questo film")
    
    case _:
        pass
    
#-----------------------------------------------------------------------------
numero_1 = int(input("Inserisci primo numero: "))
numero_2 = int(input("Inserisci secondo numero: "))

operazione = input("Inserisci l'operazione da eseguire tra +, - , *   e /: ")

#Rislutato dell'operazione matematica con attenzione alla divisione per zero
match operazione:
    case "+":
        print("Risultato dell'addizione: ", numero_1 + numero_2)
    case "-":
        print("Risultato della sottrazione: ", numero_1 - numero_2)
    case "*":
        print("Risultato della moltiplicazione: ", numero_1*numero_2)
    case "/":
        if(numero_2 == 0):
            print("Errore: Divisione per zero")
        else:
            print("Risultato della divisione: ", numero_1/numero_2)
    case _:
        print("Operazione non valida")