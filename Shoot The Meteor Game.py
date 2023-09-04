import pygame
import random
from os import path

from pygame.sprite import Group

img_dir = path.join(path.dirname(__file__), 'imgs')
snd_dir = path.join(path.dirname(__file__), 'snd')
pygame.init()
pygame.display.set_caption("Shoot the Meteor")
clock = pygame.time.Clock()
width = 400
height = 600
FPS = 30
screen = pygame.display.set_mode([width,height])
MAGENTA = (220,20,60)
PURPLE = (138,43,226)
CYAN = (0,255,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,height/2)
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(BLACK)
    pygame.display.flip()
pygame.quit()








