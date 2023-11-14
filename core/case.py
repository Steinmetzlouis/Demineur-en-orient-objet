class Case(object):
    """Classe dfinissant une case.
    
    Attributes
    ----------
    etat : str
        etat de la case. 3 disponibles: 'cachee', 'marquee', 'decouvert'
    x : int
        coordonne de cette case: lignes
    y : int
        coordonne de cette case: colonnes
    """
    def __init__(self, x, y):
        """Constructeur de la classe Case.

        Parameters
        ----------
        x : int
            coordonne de cette case: lignes
        y : int
            coordonne de cette case: colonnes
        """
        self.etat = "cachee"
        self.x = x
        self.y = y
    
    
    def marquer(self):
        """Fonction qui modifie l'etat de la case, entre marque et cache. 
        """
        if self.etat == "cachee":
            self.etat = "marquee"
        
        elif self.etat == "marquee":
            self.etat = "cachee"
            
            
    def decouvrir(self):
        raise NotImplementedError()