#from pygameframe import * 
import pygame, sys, os
from display_components import *
import time
import numpy as np


def open_endroom(game_screen):
    background = pygame.image.load(os.path.join("Images", "tresor.png")).convert()
    game_screen.blit(background, (0, 0))
    pygame.display.update()

def zoom_touchpad(game_screen):
    background = pygame.image.load(os.path.join("Images", "tresor.png")).convert()
    game_screen.blit(background, (0, 0))
    pygame.display.update()


 
    #handle_input(game_screen)