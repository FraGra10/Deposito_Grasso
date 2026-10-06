comando = input("Inserisci comando: ")

match comando: 
    case "oggi":
        print("Hai stampato 'oggi' ")
    case "domani":
        print("Hai stampanto 'domani'")
    case "dopodomani": 
        print("Hai stampato 'dopodomani'")  
    case _:
        print("Nessun giorno selezionato")