# VARIABILI

# Numero intero
numero : int = 0

# Numeri con la virgola
valore_febbre: float = 37.7
print(valore_febbre)

# Stringhe

# Inizializzare una stringa
# che e' semplicemente una sequenza di caratteri

x = "Ciao sono pippo"

# In memoria ogni carattere della stringa ha la sua celletta.
# ---------------------------------
# | C | i | a | o |   | s | o | 
# --------------------------------

# Per selezionare un solo carattere (char)
lettera = x[0]
print(lettera)

seconda_lettera = x[1]
print(seconda_lettera)

print("")

# Operazioni sulle strighe

# https://docs.python.it/html/lib/module-string.html

# 1.  Concatenare stringhe
nome = "Giuseppe"
cognome = "Garibaldi"

full_name = nome + " " + cognome
print(full_name)

print("")

# 2. Da intero a stringa 'A'
lettera_a = chr(65)
print(lettera_a)

# 2B. Da intero a stringa 'a'
lettera_a = chr(97)
print(lettera_a)

print("")

# 3. Concatenare tutto l'alfabeto con while
i: int = 65
result = ""
while i < 91:
    t_lettera = chr(i)
    print(str(i) + " > "  + t_lettera)
    result = result + " " + t_lettera
    i = i + 1
    
print("")

print("RISULTATO ALFABETO")
print(result)

print("")

# Modificare le stringhe

# 4. tutto minuscolo
result = result.lower()
print("Converto tutti in minuscolo")
print(result)

print("")

# 5. conto le occorrenze della lettera s
count_s = result.count("s")
print("Conto le lettere s", count_s)

print("")

# 5A. aggiungo altre 3 s

result = result + " s " + " ss"
count_s = result.count("s")
print("Conto le lettere s dopo l'aggiunta", count_s)

# 6. Sostituire una stringa

# replace(str, old, new[, maxreplace])

# Restituisce una copia della stringa str con tutte le occorrenze
# della sotto stringa old sostituite dalla stringa new.
# Se l'argomento facoltativo maxreplace viene fornito, 
# le prime maxreplace occorrenze vengono sostituite. 
print("Sostituzione stringa:")

saluti = "Ciao sono Paolino Paperino"
saluti = saluti.replace("Paolino","Paperoga")

print("La variabile saluti ora vale: ", saluti)

print("")