# ----- CONSEGNA ------ 
# Chiedi all'utente il nome di 3 squadre di calcio. 
# Per ogni squadra inserisci quante partite la squadra ha vinto, pareggiato o perso. 
# Infine stampa la classifica generale.
# ---------------------

i = 0

# Variabili di appoggio
temp_team_name: str = ""
temp_won: int = 0
temp_drow: int = 0
temp_lose: int = 0
temp_total: int = 0

# Varibiali dove salvare i dati
team_1_name: str = "" 
team_1_points: int = 0
team_2_name: str = "" 
team_2_points: int = 0
team_3_name: str = "" 
team_3_points: int = 0

# 1 - Chiedo i dati all'utente
while(i < 3):
    temp_team_name = input("Inserisci il nome della squadra "+str(i+1) + ": ")
    temp_won = int(input("Vittorie: "))
    temp_drow = int(input("Pareggio: "))
    temp_lose = int(input("Sconfitte: "))
    temp_total = (temp_won * 3) + (temp_drow * 1)
    if(i == 0):
        team_1_name = temp_team_name
        team_1_points = temp_total

    if(i == 1):
        team_2_name = temp_team_name
        team_2_points = temp_total

    if(i == 2):
        team_3_name = temp_team_name
        team_3_points = temp_total

    i  = i + 1 

# 2 - Inizio i confronti
# Ci possono essere 6 combinazioni
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
# TROVO IL PRIMO CLASSIFICATO (SQUADRA 1)
# if (squadra_1_punti > squadra_2_punti):
#     if (squadra_1_punti > squadra_3_punti):
#         classifica_squadra_1_punti = squadra_1_punti
#         classifica_squadra_1_name = squadra_1_name
# 
# TROVO IL PRIMO CLASSIFICATO (SQUADRA 2)
# if (squadra_1_punti > squadra_2_punti):
#     if (squadra_1_punti > squadra_3_punti):
#         classifica_squadra_1_punti = squadra_1_punti
#         classifica_squadra_1_name = squadra_1_name
# 
# ... troppo lungo

# BUBLE SORT

# Faccio confronti tra le prime 2 squadre
# se la 2 squadra ha più punti allora la "sposto" come prima
if (team_2_points > team_1_points):
    # salvo i dati per lo swap
    temp_team_name = team_1_name
    temp_total = team_1_points
    # assegno la nuova prima in classifica
    team_1_name = team_2_name
    team_1_points = team_2_points
    # assegno la seconda in classifica
    team_2_name = temp_team_name
    team_2_points = temp_total


# Arrivato qui so che in team_1_points 
# ho la squadra con il numero maggiore di punti.
# (ma manca ancora una squadra ...)


# Faccio il confrontro tra la 1 e la 3
if (team_3_points > team_1_points):
    # salvo i dati per lo swap
    temp_team_name = team_1_name
    temp_total = team_1_points
    # assegno la nuova prima in classifica
    team_1_name = team_3_points
    team_1_points = team_3_points
    # assegno la seconda in classifica
    team_3_name = temp_team_name
    team_3_points = temp_total

# Arrivato qui so che in team_1_points 
# ho la squadra con il numero maggiore di punti tra le 3

# Non so ancora la vera seconda classificata però

# Faccio il confrontro tra la 2 e la 3
if (team_3_points > team_2_points):
    # salvo i dati per lo swap
    temp_team_name = team_2_name
    temp_total = team_2_points
    # assegno la seconda in classifica
    team_2_name = team_3_name
    team_2_points = team_3_points
    # assegno la terza in classifica
    team_3_name = temp_team_name
    team_3_points = temp_total

print("Classifica:")
print("1: " + team_1_name + " con " +str(team_1_points) + " punti.")
print("2: " + team_2_name + " con " +str(team_2_points) + " punti.")
print("3: " + team_3_name + " con " +str(team_3_points) + " punti.")