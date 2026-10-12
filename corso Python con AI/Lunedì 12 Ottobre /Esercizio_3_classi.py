#Esercizio 3 

#Classe ContoCorrente con intestatario e saldo
class ContoCorrente():
    
    def __init__(self,intestatario,saldo):
        
        self.intestatario = intestatario 
        self.saldo = saldo
        
    def deposito(self,importo):
        if(importo > 0):
            self.saldo += importo
            print("Importo aggiunto correttamente al saldo")
        else:
            print("Errore, importo non valido!")
    
    def preleva(self,importo):
        
        if(importo > 0 and self.saldo >= importo):
            
            self.saldo -= importo
            print("Importo sottratto correttamente al saldo")
            
        elif(importo < 0 ):
            print("Errore, importo non valido!")
        else:
            print("Errore, saldo non sufficiente!")
            
    def stampa_saldo(self):
        
        print("Il saldo di ", self.intestatario, "è", self.saldo, "$")

            
                
Conto = ContoCorrente("Francesco", 100)

while(True):
    operazione= input("Inserisci operazione da eseguire: deposito,prelievo,stampa, esci: ")

    if(operazione.lower() == "deposito"):
        importo = int(input("Inserisci importo da aggiungere: "))
        Conto.deposito(importo)  
        
    if(operazione.lower() == "prelievo"):
        importo = int(input("Inserisci importo da prelevare: "))
        Conto.preleva(importo)

    if(operazione.lower() == "stampa"):
        Conto.stampa_saldo()
        
    if(operazione.lower() == "esci"):
        break       