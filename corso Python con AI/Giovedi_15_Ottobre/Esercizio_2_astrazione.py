from abc import ABC, abstractmethod

#Implementazione classa astratta 
class VeicoloTrasporto(ABC):
    
    def __init__(self,targa,peso_massimo,carico_attuale):
        
        self.__targa = targa
        self.__peso_massimo = peso_massimo
        self.__carico_attuale = carico_attuale
    
    def carica(self,peso):
        
        if(self.__carico_attuale + peso > self.__peso_massimo):
            print("Attenzione, capacità superata!")
        else:
            self.__carico_attuale += peso
            print("Peso aggiunto correttamente al carico attuale!")
    
    def scarica(self):
        self.__carico_attuale = 0
        print("Carico attuale portato correttamente a 0!")
    
    @abstractmethod
    def costo_manutenzione(self):
        pass 
    
    #Getter degli attributi comuni
    def get_targa(self):
        return self.__targa
    def get_peso(self):
        return self.__peso_massimo
    def get_carico(self):
        return self.__carico_attuale
    
    #Setter degli attributi comuni        
    def set_targa(self, targa):

        if len(targa) == 0 :
            print("Targa non valida!")
        else:
            self.__targa = targa
    
    def set_carico(self, carico_attuale):

        if carico_attuale < 0 :
            print("Carico non valido!")
        else:
            self.__carico_attuale = carico_attuale
    
    def set_peso(self, peso_massimo):

        if peso_massimo < 0 :
            print("Peso massimo non valido!")
        else:
            self.__peso_massimo = peso_massimo
##############################################################################

class Camion(VeicoloTrasporto):
    
    def __init__(self,targa,peso_massimo,carico_attuale,numero_assi):
        
        super().__init__(targa,peso_massimo,carico_attuale)
        
        self.__numero_assi = numero_assi
        
    def costo_manutenzione(self):
        
        costo_manutenzione = self.__numero_assi*100 + self.get_peso()
        
        return costo_manutenzione
        
    


class Furgone(VeicoloTrasporto):
 
    def __init__(self,targa,peso_massimo,carico_attuale,alimentazione):
        super().__init__(targa,peso_massimo,carico_attuale)
        self.__alimentazione = alimentazione
        
    def costo_manutenzione(self):
        
        if(self.__alimentazione == "diesel"):
            costo_manutenzione =  150
        elif(self.__alimentazione == "elettrico"):
            costo_manutenzione = 200
        
        return costo_manutenzione

class Motocarro(VeicoloTrasporto):
    
    def __init__(self,targa,peso_massimo,carico_attuale,anni_servizio):
        super().__init__(targa,peso_massimo,carico_attuale)  
        self.__anni_servizio = anni_servizio   
    
    def costo_manutenzione(self):
        
        costo_manutenzione = 50*self.__anni_servizio
        
        return costo_manutenzione
###############################################################

class GestoreFlotta():
    
    def __init__(self):
        self.veicoli = []
        
    def aggiungi_veicolo(self):
        
        tipo = input("Inserisci il tipo di veicolo da aggiungere: camion, furgone, o motocarro: ")
        
        if(tipo.lower() == "camion"):
            targa = input("Inserisci numero di targa: ")
            peso  = int(input("Inserisci peso massimo:"))
            carico = int(input("Inserisci carico attuale: "))
            assi   = int(input("Inserisci numero di assi: "))
            
            self.veicoli.append(Camion(targa,peso,carico,assi))
            
        elif(tipo.lower() == "furgone"):
            targa = input("Inserisci numero di targa: ")
            peso  = int(input("Inserisci peso massimo:"))
            carico = int(input("Inserisci carico attuale: "))
            alimentazione   =input("Inserisci tipo di alimentazione: ")
            
            self.veicoli.append(Furgone(targa,peso,carico,alimentazione))
    
        elif(tipo.lower() == "motocarro"):
            targa = input("Inserisci numero di targa: ")
            peso  = int(input("Inserisci peso massimo:"))
            carico = int(input("Inserisci carico attuale: "))
            anni   = int(input("Inserisci numero di anni di servizio: "))     

            self.veicoli.append(Motocarro(targa,peso,carico,anni))

    def rimuovi_veicolo(self,targa):
        flag = False
        for i in self.veicoli:
            if(i.get_targa() == targa):
                self.veicoli.remove(i)
                flag=True
                break
        
        if(not flag):
            print("Veicolo non trovato!")
            
    def costo_totale_manutenzione(self):
        somma = 0 
        for i in self.veicoli:
            somma += i.costo_manutenzione()
        
        print("Costo totale di manutenzione pari a : ", somma)
    
    def stampa_veicoli(self):
        if(len(self.veicoli)== 0):
            print("Nessun veicolo registrato!")
        else:
            for i in self.veicoli:
                print("Targa: ", i.get_targa())
                print("Tipo: " ,type(i).__name__) 
                print("Carico attuale: " , i.get_carico())
                
###############################################################################

Gestore = GestoreFlotta()
    
while(True):
    
    print("Inserisci 1 per aggiungere un veicolo: ")
    print("Inserisci 2 per rimuovere un veicolo:  ")
    print("Insersci  3 per visualizzare il costo totale di manutenzione: ")
    print("Inserisci 4 per stampare i veicoli registrati: ")
    print("Inserisci 5 per uscire: ")
    
    operazione = int(input(" "))
    
    if(operazione == 1):
        Gestore.aggiungi_veicolo()
    if(operazione == 2):
        
        targa = input("Digita la targa del veicolo da rimuovere: ")
        Gestore.rimuovi_veicolo(targa)
        
    if(operazione == 3):
        Gestore.costo_totale_manutenzione()
    if(operazione == 4):
        Gestore.stampa_veicoli()
    if(operazione == 5): 
        break      
                
            

