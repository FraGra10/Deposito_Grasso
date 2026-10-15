#classe madre 
class Prodotto:
    
    def __init__(self,nome,quantità):
        
        self.__nome     = nome
        self.__quantità = quantità
    
    #Metodo di lavorazione     
    def metodo_di_lavorazione(self):
    
        print(f"Il prodotto {self.__nome} è stato realizzato con macchinari.")
    
    #Getter e Setter
    def get_nome(self):
        return self.__nome
    
    def get_quantità(self):
        return self.__quantità
        
    def set_nome(self, nome_nuovo):

        if len(nome_nuovo) < 0 :
            print("Nome inserito non valido!")
        else:
            self.__nome = nome_nuovo

    def set_quantità(self, quantità):

        if quantità < 0 :
            print("Quantità non valida!")
        else:
            self.__quantità = quantità

##Classe derivata  Tubo 

class Tubo(Prodotto):
    
    def __init__(self,nome,quantità,diametro):
        
        super().__init__(nome,quantità)
        self.__diametro = diametro
    
    def metodo_di_lavorazione(self):
    
        print(f"Il prodotto {self.get_nome()} è stato realizzato tramite saldatura o  con dei rulli di formatura.")

    #Getter e setter della classe figlia 
    def get_diametro(self):
        return self.__diametro
        
    def set_diametro(self, diametro_nuovo):

        if diametro_nuovo < 0 :
            print("Diametro inserito non valido!")
        else:
            self.__diametro = diametro_nuovo

#Classe derivata bullone 

class Bullone(Prodotto):
    
    def __init__(self,nome,quantità,filettatura):
        
        super().__init__(nome,quantità)
        self.__filettatura = filettatura
    
    def metodo_di_lavorazione(self):
    
        print(f"Il prodotto {self.get_nome()} è stato realizzato tramite una pressa.")

    #Getter e setter della classe figlia 
    def get_filettatura(self):
        return self.__filettatura
        
    def set_filettatura(self, filettatura_nuova):

        if len(filettatura_nuova) < 0 :
            print("Filettatura inserito non valido!")
        else:
            self.__filettatura = filettatura_nuova

### Gestione dei prodotti 


class GestioneFabbrica: 
    
    def __init__(self):
        
        self.prodotti_totali = []
        
    def Aggiungi_Prodotto(self,Tubo_obj,Bullone_obj):
        elemento = input("Scegli quale elemento aggiungere: bullone o tubo")
        if(elemento == "tubo"):
            elem_1 = input("Inserisci nome: ")
            elem_2 = int(input("Inserisci quantità del prodotto: "))
            elem_3 = int(input("Inserisci diametro del tubo: "))
            Tubo_obj.set_nome(elem_1)
            Tubo_obj.set_quantità(elem_2)
            Tubo_obj.set_diametro(elem_3)
            self.prodotti_totali.append(Tubo_obj)
        if(elemento == "bullone"):
            elem_1 = input("Inserisci nome: ")
            elem_2 = int(input("Inserisci quantità del prodotto: "))
            elem_3 = input("Inserisci filettatura del bullone: ")
            Bullone_obj.set_nome(elem_1)
            Bullone_obj.set_quantità(elem_2)
            Bullone_obj.set_filettatura(elem_3)
            self.prodotti_totali.append(Bullone_obj)
    
    def Visualizza_produzione(self):
        
        print("Elementi prodotti: ")
        for i in self.prodotti_totali:
            print(i.get_nome())
            
    def Cerca_Prodotto(self):
        
        nome_cercato = input("Inserisci il nome da cercare: ")
        flag = False
        for i in self.prodotti_totali:
            if(i.get_nome() == nome_cercato):
                "Prodotto Trovato!"
                flag = True
        if(flag == False):
            print("Prodotto non trovato!")
    
    def Modifica_Quantità(self):
        nome = input("Inserisci il nome dell'oggetto: ")
        quantità = int(input("Inserisci nuova quantità da impostare: "))
        for i in self.prodotti_totali:
            if(i.get_nome() == nome):
                i.set_quantità(quantità)
    
    def Rimuovi_Prodotto(self):
        
        nome_cercato = input("Inserisci il nome da rimuovere: ")
        flag = -1
        for i in range(len(self.prodotti_totali)):
            if(self.prodotti_totali[i].get_nome() == nome_cercato):
                print("Prodotto Trovato!")
                flag = i
        
        if(flag >= 0):
            self.prodotti_totali.pop(flag)
        else:
            print("Prodotto non trovato!")
    
    def Totale_pezzi_prodotti(self):
        sum = 0
        for i in self.prodotti_totali:
            qt = i.get_quantità()
            sum += qt
        print("La somma totale dei pezzi prodotti è: ", sum)
        
                
################################################################################################À
Tubo_1   = Tubo("",0,"")
Bullone_1 =Bullone("",0,"")
Gestione_fabbrica_1 = GestioneFabbrica()

#Menu di scelta 
while(True):

    operazione = int(input(" Scegli 1 per aggiungere un prodotto \n Scegli 2 per visualizzare la produzione \n Scegli 3 per cercare un prodotto \n Scegli 4 per modificarne la quantità \n Scegli 5 per  rimuovere un prodotto \n Scegli 6 per calcolare totale pezzi prodotti \n Scegli 7 per uscire dal menu: "))
    
    if(operazione == 1):
        Gestione_fabbrica_1.Aggiungi_Prodotto(Tubo_1,Bullone_1)
    if(operazione == 2):
        Gestione_fabbrica_1.Visualizza_produzione()
    if(operazione == 3):
        Gestione_fabbrica_1.Cerca_Prodotto()
    if(operazione == 4):
        Gestione_fabbrica_1.Modifica_Quantità()
    if(operazione == 5):
        Gestione_fabbrica_1.Rimuovi_Prodotto()
    if(operazione == 6):
        Gestione_fabbrica_1.Totale_pezzi_prodotti()
    if(operazione == 7):
        break
