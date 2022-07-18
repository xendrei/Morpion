import random
from time import sleep

### Reste à gérer
# 1) Le jeu ne fonctionne pas si les 2 joueurs entrent le même nom
# 2) Le joueur ne peux plus changer son nom s'il s'est trompé, ou si par exemple il a appuyé
#    sur Entrée trop rapidement sans faire attention. Dans ce cas il aura un nom vide.

### Variables
# On génère la grille qui sera utilisée pour le jeu
grille=list(range(1,10))
# On définit les variables pour le joueur en cours
joueur = ""
autre_joueur = ""
case_joueur = ""
signe_joueur = ""
# On définit les variables pour les 2 joueurs
j1 = ""
j2 = ""
nom_j1 = ""
nom_j2 = ""
signe_j1 = ""
signe_j2 = ""


### Fonctions
# Fonction qui définit quel joueur va jouer en premier
def choix_premier():
    if random.randint(0,1000) % 2 == 0:
        return True
    else:
        return False

# Fonction qui demande au 1er joueur quel signe il souhaite utiliser (X ou O) et affecte l'autre au second joueur
def choix_signe_joueur():
    global signe_j1
    global signe_j2
    print(f"\n{j1}, quel signe souhaites-tu utiliser ? X ou O ?")
    print(f"(Merci d’entrer la lettre x ou la lettre o (majuscule ou minuscule))")
    signe_j1 = input(">>> ")
    try:
        if signe_j1 in "xoXO" and len(signe_j1) == 1:
            print(f"\nParfait {j1}, tu utiliseras le signe {signe_j1.upper()}")
            if signe_j1 in "oO":
                signe_j2 = "X"
            else:
                signe_j2 = "O"
            print(f"\n{j2}, tu auras donc le signe {signe_j2}")
            return
    except: #Exception as err:
        #exception_type = type(err).__name__
        #print(exception_type)
        print("Tu n'as pas saisi X ou O...")
        choix_signe_joueur()

# Fonction qui affiche la grille en cours
def affiche_grille():
    global grille
    s="|"
    print(13*"-")
    i = 1
    for x in grille:
        if i%3 != 0:
            s += f" {x} |"
        else:
            s += f" {x} |"
            print(s)
            print(13*"-")
            s = "|"
        i+=1

# Fonction qui demande au joueur en cours sur quelle case il veut jouer
def choix_du_joueur():
    global grille
    global joueur
    global signe_joueur
    global case_joueur
    print(f"Sur quelle case souhaites-tu jouer {joueur}? ({signe_joueur})\n")
    try:
        case_joueur = int(input(">>> "))
        if not verifie_position():
            raise ValueError
    except: #Exception as err:
        #exception_type = type(err).__name__
        #print(exception_type)
        print(f"Tu ne peux pas jouer sur cette case {joueur}...")
        print("\nVoici la grille :\n")
        affiche_grille()
        choix_du_joueur()

# Fonction qui vérifie que la position choisie par le joueur en cours est jouable
def verifie_position():
    global grille
    global case_joueur
    # La vérif du case_joueur > 0 permet d'empêcher le joueur de mettre une valeur négative comme -5 qui fonctionnerait
    # et irait dans le mauvais index
    if case_joueur > 0 and 1 <= int(grille[case_joueur-1]) <= 9:
        return True
    else:
        return False

# Fonction qui place le signe du joueur en cours sur al position choisie dans la grille
def placer_signe():
    global grille
    grille[case_joueur-1]=signe_joueur

# Fonction qui vérifie si une combinaison gagnante est trouvée dans la grille
# Cette fonction modifie également la grille afin de ne laisser que la combinaison gagnante pour plus de clarté à la fin du jeu
def verifie_gagnant():
    global grille
    if grille[0] == grille[1] == grille[2] == signe_joueur:
        for i in range(3,9):
            grille[i] = " "
        return True
    elif grille[3] == grille[4] == grille[5] == signe_joueur:
        for i in range(0,3):
            grille[i] = " "
        for i in range(6,9):
            grille[i] = " "
        return True
    elif grille[6] == grille[7] == grille[8] == signe_joueur:
        for i in range(0,6):
            grille[i] = " "
        return True
    elif grille[0] == grille[3] == grille[6] == signe_joueur:
        for i in range(1,3):
            grille[i] = " "
        for i in range(4,6):
            grille[i] = " "
        for i in range(7,9):
            grille[i] = " "
        return True
    elif grille[1] == grille[4] == grille[7] == signe_joueur:
        grille[0] = " "
        grille[8] = " "
        for i in range(2,4):
            grille[i] = " "
        for i in range(5,7):
            grille[i] = " "
        return True
    elif grille[2] == grille[5] == grille[8] == signe_joueur:
        for i in range(0,2):
            grille[i] = " "
        for i in range(3,5):
            grille[i] = " "
        for i in range(6,8):
            grille[i] = " "
        return True
    elif grille[0] == grille[4] == grille[8] == signe_joueur:
        for i in range(1,4):
            grille[i] = " "
        for i in range(5,8):
            grille[i] = " "
        return True
    elif grille[2] == grille[4] == grille[6] == signe_joueur:
        grille[3] = " "
        grille[5] = " "
        for i in range(0,2):
            grille[i] = " "
        for i in range(7,9):
            grille[i] = " "
        return True
    else:
        return False

