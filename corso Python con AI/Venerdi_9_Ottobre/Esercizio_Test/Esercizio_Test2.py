
#definizioni delle funzioni di somma e sottrazione 

def somma():
    primo_valore = int(input("Inserisci primo valore: "))
    secon_valore = int(input("Inserisci secondo valore: "))
    
    sum = primo_valore + secon_valore
    
    return sum

def sottrazione():
    primo_valore = int(input("Inserisci primo valore: "))
    secon_valore = int(input("Inserisci secondo valore: "))
    
    sottr = primo_valore - secon_valore
    
    return sottr   

while(True):
    
    #inserimento valori per il login
    nome =    input("Inserisci nome per accedere: ")
    codice =  int(input("Inserisci codice per accedere: ")) 

    #controllo dei valori
    if(len(nome) != 0 and codice != 0 ):
        
        login_nome = input("Inserisci il nome di login: ")
        login_cod  = int(input("Inserisci il codice di login: "))
        
        if(login_nome == nome and login_cod == codice):
        
            somma_valori = []
            sottrazione_valori = []
        
            while(True):
                
                operazione = int(input("Inserisci operazione da effettuare: 1 per somma, 2 per sottrazione, 3 per vedere risultati, 4 per uscire:  "))

                if(operazione == 1):
                    somma_valori.append(somma())
                if(operazione == 2):
                    sottrazione_valori.append(sottrazione())
                if(operazione == 3):
                    print("Risultati: ")
                    print("La somma è: ", somma_valori)
                    print("La sottrazione è : ", sottrazione_valori)
                if(operazione == 4):
                    break
                
                    
            
              
            

