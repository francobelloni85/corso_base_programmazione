# ----- CONSEGNA ------ 
# Chiedi all'utente di indovinare un numero magico. 
# Il numero magico è il numero 7. 
# L'utente ha 10 tentativi.
# Se indovina stampa "Complimenti, hai indovinato!" 
# Se non indovina stampa "Game over!"
# ---------------------
numero_magico = 7
numero = 0
output = "Game Over!"
i = 1
while i <= 10:
    numero = int(input("Prova ad indovinare il numero magico: "))
    if(numero == numero_magico):
        output = "Complimenti, hai indovinato!"        
        break
    i = i + 1
print(output)
 
# exit
lettera = input("press any key to exit")