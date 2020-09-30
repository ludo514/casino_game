import random

roulette = {
    1 : [0, "vert"],
    2 : [32, "rouge"],
    3 : [15, "noir"],
    4 : [4, "rouge"],
    5 : [21, "noir"],
    6 : [2, "rouge"],
    7 : [25, "noir"],
    8 : [17, "rouge"],
    9 : [34, "noir"],
    10 : [6, "rouge"],
    11 : [27, "noir"],
    12 : [13, "rouge"],
    13 : [36, "noir"],
    14 : [11, "rouge"],
    15 : [30, "noir"],
    16 : [8, "rouge"],
    17 : [23, "noir"],
    18 : [10, "rouge"],
    19 : [5, "noir"],
    20 : [24, "rouge"],
    21 : [16, "noir"],
    22 : [33, "rouge"],
    23 : [1, "noir"],
    24 : [20, "rouge"],
    25 : [14, "noir"],
    26 : [31, "rouge"],
    27 : [9, "noir"],
    28 : [22, "rouge"],
    29 : [18, "noir"],
    30 : [29, "rouge"],
    31 : [7, "noir"],
    32 : [28, "rouge"],
    33 : [12, "noir"],
    34 : [35, "rouge"],
    35 : [3, "noir"],
    36 : [26, "rouge"]
}
#while i < 2:
#    while tour < 5:
#        nombre = random.choice(roulette)
#        tour += 1
#        if nombre >= 13 and nombre <= 34:
#            compteGagant += 1
#            banque += mise * 3
#            print("{} | Gagnant nombre : {} | banque : {}".format(tour, nombre, banque))
#        else:
#            banque -= 10
#            comptePerdant += 1
#            print("{} | Perdant nombre : {}| banque : {}".format(tour, nombre, banque))
#        if nombre == 0:
#            compteZéro += 1
#    print("============================================================================")
#    print("nombre de coup gagnant : {}| nombre de coup perdant {}| résultat banque: {} | nombre de zéro sortie : {}".format(compteGagant, comptePerdant, banque, compteZéro))
#    i += 1
#    
#    with open('resultatRoulette.txt', 'w') as fichier:
#        if banque <= 5:
#            tableauResultat.append("\nPerdant")
#        else:
#            totalGagne += banque - 20
#            tableauResultat.append("\nGagnant | banque : {}".format(str(banque)))
#        for tabl in tableauResultat:
#            fichier.write("{}".format(tabl))
#        fichier.write("\nTotal gagner sur 3 parties : {}".format(str(totalGagne)))
#        
#    if banque <= 5:
#        banque = 20
#    else:
#        banque = banque - 20
#
#    tour = 0


def game():

    continuer = True
    while continuer == True:
        choix = choixRoulette()
        if choix == "1":
            rouletteManu()
        if choix == "2":
            simuRoulette()
        if choix == "3":
            continuer = False


def rouletteManu():
    choix = True
    banque = input(" Mettez le montant à mettre en banque : ")
    while banque != 0 or choix != False:
        print(" Mettez votre mise 5, 10, 20 , 50, 100")
        mise = input("Mise : ")
        tabMise = stringToDict(mise)
        print("Roullette lancé !!")
        chiffreTire = roulette[random.randint(0,36)]


def simuRoulette():
    pass

def stringToDict(mise):
    tab = mise.split(" ")
    return tab

def winOrLose(roulette):
    pass

def choixRoulette():
    print("1 : Roulette normale")
    print("2 : Roulette simulation")
    print("3 : Quittez")
    choix = input("Choix : ")

    return choix

game()