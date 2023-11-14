# from partie import Partie
from case_bombe import Bombe
from case_vide import Vide
from case_voisin import Voisin

class Grille(object):
    """Classe définissant une case.
    
    Attributes
    ----------
    longueur_grille : int
        plus grand coté de la grille (= nb de colonnes)
    largeur_grille : int
        plus petit coté de la grille (= nb de lignes)
    etat_partie : str
        renseigne sur l'état de la partie. 3 etats possibles: 'non_fini', 'fini' et 'erreur'
    """
    def __init__(self, etat_partie, longueur_grille, largeur_grille, grille, nb_bombe):
        """Constructeur de la classe Grille.

        Parameters
        ----------
        etat_partie : str
            renseigne sur l'état de la partie. 3 etats possibles: 'non_fini', 'fini' et 'erreur'
        longueur_grille : int
            plus grand coté de la grille (= nb de colonnes)
        largeur_grille : int
            plus petit coté de la grille (= nb de lignes)
        grille : Grille
            grille de la partie
        nb_bombe : int
            nombre de bombes placé dans la grille
        """
        self.longueur_grille = longueur_grille
        self.largeur_grille = largeur_grille
        self.grille = grille
        self.etat_partie = "non_fini"
        
    def __str__(self):
        """Fonction qui permet de réaliser l'affichage de la grille dans la console.
        """
        result = ' '
        #entete:
        for j in range (self.longueur_grille):
            result += '--'
        result += '-----\n   '
        for j in range (self.longueur_grille):
            result += ' ' + str(j%10)
        result += '   y\n   '
        for j in range (self.longueur_grille):
            result += '__'
        result += '\n'
        for i in range (self.largeur_grille):
            result += str(i%10) + ' |'
            for j in range (self.longueur_grille):
                case = self.grille[i][j]
                result += ' '
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
        #Pied de page
        result += '\nx\n'
        for j in range (self.longueur_grille):
            result += '--'
        result += '-----\n'
                    
        return result
        
        
    def decouvrir_case(self,x,y,action):
        """Fonction qui demande et réalise l'action que veut faire le joueur 
        (marquer/démarquer ou découvrir une case). C'est dans cette dernière qu'est géré la récursivité
        de la fonction découverte sur une case vide.

        Parameters
        ----------
        x : int
            coordonnée de cette case: lignes
        y : int
            coordonnée de cette case: colonnes
        action : string
            action que le joueur veut réaliser. Cela peut être soit m pour marquer/démarquer une case soit d 
            pour découvrir. Pour tout autre saisie par le joueur, l'action découverte sera réalisé.
        """
        case = self.grille[x][y]
        if action == 'm':
            case.marquer()
        else:
            if case.etat != "marquee":
                case.decouvrir()
                if isinstance(case, Vide):                
                    for i in range (x-1,x+2):
                        for j in range (y-1,y+2):
                            if 0 <= i < self.largeur_grille and 0 <= j < self.longueur_grille and self.grille[i][j].etat == "cachee":
                                self.decouvrir_case(i,j,'d')
                    
    
    def test_fin(self):
        """Fonction qui permet de changer l'état de la partie s'il y a une erreur ou si la grille est finie.
        """
        for i in range (self.largeur_grille):
            for j in range (self.longueur_grille):
                case = self.grille[i][j]
                if isinstance(case, Bombe) and case.etat == "decouvert":
                    self.etat_partie = "erreur"
                    return
        for i in range (self.largeur_grille):
            for j in range (self.longueur_grille):
                case = self.grille[i][j]
                if not isinstance(case, Bombe) and case.etat == "cachee":
                    self.etat_partie = "non_fini"
                    return
        self.etat_partie = "fini"