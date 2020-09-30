from jeuxDeCarte import tirage

class Player:
    def __init__(self, sommeTotal):
        self.someTotal = int(sommeTotal)
        self.compte = 0
        self.turn = True
        self.choix = ""
        self.misePlayer = 0

    def statusSomme(self):
        print("Banque: {}".format(self.someTotal))

    def mise(self, mise):
        self.misePlayer = mise
        self.someTotal -= self.misePlayer
    
    def play(self):
        print("Votre tour")
        self.choix = input("Tirer = 1 / Garder = 2 : ")
        if self.choix == "1":
            self.playerTirage()
        else:
            self.turn = False

    def outOfMoney(self):
        if(self.someTotal < 5):
            print("Vous n'avez plus assez pour miser")
            return True
        else:
            return False
    
    def playerTirage(self):
        carte, valeur = tirage()
        print("Vous avez tirez " + carte)
        self.compte += valeur
        print("score : {}".format(self.compte))
    

    def winOrNot(self, iaCompte):
        iaDiff = 21 - iaCompte
        playerDiff = 21 - self.compte
        if iaDiff < playerDiff:
            self.playerWin(2)
        elif iaDiff == playerDiff:
            self.playerWin(1)
        elif playerDiff == 0:
            self.playerWin(3)
        else:
            print("Vous avez perdu votre mise de {}".format(self.misePlayer))
            choixContinue = input("Voulez vous remisé ? O/N : ")
            if choixContinue == "O":
                self.mise2()
                self.compte = 0
                self.turn = True
            elif choixContinue == "N":
                return True

    def mise2(self):
        miseJoueur = input("Mise minimum 5 euros, palier de 5, 5/10/15/20/25 : ")
        print("mise de " + miseJoueur + " euros")
        self.mise(int(miseJoueur))

    def playerWin(self, multiple):
        self.multiplicateur(multiple)
        self.statusSomme()
        choixContinue = input("Voulez vous remisé ? O/N : ")
        if choixContinue == "O":
            self.mise2()
            self.compte = 0
            self.turn = True
        elif choixContinue == "N":
            return True
    
    def multiplicateur(self, multiple):
        switch = {
            1:"Vous gagnez votre mise {}".format(self.misePlayer*multiple),
            2:"Vous gagnez le double de votre mise {}".format(self.misePlayer*multiple),
            3:"BlackJack !! Vous gagnez le triple de votre mise {}".format(self.misePlayer*multiple)
        }
        print(switch[multiple])
        self.someTotal += self.misePlayer * multiple