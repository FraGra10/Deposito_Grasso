file_valorizzato_da_open = open("pippo.txt", "r")


#metodo di lettura totale del file 
#contenuto_file_totale = file_valorizzato_da_open.read()
#print(contenuto_file_totale)

#metodo di lettura line by line 
contenuto_file_riga = file_valorizzato_da_open.readline()

print(contenuto_file_riga)

file_valorizzato_da_open.close()

file_valorizzato_da_open = open("pippo.txt", "w")

file_valorizzato_da_open.write("prova")
file_valorizzato_da_open.close()


#Per garantire automaticamente la chiusura di un file 
with open("pippo.txt","r") as file:
    contenuto = file.read()
    print(contenuto)