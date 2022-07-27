import pygame, os
from display_components import *

rauschen = pygame.mixer.Sound('Sounds/Meeresrauschen.wav')
pygame.mixer.Sound.set_volume(rauschen, 0.3)
rauschen.play()


def open_startscreen(simulate_push = False):
    """Opens i.e. displays the startscreen
    """  
    global rauschen

    set_current_room("STRT")
    if simulate_push:
        background = pygame.image.load(os.path.join("Images", "start_pushstart.png")).convert()
        game_screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(2)

    game_screen.blit(pygame.image.load(os.path.join("Images", "start.png")).convert(), (0, 0))

    # display game instructions
    input_rect = pygame.Rect(600, 450, 300, 100)
    pygame.draw.rect(game_screen, (235, 235, 235), input_rect)
    textSurf, textRect = text_objects("How to play?", smallText)
    textRect.bottomleft = ((600 + 5, 450 + 25))
    game_screen.blit(textSurf, textRect)  
    textSurf, textRect = text_objects("Click on 'START' to start the game.", smallText)
    textRect.bottomleft = ((600 + 5, 450 + 55))
    game_screen.blit(textSurf, textRect)
    textSurf, textRect = text_objects("and on 'STORY' to get background.", smallText)
    textRect.bottomleft = ((600 + 5, 450 + 85))
    game_screen.blit(textSurf, textRect)


def open_3doors(simulate_push = True):
    """Opens i.e. the room with three doors to choose from
        Args: 
            simulate_push if True simulates a push on the prior "START" button
    """
    global rauschen

    rauschen.stop()
    # simulate a click on the startbutton
    open_startscreen(simulate_push = simulate_push)

    # set the current room
    set_current_room("DOOR")

    # load the new room
    background = pygame.image.load(os.path.join("Images", "3doors.png")).convert()
    game_screen.blit(background, (0, 0))

    # load speechbubble with text
    game_screen.blit(speech_bubble, (speech_bubble_x,speech_bubble_y))
    textSurf, textRect = text_objects('Where is my Emma? I need to find her. How dare she leave me alone!', smallText)
    textRect.bottomleft = ((200, 510))
    game_screen.blit(textSurf, textRect)
    textSurf, textRect = text_objects("My parents' house is so big, where should I start?", smallText)
    textRect.bottomleft = ((200, 530))
    game_screen.blit(textSurf, textRect)


def open_story():
    """Opens i.e. displays the backhround information on this game
    """
    pygame.mixer.Sound.play(button_pushed)
    # set the current room
    set_current_room("STRY")
    
    # simulate a click on the button
    background = pygame.image.load(os.path.join("Images", "start_pushstory.png")).convert()
    game_screen.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(2)

    background = pygame.image.load(os.path.join("Images", "start.png")).convert()
    game_screen.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(2)
    
    background = pygame.image.load(os.path.join("Images", "chat.png")).convert()
    game_screen.blit(background, (0, 0))

    