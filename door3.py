import pygame, os, time
from display_components import *
from startscreen import *


def open_door_3():
    """Opens the mysterious door
    """
    game_screen.blit(pygame.image.load(os.path.join("Sounds", "justmafiathings.jpg")).convert(), (0, 0))
    game_screen.blit(speech_bubble, (speech_bubble_x, speech_bubble_y))
    textSurf, textRect = text_objects('I should not.. go... here...?!', smallText)
    textRect.bottomleft = ((200, 520))
    game_screen.blit(textSurf, textRect)

    pygame.display.update()
    time.sleep(5)
    open_3doors(False)