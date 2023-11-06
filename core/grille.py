class Grille(object):
    def __init__(self, longueur_grille, largeur_grille, grille, nb_bombe):
        self.longueur_grille = longueur_grille
        self.largeur_grille = largeur_grille
        self.grille = grille
        self.bombe_restante = nb_bombe
        self.case_a_decouvrir = longueur_grille*largeur_grille-nb_bombe
        self.grille_devoilee = False
        
        
    def decouvrir_case(self,x,y):
        case = self.grille[x,y]
        case.decouvrir()
        if isinstance(case, Bombe):
            self.case_a_decouvrir = -1
        elif isinstance(case, Voisin):
            self.case_a_decouvrir -= 1
        if isinstance(case, Vide):
            self.case_a_decouvrir -= 1
            for i in range (x-1,x+1):
                for j in range (y-1,y+1):
                    self.grille[i,j].decouvrir()
                    self.case_a_decouvrir -= 1
    
    def test_fin(self):
        while self.grille_devoilee == False:
            if self.case_a_decouvrir == 0:
                self.grille_devoilee == True
            elif self.case_a_decouvrir == -1:
                