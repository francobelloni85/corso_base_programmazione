# ----- CONSEGNA ------ 
# Inserisci due stringhe ma se sono uguali allora richiederle. (1 punti) 
# Se il primo carattere della prima stringa è uguale all’ultimo carattere della seconda stringa (1 punto) 
# allora stampa la prima stringa all’incontrario (2 punti).  
# Se sono diversi stampa la seconda stringa (1 punto)  
# ---------------------

text_a: str = ""
text_b: str = ""

while True:
    text_a = ""
    while(len(text_a)==0):
        text_a: str = input("inserisci stringa A: ")
    text_b = ""
    while(len(text_b)==0):
        text_b: str = input("inserisci stringa B: ")
    if(text_a != text_b):
        break 

print("ok, stringhe diverse")

if(text_a[0] == text_b[len(text_b)-1]):
    result: str = ""
    i = len(text_b)-1
    while(i >= 0):
        result = result + text_b[i]
        i =  i - 1
    print(result)
else:
    print(text_a)

