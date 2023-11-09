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
        self.etat_partie = "non_fini"
        
    def __str__(self):
        result = ''
        for i in range (self.largeur_grille):
            for j in range (self.longueur_grille):
                result += ' '
                case = self.grille[i][j]
                if case.etat == "cachee":
                    result += '.'
                elif case.etat == "marquee":
                    result += 'X'
                else:
                    if isinstance(case, Vide):
                        result += '0'
                    elif isinstance(case, Bombe):
                        result += 'B'
                    elif isinstance(case, Voisin):
                        result += str(case.nb_voisin)
            result += '\n'
                    
        return result
        
        
    def decouvrir_case(self,x,y,action):
        case = self.grille[x][y]
        if action == 'm':
            case.marquer()
        else:
            case.decouvrir()
            if isinstance(case, Vide):                
                for i in range (x-1,x+2):
                    for j in range (y-1,y+2):
                        if 0 <= i < self.largeur_grille and 0 <= j < self.longueur_grille and self.grille[i][j].etat == "cachee":
                            self.decouvrir_case(i,j,'d')
                    
    
    def test_fin(self):
        for i in range (self.largeur_grille):
            for j in range (self.longueur_grille):
                case = self.grille[i][j]
                if not isinstance(case, Bombe) and case.etat == "cachee":
                    self.etat_partie = "non_fini"
                elif isinstance(case, Bombe) and case.etat == "decouvert":
                    self.etat_partie == "erreur"
                else:
                    self.etat_partie == "fini"