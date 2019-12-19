# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du client roboc"""

import os
import socket, pickle

# Initialisation de la connexion
hote = "localhost"
port = 21000
connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_serveur.connect((hote, port))

print("Connexion établie avec le serveur sur le port {}".format(port))

#joueur = input("Entrez votre pseudo : ")



msg_recu = connexion_serveur.recv(1024)
carte = msg_recu.decode()
print(carte)

commencer = input("Appuyez sur C pour commencer la partie\n").lower()



os.system("pause")
print("Fermeture")
connexion_serveur.close()