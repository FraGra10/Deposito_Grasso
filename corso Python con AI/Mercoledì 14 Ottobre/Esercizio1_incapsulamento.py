class ContoBancario:
    
    __titolare = ""
    __saldo  = 0
    
    def __init__(self, titolare,saldo):
        
        self.__titolare = titolare
        self.__saldo    = saldo
    
    
    #getter
    def get_titolare(self):
        return self.__titolare
    
    def get_saldo(self):
        return self.__saldo
        
    #setter
        
    def set_titolare(self, nome):

        if len(nome) < 0 :
            print("Nome errato!")
        else:
            self.__titolare = nome
        
    def set_saldo(self, importo):

        if   importo < 0 :
            print("Errore! saldo negativo!")
        else:
            self.__saldo = importo
    
    #metodo per depositare sul conto 
    def deposita(self,importo):
        
        if(importo >= 0):
            
            __saldo += importo
    
    #metodo per prelevare dal conto 
    def preleva(self,importo):
            
            if(importo >= 0 and __saldo >= importo ):
                
                __saldo -= importo
    
    #metodo per visualizzare il saldo
    def visualizza_saldo(self):
        print(f"Il saldo è {self.__saldo}")
                
            

            
            
            
# Primo conto Bancario
    
Conto_1 = ContoBancario("Mario_Rossi",300)

print(Conto_1)