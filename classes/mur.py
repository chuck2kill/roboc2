# -*-coding:Utf-8 -*

"""Fichier contenant la classe Mur, héritée de
la classe Obstacle"""

from classes.obstacle import Obstacle


class Mur(Obstacle):
    """Classe représentant un mur"""

    peut_traverser = False
    nom = "mur"
    symbole = "O"
