# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du serveur roboc"""

import socket, select, pickle, os

from classes.carte import Carte
from classes.labyrinthe import *

# Initialisation de la connexion
hote = ''
port = 21000
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute sur le port {}".format(port))

nb_joueurs = str
while type(nb_joueurs) is not int:
    nb_joueurs = input("Entrez le nombre de joueurs : ")
    try:
        nb_joueurs = int(nb_joueurs)
    except ValueError:
        print("On attend un chiffre !!")

# On charge les cartes existantes
chemin = None
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].lower()
        with open(chemin, "r") as fichier:
            lecture = fichier.read()
            contenu = []
            contenu.append(lecture)
            try:
                carte = Carte(nom_carte, contenu[0])
            except ValueError as err:
                print("Erreur lors de la lecture de {} : {}".format(chemin, str(err)))
            else:
                cartes.append(carte)

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print(" {} - {}".format(i + 1, carte.nom))
    liste_labyrinthes = (" {} - {}\n".format(i + 1, carte.nom))

# Choix de la carte
carte = None
labyrinthe = None
partie = True
choix = 0
while labyrinthe is None:
    choix = input("Entrez un numéro de labyrinthe pour commencer à jouer : ")
    if choix.lower() == "r":
        if partie:
            labyrinthe = partie
        else:
            print("Il n'y a aucune partie enregistrée pour le moment.")
    else:
        # Si le joueur n'a pas entré R, on s'attend à un nombre
        try:
            choix = int(choix)
        except ValueError:
            print("choix invalide : {}".format(choix))
        else:
            if choix < 1 or choix > len(cartes):
                print("Numéro {} invalide".format(choix))
                continue

            carte = cartes[choix - 1]
            labyrinthe = carte.labyrinthe

print("On attend les clients")

i = 0
vrai_chemin = None
for fichier in os.listdir("cartes"):
    if fichier.endswith(".txt"):
        chemin = os.listdir("cartes")[choix - 1]

# On ouvre la bonne carte
serveur = True
vrai_chemin = os.path.join("cartes", chemin)
with open(vrai_chemin, "r") as fichier:
    contenu_carte = fichier.read()

# On reçoit la connexion des clients et on leur envoie la carte de départ
clients_connectes = []
while serveur:
    connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        clients_connectes.append(connexion_avec_client)
        bienvenue = []

        for i, connexion in enumerate(clients_connectes):
            bienvenue.append("Bienvenue joueur {}, votre socket est {}\n".format(i + 1, connexion))
            bienvenue[i] = bienvenue[i].encode()
            clients_connectes[i].send(bienvenue[i])
            data1 = contenu_carte.encode()
            clients_connectes[i].send(data1)

    if len(clients_connectes) == nb_joueurs:
        serveur = False
        #data1 = contenu_carte.encode()
        #clients_connectes[i].send(data1)

bienvenue = []

data1 = contenu_carte.encode()

while not labyrinthe.gagnee:
    coup = input("> ")
    if coup == "":
        continue
    elif coup.lower() == "q":
        # On quitte la partie
        break
    elif coup[0].lower() in "nseo":
        lettre = coup[0].lower()
        if lettre == "e":
            direction = "est"
        elif lettre == "n":
            direction = "nord"
        elif lettre == "s":
            direction = "sud"
        else:
            direction = "ouest"

        # On va essayer de convertir le déplacement
        coup = coup[1:]
        if coup == "":
            nombre = 1
        else:
            try:
                nombre = int(coup)
            except ValueError:
                print("Nombre invalide : {}".format(coup))
                continue

        labyrinthe.deplacer_robot(direction, nombre)
    else:
        print("coups autorisés :")
        print(" Q pour sauvegarder et quitter la partie en cours")
        print(" E pour déplacer le robot vers l'est")
        print(" S pour déplacer le robot vers le sud")
        print(" O pour déplacer le robot vers l'ouest")
        print(" N pour déplacer le robot vers le nord")
        print(" Vous pouvez préciser un nombre apès la direction")
        print(" Pour déplacer votre robot plus vite. Exemple -> n3")

if labyrinthe.gagnee:
    print("Bravo, vous avez gagné !")
    labyrinthe.detruire()
else:
    print("Votre partie a été sauvegardée.")
