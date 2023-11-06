from case import Case

class Voisin(Case):
    def __init__(self, x, y, nb_voisin):
        super().__init__(x,y)
        self.nb_voisin = nb_voisin
        
    def decouvrir(self):
        self.etat = "decouvert"