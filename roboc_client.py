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


msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    #msg_a_envoyer = input("> ")
    #msg_a_envoyer = msg_a_envoyer.encode()
    #connexion_serveur.send(msg_a_envoyer)
    msg_recu = connexion_serveur.recv(1024)
    carte = pickle.loads(msg_recu)
    print(carte)

os.system("pause")
print("Fermeture")
connexion_serveur.close()