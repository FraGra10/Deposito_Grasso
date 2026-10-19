
#Funziona crea file
def crea_file():
    
    nome_file = input("Inserisci nome del file da creare: ")
        
    with open(nome_file,"w") as file:
        pass
 
#Funzione modifica file   
def modifica_file():
    
    nome_file = input("Inserisci nome file da modificare: ")
    
    with open(nome_file,"a") as file:
        
        text = input("Inserisci elementi da aggiungere alla fine del file: ")
        file.write("\n")
        file.write(text)

#Funzione leggi file       
def leggi_file():
    
    nome_file = input("Inserisci nome file da leggere: ")
    
    with open(nome_file,"r") as file:
        
        contenuto = file.read()
        print(contenuto)

#Funzione svuota file
def svuota_file():

    nome_file = input("Inserisci nome file da svuotare: ")
    
    with open(nome_file,"w") as file:
        pass


#while con match
while True:
    
    operazione = input("Inserisci operazione da compiere: crea,modifica,leggi,svuota,esci: ")

#match con vari case    
    match operazione:
        
        case "crea":
            crea_file()
            
        case "leggi": 
            leggi_file() 
                     
        case "svuota":
            svuota_file()
            
        case "modifica":
            modifica_file()
                    
        case "esci":
            break
            