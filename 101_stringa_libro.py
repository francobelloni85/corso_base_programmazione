# Stampare una stringa (che sia l'inizio di un libro) in verticale.
i: int = 0
text: str = "Nel mezzo del cammin di nostra vita mi trovai"
count_text = len(text)
while i < count_text:
    n: str = text[i]    
    print(str(n))
    i = i + 1

#region Altre versioni

# OPZIONE "FORMATTATA MEGLIO" 
# Stampare una stringa (che sia l'inizio di un libro) in verticale.
# i: int = 0
# text: str = "Nel mezzo del cammin di nostra vita mi trovai"
# count_text = len(text)
# while i < count_text:
#    n: str = text[i]
#    zero_padding = ""
#    if(i < 9):
#        zero_padding = "0"
#    print(zero_padding + str(i+1) + "> " + str(n))
#    i = i + 1

# VERSIONE CON BUG
# n = len(divina)
# while True:
#     if(i == n):
#         break
#     n=divina[i]
#     print(str(i) + " > " + str(n))
#     i = i + 1

#endregion