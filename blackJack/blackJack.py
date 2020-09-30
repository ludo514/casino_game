import pygame
from player import Player
from ia import Ia
from Game import Game

if __name__ == "__main__":
    
    LARGEUR = 640
    HAUTEUR = 480
    FPS = 60

    # couleur
    WHITE = (255, 255, 255)
    GREEN = (0, 147, 73)

    # initialisation de pygame et création de la fenêtre
    pygame.init()
    screen = pygame.display.set_mode((LARGEUR, HAUTEUR))

    pygame.display.set_caption("BlacJack")#nom de la fenêtre
    clock = pygame.time.Clock()
    police = pygame.font.SysFont("comicsansms", 30, 1)
    game = Game(screen)
    
    #miseJoueur = input("Mise minimum 5 euros, palier de 5, 5/10/15/20/25 : ")
    #print("mise de " + miseJoueur + " euros")
    #player.mise(int(miseJoueur))
    #player.statusSomme()
    #print("===================================")
    
    launched = True
    stop = False
    while launched:

        clock.tick(FPS)
        # récupération d'un event

        for event in pygame.event.get():
            #
            if event.type == pygame.QUIT:
                launched = False

        #if player.outOfMoney() == False and stop != True:
            #if player.turn == True:
                #player.play()
                #print("===================================")
                #player.statusSomme()
                #bank.turn = True
            #elif bank.turn == True:
                #print("Tour de la banque")
                #bank.iaPlay()
                #print("===================================")
                #time.sleep(1)
            #else:
                #stop = player.winOrNot(bank.compte)
                #bank.iaReplay(stop)
        
        screen.fill(GREEN)
        game.draw()
        pygame.display.flip()

pygame.quit()

