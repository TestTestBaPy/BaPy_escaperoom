"""Manages the displaying of the starting screen and opens either the game or the story, if clicked on."""
import pygame, os
from display_components import *

pygame.mixer.Sound.set_volume(RUSTLE, 0.3)
RUSTLE.play()


def open_startscreen(simulate_push = False):
    """Opens i.e. displays the startscreen
    Args:
      simulate_push: if set to True simulate a push on the start button
    """  
    global RUSTLE

    set_current_room("STRT")

    # Simulate a push if it was set to True
    if simulate_push:
        pygame.mixer.Sound.play(BUTTON_PUSHED)
        background = pygame.image.load(os.path.join("Images", "start_pushstart.png")).convert()
        game_screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(2)

    game_screen.blit(pygame.image.load(os.path.join("Images", "start.png")).convert(), (0, 0))

    # Display game instructions
    input_rect = pygame.Rect(600, 450, 300, 100)
    pygame.draw.rect(game_screen, (235, 235, 235), input_rect)
    textSurf = text_objects("How to play?", small_text)
    game_screen.blit(textSurf, (600 + 5, 450 + 5))  
    textSurf = text_objects("Click on 'START' to start the game.", small_text)
    game_screen.blit(textSurf, (600 + 5, 450 + 35))
    textSurf = text_objects("and on 'STORY' to get background.", small_text)
    game_screen.blit(textSurf, (600 + 5, 450 + 65))


def open_3doors(simulate_push = True):
    """Opens i.e. the room with three doors to choose from
    Args: 
      simulate_push: if set to True simulate a push on the start button
    """
    global RUSTLE  

    RUSTLE.stop()
    # Simulate a click on the startbutton
    open_startscreen(simulate_push = simulate_push)

    # Set the current room
    set_current_room("DOOR")

    # Load the new room
    background = pygame.image.load(os.path.join("Images", "3doors.png")).convert()
    game_screen.blit(background, (0, 0))

    # Load speechbubble with text
    game_screen.blit(speech_bubble, (SPEECH_BUBBLE_X,SPEECH_BUBBLE_Y))
    textSurf = text_objects('Where is my Emma? I need to find her. How dare she leave me alone!', small_text)
    game_screen.blit(textSurf, (200, 490))
    textSurf = text_objects("My parents' house is so big, where should I start?", small_text)
    game_screen.blit(textSurf, (200, 510))


def open_story():
    """Opens i.e. displays the background information on this game"""
    pygame.mixer.Sound.play(BUTTON_PUSHED)
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