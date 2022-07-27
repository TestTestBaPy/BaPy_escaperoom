import pygame, os, time
from display_components import *
from startscreen import *


def open_door_3():
    """Opens the mysterious door
    """
    game_screen.blit(pygame.image.load(os.path.join("Sounds", "justmafiathings.jpg")).convert(), (0, 0))
    game_screen.blit(speech_bubble, (SPEECH_BUBBLE_X, SPEECH_BUBBLE_Y))
    textSurf = text_objects('I should not..go... here..?! Um..I did not see anything.', small_text)
    game_screen.blit(textSurf, (200, 520))

    pygame.display.update()
    time.sleep(3)
    open_3doors(False)