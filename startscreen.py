import pygame, os
from display_components import *

# this function displays the startscreen
def open_startscreen(game_screen):

    background = pygame.image.load(os.path.join("Images", "start.png")).convert()
    game_screen.blit(background, (0, 0))
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


# the room '3doors will be opened if the user clicked on start
def open_3doors(game_screen, simulate_push = True):


    if simulate_push:
        # simulate a click on the button
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
    game_screen.blit(speech_bubble, (speech_bubble_x,speech_bubble_y))
    textSurf, textRect = text_objects('Wait... How did I get HERE?! Am I dreaming? That is my old house.', smallText)
    textRect.bottomleft = ( (200,500) )
    game_screen.blit(textSurf, textRect)
    textSurf, textRect = text_objects('But wait... where is Emma? I should go find her.', smallText)
    textRect.bottomleft = ( (200,520) )
    game_screen.blit(textSurf, textRect)

def open_story(game_screen):

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
