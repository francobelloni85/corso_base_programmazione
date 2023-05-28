# ----- CONSEGNA ------ 
# 1. Inserisci in una lista i primi 20 numeri multipli di 3 o multipli di 7.  
# 2. Stampa il risultato solo alla fine dell’ultimo numero inserito come nell’esempio. 
# 3. Stampa la scritta “--parte 2--” 
# 4. Per ogni elemento della lista se è pari cambia il suo valore con la stringa “ciao” 
# 5. Stampa il risultato solo alla fine dell’ultimo cambio come nell’esempio.  
# ---------------------

my_list = []
i = 0
while i < 20:
    if(i % 3 == 0) or (i % 7 == 0):
        my_list.append(i)
    i = i + 1

i = 0
while i < len(my_list):
    print(str(i) +") " + str(my_list[i]))
    i = i + 1

print("--parte 2 --")

i = 0
while i < len(my_list):
    if(int(my_list[i]) % 2 == 0):
        my_list[i] = "ciao"
    i = i + 1

i = 0
j = 10
while i < len(my_list):
    print(str(j) +") " + str(my_list[i]))
    j = j + 3
    i = i + 1