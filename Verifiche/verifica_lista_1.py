# ----- CONSEGNA ------ 
# Scrivi il programma Python e il flowchar del seguente esercizio: 
# 1. Inserisci in una lista i primi 20 numeri pari, maggiori di 0 e il numero sette.  
# 2. Stampa il risultato solo alla fine dell’ultimo numero inserito come nell’esempio. 
# 3. Stampa la scritta “--parte 2--” 
# 4. Per ogni elemento della lista se è multiplo di quattro cambia il suo valore con la stringa “ciao” 
# Stampa il risultato solo alla fine dell’ultimo cambio come nell’esempio. 
# ---------------------

my_list = []
i = 1
while i < 20:
    if(i % 2 == 0) or (i == 7):
        my_list.append(i)
    i = i + 1

i = 0
while i < len(my_list):
    print(str(i) +") " + str(my_list[i]))
    i = i + 1

print("--parte 2 --")

i = 0
while i < len(my_list):
    if(int(my_list[i]) % 4 == 0):
        my_list[i] = "ciao"
    i = i + 1

i = 0
j = 1
while i < len(my_list):
    print(str(j) +") " + str(my_list[i]))
    j = j + 2
    i = i + 1