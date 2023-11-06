import numpy as np
import random
from case_bombe import Bombe
from case_vide import Vide
from case_voisin import Voisin
from grille import Grille

class Partie(object):
    def __init__(self):
        self.difficulte = "moyen"
        self.nb_bombe = 40
        self.longueur_grille = 18
        self.largeur_grille = 15
        
        self.grille_devoilee = False
        
    
    def choix_difficulte(self, difficulte):
        self.difficulte = difficulte
        
    
    def creation_grille_array(self):
        grille = np.zeros(self.largeur_grille, self.longueur_grille)
        
        B = []
        array_bombe = random.choice(self.longueur_grille*self.largeur_grille, size=self.nb_bombe, replace=False)
        for b in array_bombe:
            ligne = b // self.longueur_grille
            colonne = b % self.longueur_grille
            grille[ligne, colonne] = Bombe(ligne, colonne)
            B.append((ligne,colonne))
            
        for b in B:
            for i in range (b[0]-1, b[0]+1):
                for j in range (b[1]-1, b[1]+1):
                    grille[i,j] += 1
                    
        for i in range (self.largeur_grille):
            for j in range (self.longueur_grille):
                if not isinstance(grille[i,j],Bombe):
                    if grille[i,j] == 0:
                        grille[i,j] = Vide(i,j)
                    
                    else:
                        nb_voisin = grille[i,j]
                        grille[i,j] = Voisin(i,j,nb_voisin)
        
        return grille
        
        
    def debut_partie(self):
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
            
        
        self.magrille = Grille(self.longueur_grille, self.largeur_grille, self.creation_grille_array(), self.nb_bombe)
        
            
            
    
    # def fin_partie(self):
    #     if self.grille_devoilee == True:
    #         #stop chrono
            