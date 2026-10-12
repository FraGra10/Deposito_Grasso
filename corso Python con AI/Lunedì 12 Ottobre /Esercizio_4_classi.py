#Esercizio 4 

class Garage:
    
    def __init__(self,capienza):
        
        self.capienza = capienza
        self.auto_presenti = []
    
    #Metodo per la funzione di parcheggio
    def parcheggia(self, targa):
        if(targa in self.auto_presenti):
            print("Auto già in garage!")
        elif(len(self.auto_presenti) == self.capienza):
            print("Errore! Garage pieno!")
        elif(not self.formato_targa_valido(targa)):
            print("Errore! Formato targa non valido!")
        else:
            self.auto_presenti.append(targa)
    
    #Metodo per rimuovere l'auto dal garage
    def rimuovi(self,numero_targa):
            if(numero_targa in self.auto_presenti):
                self.auto_presenti.remove(numero_targa)
            else:
                print("Errore! Auto non presente!")
            
    
    #Metodo per restituire i posti liberi 
    def posti_liberi(self):
        return self.capienza - len(self.auto_presenti)
    
    #Metodo statico per valutare se la targa ha il formato giusto
    @staticmethod
    def formato_targa_valido(targa):
        
        if(len(targa) != 7):
            return False
        
        part_one = targa[0:2]
        part_two = targa[2:5]
        part_thr = targa[5:7]
        
        if(part_one.isalpha() and part_two.isdigit() and part_thr.isalpha()):
            return True 
        else:
            return False
                    
        
    


Garage_1 = Garage(5)

while(True):
    operazione= input("Inserisci operazione da eseguire: parcheggia,rimuovi,posti, esci: ")
    
    #aggiunge una targa 
    if(operazione.lower() == "parcheggia"):
        targa = input("Inserisci targa dell'auto da parcheggiare: ")
        Garage_1.parcheggia(targa)  
    
    #rimuove una targa  
    if(operazione.lower() == "rimuovi"):
        targa = input("Inserisci targa dell'auto da eliminare: ")
        Garage_1.rimuovi(targa)

    #visualizza posti liberi in garage
    if(operazione.lower() == "posti"):
        print(Garage_1.posti_liberi())
        
    if(operazione.lower() == "esci"):
        break 
    
        
        