# ----- CONSEGNA ------ 
# Stampa le combinazioni e quante volte sono uscite le combinazioni di 2 dati
# fino a quanto non esce il 6-6.
# ---------------------
import random

dice_1: int = 0
dice_2: int = 0
list_dice_extraction: list[str] = []
dice_format: str = "{0}-{1}"

# Mi salvo in una lista tutte le estrazioni avvenute
while True:
    dice_1 = random.randrange(6) + 1
    dice_2 = random.randrange(6) + 1
    list_dice_extraction.append(dice_format.format(dice_1,dice_2))
    if(dice_1 == 6 and dice_2 == 6):
        break

# Stampo la lista per poi controllare.
print(list_dice_extraction)

while(len(list_dice_extraction) != 0):

    # Recupero il primo elemento della lista
    item = list_dice_extraction[0]

    # https://www.w3schools.com/python/ref_list_count.asp 
    # conto quanti elementi nella lista oltre al primo
    count_elements: int = list_dice_extraction.count(item)

    # stampo l'elemento e quante volte è stato estratto.
    print("{0} | {1}".format(item, count_elements))

    # https://www.geeksforgeeks.org/remove-all-the-occurrences-of-an-element-from-a-list-in-python/
    # Rimuovo tutti gli elementi che ho già stampato dalla lista, uno alla volta.
    i: int = 0    
    while i < count_elements:
        list_dice_extraction.remove(item)
        i = i + 1
