#classe generica dell'elettrodomestico
class Elettrodomestico:
    
    def __init__(self,marca:str,modello:str,anno_acquisto:int,guasto:str):
        
        self.__marca = marca 
        self.__modello = modello
        self.__anno = anno_acquisto
        self.__guasto = guasto
    
    #metodi getter per le variabili protette
    def get_marca(self):
        return self.__marca
    def get_modello(self):
        return self.__modello
    def get_anno(self):
        return self.__anno
    def get_guasto(self):
        return self.__guasto
    
    #metodi setter per le variabili private    
    def set_marca(self, marca):

        if len(marca) <= 0 :
            print("Marca non valida!")
        else:
            self.__marca = marca
    def set_modello(self, modello):

        if len(modello) <= 0 :
            print("Modello non valido!")
        else:
            self.__modello = modello   
    def set_anno(self, anno):

        if anno > 2026 :
            print("Anno non valido!")
        else:
            self.__anno = anno
    def set_guasto(self, guasto):

        if len(guasto) <= 0 :
            print("Guasto non valida!")
        else:
            self.__guasto = guasto
            
    #descrizione       
    def descrizione(self):
        return "Elettrodomestico di marca: ", self.__marca," di modello: ", self.__modello, " acquistato nell'anno: ", self.__anno, ", con il guasto: ",self.__guasto
    
    #stima costo dovuto al guasto 
    def stima_costo_base(self):
        costo_base_diagnosi = 100
        
        return costo_base_diagnosi


##################################################################################
#Classe derivata Lavatrice con due nuovi attributi privati
class Lavatrice(Elettrodomestico):
    
    def __init__(self,marca,modello,anno_acquisto,guasto,capacita_kg:int,giri_centrifuga:int):
        super().__init__(marca,modello,anno_acquisto,guasto)
        self.__capacita_kg = capacita_kg
        self.__giri_centrifuga = giri_centrifuga

#Overriding del metodo stima_costo_base
    def stima_costo_base(self):
        
        if(self.__capacita_kg > 10):
            
            costo_base_diagnosi = 400
        else:
            costo_base_diagnosi = 200
        
        return costo_base_diagnosi

#Classe derivata Frigorifero con due nuovi attributi privati
class Frigorifero(Elettrodomestico):
    def __init__(self,marca,modello,anno_acquisto,guasto,litri:int,ha_freezer:bool):
        super().__init__(marca,modello,anno_acquisto,guasto)
        self.__litri = litri
        self.__ha_freezer = ha_freezer

#Overriding del metodo stima_costo_base
    def stima_costo_base(self):
        
        if(self.__ha_freezer):
            
            costo_base_diagnosi = 750
        
        else:
            costo_base_diagnosi = 400
        
        return costo_base_diagnosi

#Classe derivata Forno con due nuovi attributi privati
class Forno(Elettrodomestico):
    def __init__(self,marca,modello,anno_acquisto,guasto,tipo_alimentazione:str,ha_ventilato:bool):
        super().__init__(marca,modello,anno_acquisto,guasto)
        self.__tipo_alimentazione = tipo_alimentazione
        self.__ha_ventilato = ha_ventilato

#Overriding del metodo stima_costo_base        
    def stima_costo_base(self):
        
        if(self.__tipo_alimentazione == "elettrico" and self.__ha_ventilato):
            
            costo_base_diagnosi = 1000
        elif(self.__tipo_alimentazione == "elettrico" and not self.__ha_ventilato):
            costo_base_diagnosi = 700
        elif(self.__tipo_alimentazione == "gas" and  self.__ha_ventilato):
            costo_base_diagnosi = 500
        else:
            costo_base_diagnosi = 350           
        
        return costo_base_diagnosi
    

####################################################################################################
class TicketRiparazione:
    def __init__(self,id_ticket,elettrodomestico,stato):
        
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico
        self.__stato = stato
        self.__note = []

    def get_stato(self):
        return self.__stato
    def get_note(self):
        return self.__note
    
    def get_id_ticket(self):
        return self.__id_ticket
    
    def get_elettrodomestico(self):
        return self.__elettrodomestico

    
    #metodi setter per le variabili private    
    def set_stato(self, stato):

        if len(stato) <= 0 :
            print("Stato non valida!")
        else:
            self.__stato = stato
            
    def set_note(self, note):

        if len(note) <= 0 :
            print("Note non valide!")
        else:
            self.__note = note
    
    def aggiungi_nota(self,testo):
        
        if(len(testo) > 0):
            self.__note.append(testo)
        else:
            print("nota non valida!")
            
    def calcola_preventivo(self,*voci_extra):
        
        costo_base = self.__elettrodomestico.stima_costo_base()
        
        totale = 0 
        for voce in voci_extra:
            totale  += voce
        
        costo_totale = costo_base + totale
        
        return costo_totale 
            
####################################################################################################
            
class Officina:
    
    def __init__(self):
        
        self.nome = "" 
        self.tickets = []
    
    def aggiungi_ticket(self,ticket):
        
        self.tickets.append(ticket)
    
    def chiudi_ticket(self,id_ticket):
        
        for i in self.tickets:
            
            if(i.get_id_ticket() == id_ticket):
                self.tickets.remove(i)
                return

        print("ID non trovato")
            
    def stampa_ticket_aperti(self):
        for i in self.tickets:
            print("ID:", i.get_id_ticket(), "Tipo:" ,type(i.get_elettrodomestico()).__name__, "Stato: ", i.get_stato() )
    
    def totale_preventivi(self):
        somma = 0
        for i in self.tickets:
            somma +=i.calcola_preventivo()
            
        print("La somma dei preventivi è: ", somma)
        
    def statistiche_per_tipo(self):
        
        num_forno =  0 
        num_lavatrice = 0
        num_frigorifero = 0 
        
        for i in self.tickets: 
            if(type(i.get_elettrodomestico()).__name__ == "Forno"):
                num_forno += 1
            elif(type(i.get_elettrodomestico()).__name__ == "Lavatrice"):
                
                num_lavatrice +=1 
                
            elif(type(i.get_elettrodomestico()).__name__ == "Frigorifero"):
                
                num_frigorifero +=1 
                
        print("Numero di lavatrici in riparazione: ", num_lavatrice)
        print("Numero frigoriferi in  riparazione: ", num_frigorifero)
        print("Numero forni in riparazione: ", num_forno)
        
######################################################################################

#Main

prova_1 = Frigorifero("Sony","DES",2000,"refrigerante",30,True)
prova_2 = Forno("DSDS","FDR",2010,"centralina","elettrico",True)
prova_3 = Lavatrice("Ericson","sss",2000,"centralina",10,300)

Ticket = TicketRiparazione(10,prova_3,"Aperto")
Ticket_1 = TicketRiparazione(10,prova_1,"Chiuso")
Ticket_2 = TicketRiparazione(10,prova_2,"In Lavorazione")

Officina_1 = Officina()
Officina_1.aggiungi_ticket(Ticket)
Officina_1.aggiungi_ticket(Ticket_2)
Officina_1.aggiungi_ticket(Ticket_1)
Officina_1.aggiungi_ticket(Ticket_2)

Officina_1.statistiche_per_tipo()
Officina_1.stampa_ticket_aperti()