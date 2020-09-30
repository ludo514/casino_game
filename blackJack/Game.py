import random
import time
from player import Player
from ia import Ia
import pygame

GREY = (192, 192, 192)
YELLOW = (226, 221, 10)
BLACK = (0, 0, 0)
class Game(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.sommeJoueur = 200
        self.player = Player(self.sommeJoueur)
        self.screen = screen
        self.bank = Ia()
        self.police = pygame.font.SysFont("comicsansms", 30, 0)
    def update(self):
        pass


    def draw(self):
        pygame.draw.rect(self.screen, GREY, (520, 0, 120, 480))
        pygame.draw.rect(self.screen, YELLOW, (520, 10, 120, 50))
        pygame.draw.rect(self.screen, YELLOW, (520, 70, 120, 50))
        tirer = self.police.render("Tirer", True, BLACK)
        tirer = self.police.render("Tirer", True, BLACK)
        self.screen.blit(tirer, [540,17])