# ----- CONSEGNA ------ 
# Stampa i primi 10 numeri con il cliclo while. 
# Se sono pari stampa anche un punto escamativo vicino al numero.
# 1 - 2! - 3 - 4!
# ---------------------

i = 1
while i < 10:
    # % 2 è il simbolo per il modulo. (resto della divisione)
    if (i % 2 == 0):
        print(str(i)+"!")
    else :
        print(i)
    i = i + 1
a=input("Press any key to exit")

