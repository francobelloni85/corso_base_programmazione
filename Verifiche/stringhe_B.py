# ----- CONSEGNA ------   
# Chiedi all’utente due stringhe.
# Confronta la lunghezza e il numero delle vocali presenti. (2 punti) 
# Continua a chiederle finché non hanno lo stesso numero di caratteri e di vocali. (1 punto) 
# Stampa “Numero diverso di vocali” e “Lunghezza diversa” 
# come messaggio di errore se le condizioni non sono soddisfatte (2 punti) 
# ---------------------

text_a: str = ""
text_b: str = ""

while True:

    text_a = input("Stringa A: ")
    text_b = input("Stringa B: ")

    count_vowels_a: int = 0
    count_vowels_b: int = 0

    i: int = 0
    while(i < len(text_a)):
        current: str = text_a[i]
        if(current == "a" or current == "o" or current == "u" or current == "i" or current == "e"):
            count_vowels_a = count_vowels_a + 1
        i = i + 1

    j: int = 0
    while(j < len(text_b)):
        current = text_b[j]        
        if(current == "a" or current == "o" or current == "u" or current == "i" or current == "e"):
            count_vowels_b = count_vowels_b + 1
        j = j + 1

    is_same_vowels: bool = True
    is_same_lenght: bool = True

    if(count_vowels_a != count_vowels_b): 
        print("Numero diverso di vocali")
        is_same_vowels = False

    if(len(text_a) != len(text_b)): 
        print("Lunghezza diversa")
        is_same_lenght = False

    if (is_same_vowels and is_same_lenght and (len(text_a) != 0 or len(text_b) != 0)):
        break

print("Fine ... ")