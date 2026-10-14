import modulo_operazioni as m 


while(True):
  
    # 1 = somma; 2 = sottrazione; 
    # 3 = moltiplicazione; 4 = divisione
    # 5 = exit
    
    operazione = int(input("Inserisci operazione da eseguire 1, 2 ,3 ,4,5: "))
    
    if(operazione == 1):
        numero_1 = int(input("Inserisci primo numero: "))
        numero_2 = int(input("Inserisci secondo numero: "))

        print("La somma dei due numeri è : ", m.somma(numero_1,numero_2))
    if(operazione == 2):
        numero_1 = int(input("Inserisci primo numero: "))
        numero_2 = int(input("Inserisci secondo numero: "))

        print("La sottrazione dei due numeri è : ", m.sottrazione(numero_1,numero_2))
    
    if(operazione == 3):
        numero_1 = int(input("Inserisci primo numero: "))
        numero_2 = int(input("Inserisci secondo numero: "))

        print("La moltiplicazione dei due numeri è : ", m.moltiplicazione(numero_1,numero_2))
    
    if(operazione == 4):
        numero_1 = int(input("Inserisci primo numero: "))
        numero_2 = int(input("Inserisci secondo numero: "))

        print("La divisione dei due numeri è : ", m.divisione(numero_1,numero_2))
    
    if(operazione == 5):
        break
