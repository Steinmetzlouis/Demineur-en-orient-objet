from case import Case

class Vide(Case):
    """Classe définissant une case vide.
    
    Attributes
    ----------
    etat : str
        etat de la case. 3 disponibles: 'cachee', 'marquee', 'decouvert'
    x : int
        coordonnée de cette case: lignes
    y : int
        coordonnée de cette case: colonnes
    """
    def decouvrir(self):
        """Fonction qui permet de changer l'état de la case en "découvert".
        """
        if self.etat != "marquee":
            self.etat = "decouvert"