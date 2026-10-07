#esempio sul while

conteggio = 0

while (conteggio < 5):
    print(conteggio)
    conteggio += 1
    

#ciclo booleano
''' controllore = True

while(controllore):
    print("ciao")
    
    scelta = input("scrivi end per uscire: ")
    if  scelta.lower() == "end":
        controllore = False '''
        
#esempio su for

numeri = [1,2,3,4,5]

for numero in numeri:
    print(numero)

limite = 5
for x in range(limite):
    print(x)

for i in range(2,8):
    print(i)
    
for i in range(1,10,2):
    print(i)
    
#---------------------------------------------------------------------
#prova con splat
prova =[*range(10)]
print(prova)