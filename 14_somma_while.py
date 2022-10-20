# ----- CONSEGNA ------ 
# Chiedi un numero all'utente 
# e somma i numeri da 1 fino al numero immesso.
# ---------------------

numero = int(input("Metti un numero: "))
i = 1
tot = 0
while True:
    tot = tot + i  
    if(i == numero):
        break
    i = i + 1
print(tot)
a=input("Press any key to exit")