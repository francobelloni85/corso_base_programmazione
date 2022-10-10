lettera = input('Inserisci una lettera: ')
messaggio_da_stampare = "Hai scelto in modo errato"

if(lettera == "A"):
    messaggio_da_stampare = "Hai scelto Aldo!"

if(lettera == "B"):
    messaggio_da_stampare = "Hai scelto Bruno!"

if(lettera == "C"):
    messaggio_da_stampare = "Hai scelto Carlo!"

if(lettera == "D"):
    messaggio_da_stampare = "Hai scelto Dario!"

print(messaggio_da_stampare)


lettera = input("press any key to exit")