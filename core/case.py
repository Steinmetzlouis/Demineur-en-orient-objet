class Case(object):
    """Classe d�finissant une case
    
    Attributes
    ----------
    etat : str
        etat de la case. 3 disponibles: 'cachee', 'marquee', 'decouvert'
    nb_bombe : int
        nombre de bombes � placer dans la grille
    x : int
        coordonn�e de cette case: lignes
    y : int
        coordonn�e de cette case: colonnes
    """
    def __init__(self, x, y):
        """Constructeur de la classe Case
        """
        self.etat = "cachee"
        self.x = x
        self.y = y
    
    
    def marquer(self):
        """Fonction qui modifie l'etat de la case, entre marquée et cachée. 
        """
        if self.etat == "cachee":
            self.etat = "marquee"
        
        elif self.etat == "marquee":
            self.etat = "cachee"
            
            
    def decouvrir(self):
        raise NotImplementedError()