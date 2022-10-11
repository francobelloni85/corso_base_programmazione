# ----- CONSEGNA ------ 
# Chiedi 2 numeri all'utente. 
# Se il primo è maggiore di 10 scrivi "FUORI SCALA".
# Se il secondo numero è maggiore di 50 scrivi "TROPPO GRANDE". 
# Se non hai stampato nulla allora stampa "TUTTO OK"
# ---------------------

n1 = int(input("Inserisci il primo numero"))
n2 = int(input("Inserisci il secondo numero"))

# varibile che mi segna se ho già stampato qualcosa...
stampato = 0

if(n1 > 10):
    print("Fuori Scala")
    stampato = 1
     
if(n2 > 50):
    print("Troppo Grande")
    stampato = 1

if(stampato == 0):
    print("Tutto ok")
