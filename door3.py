import pygame, os, time
from display_components import *

def open_door_3(game_screen):
    background = pygame.image.load(os.path.join("Images", "mysteryroom.png")).convert()
    game_screen.blit(background, (0, 0))
    textSurf, textRect = text_objects('I should not.. go... here...?', smallText)
    textRect.bottomleft = ( (200,520) )
    game_screen.blit(textSurf, textRect)

    pygame.display.update()
    time.sleep(0.5)

