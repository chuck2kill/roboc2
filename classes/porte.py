# -*-coding:Utf-8 -*

"""Fichier contenant la classe Porte, héritée de la classe Obstacle"""

from classes.obstacle import Obstacle


class Porte(Obstacle):

    """Classe représentant une porte"""

    peut_traverser = True
    nom = "porte"
    symbole = "."
