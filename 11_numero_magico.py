# ----- CONSEGNA ------ 
# Chiedi all'utente di indovinare un numero magico. 
# Il numero magico è il numero 7. 
# L'utente ha 10 tentativi.
# Se indovina stampa "Complimenti, hai indovinato!" 
# Se non indovina stampa "Game over!"
# ---------------------

i = 1
while i <= 10:
    print("INIZIO BLOCCO WHILE")
    print(i)
    i = i + 1

    if (i==5):
        print("ESCO")
        break
    print("FINISCO BLOCCO WHILE")

# exit

lettera = input("press any key to exit")