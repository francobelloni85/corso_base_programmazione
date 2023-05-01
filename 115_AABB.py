# ----- CONSEGNA ------ 
# Stampa 99 righe da 1 a 100 con questa logica: 
# stampa tante A quante sono le unità e stampa tante B quante sono le decine.
# 1 > A
# 2 > AA 
# 13 > BAAA
# 20 > BB
# 25 > BBAAAAA 
# ---------------------

i: int = 1
while (i<101):
    a: str = ""
    b: str = ""
    unit: int = int(i % 10)
    tens: int = int(i / 10)
    
    j: int = 0
    while(j<unit):
        a = a + "A"
        j = j + 1

    j = 0
    while(j<tens):
        b = b + "B"    
        j = j + 1          
    
    print(str.format("{0}){1}{2}",i,b,a))
    i = i + 1  


