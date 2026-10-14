#Classe Madre 
class MetodoPagamento:
    
    def effettua_pagamento(self):
        importo = int(input("Inserisci importo per il pagamento: "))
        print("effettuato pagamento di importo:  ", importo)

#Classi figlie con sovrascrittura del metodo effettua_pagamento

class CartaDiCredito(MetodoPagamento):
    
        def effettua_pagamento(self):
            print("*** VISA ***")
            importo = int(input("Inserisci importo per il pagamento con Carta di Credito: "))
            print("effettuato pagamento di importo:  ", importo, "con Carta di Credito")    
   
class PayPal(MetodoPagamento):
    
        def effettua_pagamento(self):
            print("***PAYPAL***")
            importo = int(input("Inserisci importo per il pagamento con Paypal: "))
            print("effettuato pagamento di importo:  ", importo, "con PayPal") 

class BonificoBancario(MetodoPagamento):
    
        def effettua_pagamento(self):
            print("***BONIFICO BANCARIO***")
            importo = int(input("Inserisci importo per il pagamento con Bonifico Bancario: "))
            print("effettuato pagamento di importo:  ", importo, "con Bonifico Bancario")     

#Classe Gestore Pagamenti

class GestorePagamenti:
    
    def __init__ (self, classe):
        
        classe.effettua_pagamento()        

      
#Istanze delle classi precedenti
Pagamento_1 = PayPal()
Pagamento_2 = BonificoBancario()
Pagamento_3 = CartaDiCredito()

Gestore = GestorePagamenti(Pagamento_1)
Gestore = GestorePagamenti(Pagamento_2)
Gestore = GestorePagamenti(Pagamento_3)
