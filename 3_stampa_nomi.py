# 1) Chiediamo all'utente la lettera
lettera = input('Inserisci una lettera: ')

# Faccio il confronto
if(lettera == "A"):
    print("Hai scelto Alina!")
else:
    # print("Hai scelto una lettera diversa da A")
    
    if(lettera == "B"):
        print("Hai scelto Bruno!")
    else:
        # print("Hai scelto una lettera diversa da A o B")
        
        if(lettera == "C"):
            print("hai scelto Carlo")
        else:
            # print("Hai scelto una lettera diversa da A o B o C")    

            if(lettera == "D"):
                print("hai scelto Dario!")
            else:
                print("You chose ... poorly!")



lettera = input("press any key to exit")
