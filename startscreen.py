import pygame, os
from display_components import *

# this function displays the startscreen
def open_startscreen():

    # set the current room
    set_current_room("STRT")
    

    # display background
    background = pygame.image.load(os.path.join("Images", "start.png")).convert()
    game_screen.blit(background, (0, 0))

    # display game instructions
    input_rect = pygame.Rect(600, 450, 300, 100)
    pygame.draw.rect(game_screen, (235,235,235), input_rect)
    textSurf, textRect = text_objects("How to play?", smallText)
    textRect.bottomleft = ( (600 + 5, 450 + 25) )
    game_screen.blit(textSurf, textRect)  
    textSurf, textRect = text_objects("Click on 'START' to start the game.", smallText)
    textRect.bottomleft = ( (600 + 5, 450 + 55) )
    game_screen.blit(textSurf, textRect)
    textSurf, textRect = text_objects("and on 'STORY' to get background.", smallText)
    textRect.bottomleft = ( (600 + 5, 450 + 85) )
    game_screen.blit(textSurf, textRect)


def open_3doors(simulate_push = True):

    # set the current room
    set_current_room("DOOR")

    if simulate_push:
        # simulate a click on the startbutton
        background = pygame.image.load(os.path.join("Images", "start_pushstart.png")).convert()
        game_screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(2)

        background = pygame.image.load(os.path.join("Images", "start.png")).convert()
        game_screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(2)

    # load the new room
    background = pygame.image.load(os.path.join("Images", "3doors.jpg")).convert()
    game_screen.blit(background, (0, 0))

    # load speechbubble with text
    game_screen.blit(speech_bubble, (speech_bubble_x,speech_bubble_y))
    textSurf, textRect = text_objects('Where is my Emma? I need to find her. How dare she leave me alone!', smallText)
    textRect.bottomleft = ( (200,510) )
    game_screen.blit(textSurf, textRect)
    textSurf, textRect = text_objects("My parents' house is so big, where should I start?", smallText)
    textRect.bottomleft = ( (200,530) )
    game_screen.blit(textSurf, textRect)


def open_story():

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
