from jeuxDeCarte import tirage
import random
class Ia:
    def __init__(self):
        self.turn = False
        self.compte = 0

    def iaPlay(self):
        if self.compte >= 12 and self.compte <= 20:
            rand = random.randint(1,2)
            if rand == 1:
                self.tirage()
            else:
                self.turn = False
        elif self.compte >= 0 and self.compte < 12:
            self.tirage()
        else:
            self.turn = False
    
    def iaReplay(self, playerStop):
        if playerStop == None:
            self.compte = 0

    def tirage(self):
        carte, valeur = tirage()
        print("La banque tire " + carte)
        self.compte += valeur
        print("score : {}".format(self.compte))
