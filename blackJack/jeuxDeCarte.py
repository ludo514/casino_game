import random
import pygame
jeux = {
    "trefle": {
        1: {"nom": "As Trefle","valeur": 1},
        2: {"nom": "2 Trefle","valeur": 2},
        3: {"nom": "3 Trefle","valeur": 3},
        4: {"nom": "4 Trefle","valeur": 4},
        5: {"nom": "5 Trefle","valeur": 5},
        6: {"nom": "6 Trefle","valeur": 6},
        7: {"nom": "7 Trefle","valeur": 7},
        8: {"nom": "8 Trefle","valeur": 8},
        9: {"nom": "9 Trefle","valeur": 9},
        10: {"nom": "10 Trefle","valeur": 10},
    },
    "coeur":{
        1: {"nom": "As Coeur","valeur": 1},
        2: {"nom": "2 Coeur","valeur": 2},
        3: {"nom": "3 Coeur","valeur": 3},
        4: {"nom": "4 Coeur","valeur": 4},
        5: {"nom": "5 Coeur","valeur": 5},
        6: {"nom": "6 Coeur","valeur": 6},
        7: {"nom": "7 Coeur","valeur": 7},
        8: {"nom": "8 Coeur","valeur": 8},
        9: {"nom": "9 Coeur","valeur": 9},
        10: {"nom": "10 Coeur","valeur": 10},
    },
    "carreau": {
        1: {"nom": "As Carreau","valeur": 1},
        2: {"nom": "2 Carreau","valeur": 2},
        3: {"nom": "3 Carreau","valeur": 3},
        4: {"nom": "4 Carreau","valeur": 4},
        5: {"nom": "5 Carreau","valeur": 5},
        6: {"nom": "6 Carreau","valeur": 6},
        7: {"nom": "7 Carreau","valeur": 7},
        8: {"nom": "8 Carreau","valeur": 8},
        9: {"nom": "9 Carreau","valeur": 9},
        10: {"nom": "10 Carreau","valeur": 10},
    },
    "pique": {
        1: {"nom": "As Pique","valeur": 1},
        2: {"nom": "2 Pique","valeur": 2},
        3: {"nom": "3 Pique","valeur": 3},
        4: {"nom": "4 Pique","valeur": 4},
        5: {"nom": "5 Pique","valeur": 5},
        6: {"nom": "6 Pique","valeur": 6},
        7: {"nom": "7 Pique","valeur": 7},
        8: {"nom": "8 Pique","valeur": 8},
        9: {"nom": "9 Pique","valeur": 9},
        10: {"nom": "10 Pique","valeur": 10},
    }
}

def tirage():
    dic = jeux
    tab = ["trefle", "coeur", "carreau", "pique"]
    randForme = random.randint(0,3)
    randCarte = random.randint(1,10)
    forme = tab[randForme]
    carteNom = dic[forme][randCarte]["nom"]
    valeur = dic[forme][randCarte]["valeur"]

    return carteNom, valeur