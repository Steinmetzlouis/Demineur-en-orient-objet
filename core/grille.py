# from partie import Partie
from case_bombe import Bombe
from case_vide import Vide
from case_voisin import Voisin

class Grille(object):
    def __init__(self, etat_partie, longueur_grille, largeur_grille, grille, nb_bombe):
        self.longueur_grille = longueur_grille
        self.largeur_grille = largeur_grille
        self.grille = grille
        self.bombe_restante = nb_bombe
        self.case_a_decouvrir = longueur_grille*largeur_grille-nb_bombe
        self.etat_partie = "non_fini"
        
    def __str__(self):
        result = ''
        for i in range (self.largeur_grille):
            for j in range (self.longueur_grille):
                case = self.grille[i][j]
                if case.etat == "cachee":
                    result += '? | '
                elif case.etat == "marquee":
                    result += 'X | '
                else:
                    if isinstance(case, Vide):
                        result += '  | '
                    elif isinstance(case, Bombe):
                        result += 'B | '
                    elif isinstance(case, Vide):
                        result += '{} | '.format(self.case.nb_voisin)
            result += '\n'
                    
        return result
        
        
    def decouvrir_case(self,x,y):
        case = self.grille[x][y]
        case.decouvrir()
        if isinstance(case, Bombe):
            self.case_a_decouvrir = -1
        elif isinstance(case, Voisin):
            self.case_a_decouvrir -= 1
        if isinstance(case, Vide):
            self.case_a_decouvrir -= 1
            for i in range (x-1,x+1):
                for j in range (y-1,y+1):
                    self.grille[i][j].decouvrir()
                    self.case_a_decouvrir -= 1
    
    def test_fin(self):
        if self.case_a_decouvrir == 0:
            self.etat_partie == "fini"
        elif self.case_a_decouvrir == -1:
            self.etat_partie == "erreur"