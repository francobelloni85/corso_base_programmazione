# ----- CONSEGNA ------ 
# Chiedi all'utente 2 stringhe. 
# Controlla che tutti i caratteri presenti nella prima stringa siano presenti nella seconda striga. 
# Non importa la posizione. Stampa il risultato se vero o falso.
# ---------------------

input_to_check: str = ""
while(len(input_to_check)== 0):
    input_to_check = input("Inserisci la stringa da controllare: ")

text: str = ""
while(len(text)== 0):
    text = input("Inserisci la stringa di testo: ")

# Mi serve per salvarmi se ho trovato il carattere
is_char_found = False

i: int = 0
# Ciclo sulla prima stringa
while(i<len(input_to_check)-1):

    # recupero il carattere da cercare
    current_char: str = input_to_check[i]

    # Mi serve per salvarmi se ho trovato il carattere
    # Resetto il suo valore per ogni nuovo carattere
    is_char_found = False

    # Ciclo sulla seconda stringa
    j: int = 0
    while(j < len(text)):
        if(current_char == text[j]):
            is_char_found = True
            break
        j = j + 1

    if (is_char_found == False):        
        print(str.format("Non c'è il carattere {0}", current_char))
        break

    i = i + 1

if(is_char_found):
    print("Trovati tutti i caratteri")
else:
    print("Purtroppo non ho trovato tutti i caratteri")