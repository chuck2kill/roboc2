# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du client roboc"""

import os
import socket

# Initialisation de la connexion
hote = "localhost"
port = 21000
connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_serveur.connect((hote, port))

joueur = input("Entrez votre pseudo : ")


msg_recu = connexion_serveur.recv(1024)
print(msg_recu.decode())
os.system("pause")