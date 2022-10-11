# ----- CONSEGNA ------ 
# Ci sono 4 nomi: Alina, Bruno, Carlo, Dario.
# Chiedi una lettera all'utente.
# Stampa il nome corrispondente alla prima lettera. 
# Se non è nella lista stampa "you chose ... poorly".
# ---------------------


# 1) Chiediamo all'utente la lettera
lettera = input('Inserisci una lettera: ')

# Faccio il primo confronto con la lettera A
if(lettera == "A"):
    print("Hai scelto Alina!")
else:
    # print("Hai scelto una lettera diversa da A")
    
    # Faccio il secondo confronto con la lettera B
    if(lettera == "B"):
        print("Hai scelto Bruno!")
    else:
        # print("Hai scelto una lettera diversa da A o B")
        
        # Faccio il terzo confronto con la lettera C
        if(lettera == "C"):
            print("hai scelto Carlo")
        else:
            # print("Hai scelto una lettera diversa da A o B o C")    

            # Faccio l'ultimo confronto con la lettera D
            # Se la lettera selezionata è diversa allora ho scelto male!
            if(lettera == "D"):
                print("hai scelto Dario!")
            else:
                print("You chose ... poorly!")


# exit
lettera = input("press any key to exit")
