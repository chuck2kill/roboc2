# -*-coding:Utf-8 -*

"""Fichier contenant la classe Sortie, héritée de la classe Obstacle"""

from classes.obstacle import Obstacle


class Sortie(Obstacle):

    """Classe représentant une sortie du labyrinthe

    Quand le robot arrive sur cette case, la partie est considérée comme
    terminée"""

    peut_traverser = True
    nom = "sortie"
    symbole = "U"

    def arriver(self, labyrinthe, robot):
        """Le robot arrive sur la sortie

        La partie est gagnée"""

        labyrinthe.gagnee = True
