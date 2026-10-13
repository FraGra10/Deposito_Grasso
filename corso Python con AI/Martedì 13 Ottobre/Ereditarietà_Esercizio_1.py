# Definizione classe generica
class Animale:
    def __init__(self,nome,eta):
        self.nome = nome 
        self.eta  = eta
        
    def fai_suono(self):
        print(f"{self.nome} fa un suono generico.")

#Definizione della classe Leone derivata

class Leone(Animale):
    
    def __init__(self,nome,eta,caccia):
        super().__init__(nome,eta)
        self.caccia = caccia
    
    def fai_suono(self):
        print(f" {self.nome} ruggisce! ")

    def tipo_di_caccia(self):
        print(f"Il modo in cui caccia {self.nome} è {self.caccia}!")

#Definizione classe Pinguino derivata
class Pinguino(Animale):

#Costruttore della classe derivata
    def __init__(self,nome,eta,colore):
        super().__init__(nome,eta)
        self.colore = colore
    
    def fai_suono(self):
        print(f" {self.nome} stride! ")

#Nuovo metodo della classe derivata
    def colore_della_pelle(self):
        print(f"Il colore di  {self.nome} è {self.colore}!")    
        
#Definizione Classe Gatto derivata
class Gatto(Animale):
    
    def __init__(self,nome,eta,colore):
        super().__init__(nome,eta)
        self.colore = colore
    
    def fai_suono(self):
        print(f" {self.nome} miagola! ")

    def colore_della_pelle(self):
        print(f"Il colore di  {self.nome} è {self.colore}!")      


#---------------------------------------------------------------------------------------------------
Leone_1 = Leone("Simba",2,"da solo")
Leone_1.fai_suono()
Leone_1.tipo_di_caccia()

Pinguino_1 = Pinguino("Pingu",2,"Bianco e Nero")
Pinguino_1.colore_della_pelle()

Gatto_1 = Gatto("Golden",1,"Oro")
Gatto_1.colore_della_pelle()
        
#--------------------------------------------------------------------------------------------

