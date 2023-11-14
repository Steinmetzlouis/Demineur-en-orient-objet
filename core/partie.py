import numpy as np
from case_bombe import Bombe
from case_vide import Vide
from case_voisin import Voisin
from grille import Grille

class Partie(object):
    """Classe définissant la partie de démineur.
    
    Attributes
    ----------
    difficulte : str
        difficulté de la partie, définit la taille de la grille et le nombre de bombe. 4 disponibles: 'test', 
        'facile', 'moyen', 'difficile'
    nb_bombe : int
        nombre de bombes à placer dans la grille
    longueur_grille : int
        plus grand coté de la grille (= nb de colonnes)
    largeur_grille : int
        plus petit coté de la grille (= nb de lignes)
    etat_partie : str
        renseigne sur l'état de la partie. 3 etats possibles: 'non_fini', 'fini' et 'erreur'
    magrille : Grille
        Grille de la partie
    """
    def __init__(self):
        """Constructeur de la classe Partie.
        """
        self.difficulte = "test"
        self.nb_bombe = 2
        self.longueur_grille = 4
        self.largeur_grille = 4
        
        self.etat_partie = "non_fini"
        
    
    def choix_difficulte(self, difficulte):
        """Fonction qui modifie la difficulté de la partie.

        Parameters
        ----------
        difficulte : str
            difficulté de la partie, définit la taille de la grille et le nombre de bombe. 4 disponibles: 'test', 
            'facile', 'moyen', 'difficile'
        """
        self.difficulte = difficulte
        
    
    def creation_grille(self):
        """Fonction qui permet de construire et retourner une grille en fonction de la taille de la grille 
        et du nombre de bombes voulu.

        Returns
        -------
        Grille
            Grille de la partie
        """
        grille = np.zeros((self.largeur_grille, self.longueur_grille)).tolist()
        
        B = []
        array_bombe = np.random.choice(self.longueur_grille*self.largeur_grille, self.nb_bombe, replace=False)
        for b in array_bombe:
            ligne = b // self.longueur_grille
            colonne = b % self.longueur_grille
            grille[ligne][colonne] = Bombe(ligne, colonne)
            B.append((ligne,colonne))
            
        for b in B:
            for i in range (b[0]-1, b[0]+2):
                for j in range (b[1]-1, b[1]+2):
                    if 0 <= i < self.largeur_grille and 0 <= j < self.longueur_grille:
                        if not isinstance(grille[i][j], Bombe):
                            grille[i][j] += 1
                    
        for i in range (self.largeur_grille):
            for j in range (self.longueur_grille):
                if not isinstance(grille[i][j],Bombe):
                    if grille[i][j] == 0:
                        grille[i][j] = Vide(i,j)
                    
                    else:
                        nb_voisin = int(grille[i][j])
                        grille[i][j] = Voisin(i,j,nb_voisin)
        
        return grille
        
        
    def debut_partie(self):
        """Fonction qui permet de créer la grille de la partie en fonction de la difficulté souhaité.
        """
        if self.difficulte == "test":
            self.nb_bombe = 2
            self.longueur_grille = 4
            self.largeur_grille = 4
            
        if self.difficulte == "facile":
            self.nb_bombe = 10
            self.longueur_grille = 10
            self.largeur_grille = 8
        
        elif self.difficulte == "moyen":
            self.nb_bombe = 40
            self.longueur_grille = 18
            self.largeur_grille = 15
        
        elif self.difficulte == "difficile":
            self.nb_bombe = 99
            self.longueur_grille = 24
            self.largeur_grille = 20
            
        
        self.magrille = Grille(self.etat_partie, self.longueur_grille, self.largeur_grille, self.creation_grille(), self.nb_bombe)
        
            
    def marquer_case(self):
        """Fonction qui permet au joueur de saisir les coordonnées de la case 
        sur laquelle il veut agir, et séléctionne l'action à réaliser (marquer ou découvrir).
        Test aussi l'etat de la partie et met à jour ce dernier (etat_partie).
        """
        print('x: ')
        x = int(input())
        print('y: ')
        y = int(input())
        print('action (m ou d): ')
        action = input()
           
        if 0 <= x < self.largeur_grille and 0 <= y < self.longueur_grille:
            self.magrille.decouvrir_case(x,y, action)
            self.magrille.test_fin()
        else:
            print('Case hors grille')
        print(self.magrille)
        
    
    def jouer(self):
        """Fonction qui affiche la grille, et qui continue de proposer au joueur de jouer tant 
        que la condition de fin n'est pas réalisée. Si elle est atteinte, mets fin à la partie.
        """
        print(self.magrille)
        while self.magrille.etat_partie == "non_fini":
            self.marquer_case()
        if self.magrille.etat_partie == "fini":
            #stop chrono
            print("Bravo")
        elif self.magrille.etat_partie== "erreur":
            print("Echec")
            
            
if __name__ == "__main__":
    partie = Partie()
    
    print('choix difficulte (facile, moyen, difficile): ')
    difficulte = input()
    
    partie.choix_difficulte(difficulte)
    
    partie.debut_partie()
    partie.jouer()