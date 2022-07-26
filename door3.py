import pygame, os, time
from display_components import *
from startscreen import *


def open_door_3():
    """Opens the mysterious door
    """
    game_screen.blit(pygame.image.load(os.path.join("Images", "mysteryroom.png")).convert(), (0, 0))
    textSurf, textRect = text_objects('I should not.. go... here...?!', smallText)
    textRect.bottomleft = ((200, 520))
    game_screen.blit(textSurf, textRect)

    pygame.display.update()
    time.sleep(1)
    open_3doors(False)