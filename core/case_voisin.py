from case import Case

class Voisin(Case):
    """Classe définissant une case contenant à minima une bombe autour d'elle.
    
    Attributes
    ----------
    etat : str
        etat de la case. 3 disponibles: 'cachee', 'marquee', 'decouvert'
    x : int
        coordonnée de cette case: lignes
    y : int
        coordonnée de cette case: colonnes
    nb_voisin : int
        nombre de bombes autour de cette case
    """
    def __init__(self, x, y, nb_voisin):
        """Constructeur de la classe Voisin.

        Parameters
        ----------
        x : int
            coordonnée de cette case: lignes
        y : int
            coordonnée de cette case: colonnes
        nb_voisin : int
            nombre de bombes autour de cette case
        """
        super().__init__(x,y)
        self.nb_voisin = nb_voisin
        
    def decouvrir(self):
        """Fonction qui permet de changer l'état de la case en "découvert".
        """
        self.etat = "decouvert"