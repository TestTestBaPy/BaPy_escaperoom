import pygame, os
from display_components import *

rustle = pygame.mixer.Sound('Sounds/Meeresrauschen.wav')
pygame.mixer.Sound.set_volume(rustle, 0.3)
rustle.play()


def open_startscreen(simulate_push = False):
    """Opens i.e. displays the startscreen"""  
    global rustle

    set_current_room("STRT")
    if simulate_push:
        background = pygame.image.load(os.path.join("Images", "start_pushstart.png")).convert()
        game_screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(2)

    game_screen.blit(pygame.image.load(os.path.join("Images", "start.png")).convert(), (0, 0))

    # Display game instructions
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
      simulate_push:
        If True simulates a push on the prior "START" button
    """
    global rustle

    rustle.stop()
    # Simulate a click on the startbutton
    open_startscreen(simulate_push = simulate_push)

    # Set the current room
    set_current_room("DOOR")

    # Load the new room
    background = pygame.image.load(os.path.join("Images", "3doors.png")).convert()
    game_screen.blit(background, (0, 0))

    # Load speechbubble with text
    game_screen.blit(speech_bubble, (SPEECH_BUBBLE_X,SPEECH_BUBBLE_Y))
    textSurf, textRect = text_objects('Where is my Emma? I need to find her. How dare she leave me alone!', smallText)
    textRect.bottomleft = ((200, 510))
    game_screen.blit(textSurf, textRect)
    textSurf, textRect = text_objects("My parents' house is so big, where should I start?", smallText)
    textRect.bottomleft = ((200, 530))
    game_screen.blit(textSurf, textRect)


def open_story():
    """Opens i.e. displays the backhround information on this game"""
    pygame.mixer.Sound.play(button_pushed)
    # Set the current room
    set_current_room("STRY")
    
    # Simulate a click on the button
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