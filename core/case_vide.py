from case import Case

class Bombe(Case):
    def decouvrir(self):
        for i in range (self.x - 1, self.x + 1):
            for j in range (self.y - 1, self.y + 1):
                