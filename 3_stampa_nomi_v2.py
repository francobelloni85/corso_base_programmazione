# ----- CONSEGNA ------ 
# Ci sono 4 nomi: Alina, Bruno, Carlo, Dario.
# Chiedi una lettera all'utente.
# Stampa il nome corrispondente alla prima lettera. 
# Se non è nella lista stampa "you chose ... poorly".
# ---------------------

lettera = input('Inserisci una lettera: ')

# parto dal presupposto che l'utente ha scelto una lettera sbagliata
messaggio_da_stampare = "you chose ... poorly"

# faccio il primo confronto
if(lettera == "A"):
    messaggio_da_stampare = "Hai scelto Alina!"

# dal secondo confronto in poi 
# per leggibilità non li inserisco nell'else!
if(lettera == "B"):
    messaggio_da_stampare = "Hai scelto Bruno!"

if(lettera == "C"):
    messaggio_da_stampare = "Hai scelto Carlo!"

if(lettera == "D"):
    messaggio_da_stampare = "Hai scelto Dario!"

print(messaggio_da_stampare)


lettera = input("press any key to exit")