#Esercizio 3 

#Classe ContoCorrente con intestatario e saldo
class ContoCorrente():
    
    def __init__(self,intestatario,saldo):
        
        self.intestatario = intestatario 
        self.saldo = saldo
    
    #Metodo per depositare sul saldo 
        
    def deposito(self,importo):
        if(importo > 0):
            self.saldo += importo
            print("Importo aggiunto correttamente al saldo")
        else:
            print("Errore, importo non valido!")
    
    #Metodo per prelevare dal saldo
    def preleva(self,importo):
        
        if(importo > 0 and self.saldo >= importo):
            
            self.saldo -= importo
            print("Importo sottratto correttamente al saldo")
            
        elif(importo < 0 ):
            print("Errore, importo non valido!")
        else:
            print("Errore, saldo non sufficiente!")
    
    #Metodo per stampare il saldo         
    def stampa_saldo(self):
        
        print("Il saldo di ", self.intestatario, "è", self.saldo, "$")

            
                
Conto = ContoCorrente("Francesco", 100)

#Ciclo con le varie operazioni da compiere
while(True):
    operazione= input("Inserisci operazione da eseguire: deposito,prelievo,stampa, esci: ")

#operazione di deposito 
    if(operazione.lower() == "deposito"):
        importo = int(input("Inserisci importo da aggiungere: "))
        Conto.deposito(importo)  

#operazione di prelievo
    if(operazione.lower() == "prelievo"):
        importo = int(input("Inserisci importo da prelevare: "))
        Conto.preleva(importo)

#operazione di stampa
    if(operazione.lower() == "stampa"):
        Conto.stampa_saldo()
        
    if(operazione.lower() == "esci"):
        break       