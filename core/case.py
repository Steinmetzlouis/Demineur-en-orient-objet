class Case(object):
    def __init__(self, x, y):
        self.etat = "cachee"
        self.x = x
        self.y = y
    
    
    def marquer(self):
        if self.etat == "cachee":
            self.etat = "marquee"
        
        elif self.etat == "marquee":
            self.etat = "cachee"
            
            
    def decouvrir(self):
        raise NotImplementedError()