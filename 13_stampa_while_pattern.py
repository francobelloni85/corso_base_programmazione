# ----- CONSEGNA ------ 
# Stampa il seguente pattern:
# 1
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# ---------------------

# Variabile usata per salvare 
# "dove sono arrivato" ad ogni ciclo 
output = ""
counter = 1

while counter <= 6:
    print(output)
    output = output + " " + str(counter)  
    counter = counter+1

a=input("Press any key to exit")