# Fonction qui vérifie si la grille est complète
def verifie_grille_complet():
    global grille
    for x in grille:
        if isinstance(x, int):
            return False
    return True

# Fonction qui initialise le jeu avec toutes les données nécessaires pour lancer une partie
def init_jeu():
    global grille
    global joueur
    global autre_joueur
    global nom_j1
    global nom_j2
    global j1
    global j2
    grille=list(range(1,10))
    print("\nBienvenue dans le jeu du morpion bande de fous !")
    sleep(1)

    # On demande et enregistre les noms des 2 participants
    print("\nQuel est le nom du premier joueur ?")
    nom_j1 = input(">>> ")
    print("\nQuel est le nom du deuxième joueur ?")
    nom_j2 = input(">>> ")
    print(f"\nTrès bien {nom_j1} et {nom_j2} ! Que le match à mort sur ce morpion commence !")
    sleep(1)

    # On affecte les noms des joueurs à leur position (1er ou 2eme à jouer)
    if choix_premier():
        j1 = nom_j1
        j2 = nom_j2
    else:
        j1 = nom_j2
        j2 = nom_j1
    print(f"\nLa dure loi de l'aléatoire a frappé ! {j1}, tu joueras en premier !")
    sleep(1)
    
    # Le joueur qui joue en premier choisi le signe qu'il souhaite utilisé pendant la partie
    choix_signe_joueur()
    sleep(3)
    
    # On dit que le joueur en cours pour ce début de partie est le joueur qui joue en premier
    joueur = j1
    autre_joueur = j2


### Début du jeu
init_jeu()

# On lance une boucle while pour répéter les tours jusqu'à ce que la partie soit finie
while True:
    # On définit le nom et le signe du joueur en cours
    if joueur == j1:
        signe_joueur = signe_j1
    else:
        signe_joueur = signe_j2
    
    print(40*"-")
    print(f"\nA toi de jouer {joueur}, concentre-toi un peu !")
    
    # On affiche la grille en cours
    print("\nVoici la grille :\n")
    affiche_grille()
    
    # Le joueur en cours choisit la position sur laquelle il veut jouer
    choix_du_joueur()
    
    # On mets à jour al grille avec le choix du joueur
    placer_signe()
    
    # Si le joueur en cours à gagné avec son dernier tour
    # on termine le jeu et demande aux joueurs s'is veulent rejouer
    if verifie_gagnant():
        print(f"\nBravo {joueur}, tu as gagné ! {autre_joueur} tu es un gros loser...")
        print(f"\nVoici la ligne qui t'as fait gagner {joueur} :\n")
        affiche_grille()   
        # A mettre dans un try except pour mieux gérer le oui|non     
        print("\nSouhaitez-vous rejouer ? (oui pour rejouer, n'importe quel autre touche pour quitter le jeu")
        if input(">>> ") == "oui":
            print(f"\nOK, let's GO ! Si c'est une revanche, essaye de ne pas encore te faire ridiculiser {autre_joueur}...")
            init_jeu()
            continue
        else:
            print("Vous n'avez pas tapé oui, le jeu se termine donc ici...\n")
            break
    
    # Si personne n'a gagné et que le tableau est complet
    # on termine le jeu et demande aux joueurs s'is veulent rejouer
    if verifie_grille_complet():
        print("\nLe tableau est complet, c'est fini ! Vous êtes tous les deux des losers...")
        print("\nVoici la grille finale :\n")
        affiche_grille()
        # A mettre dans un try except pour mieux gérer le oui|non 
        print("\nSouhaitez-vous rejouer ? (oui pour rejouer, n'importe quel autre touche pour quitter le jeu")
        if input(">>> ") == "oui":
            init_jeu()
            continue
        else:
            print("Vous n'avez pas tapé oui, le jeu se termine donc ici...\n")
            break
    
    # On change le joueur en cours avant de passer à la boucle suivante
    if joueur == j1:
        joueur = j2
        autre_joueur = j1
    else:
        joueur = j1
        autre_joueur = j2
    
    print(40*"-")
    print(40*"-")
    print("======= CHANGEMENT DE JOUEUR ! =========")
    print(40*"-")