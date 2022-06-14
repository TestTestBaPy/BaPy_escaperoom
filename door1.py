#from pygameframe import * 
import pygame, sys, os
from display_components import *
import time
import numpy as np

clock = pygame.time.Clock()
speech_bubble = pygame.image.load(os.path.join("Images", "SpeechBubble2.png"))
crack_counter = np.zeros(12).reshape(4,3)
crack_side = 45

def open_door_1(game_screen):

    # smallText = pygame.font.Font("pokemon.ttf",20)
    # textSurf, textRect = text_objects(msg, smallText)
    # textRect.center = ( (x+(w/2)), (y+(h/2)) )
    # game_screen.blit(textSurf, textRect)


    background = pygame.image.load(os.path.join("Images", "bathroom.jpg")).convert()
    game_screen.blit(background, (0, 0))
    pygame.display.update()

    game_screen.blit(speech_bubble, (150,450))

    smallText = pygame.font.Font("pokemon.ttf",20)
    textSurf, textRect = text_objects('That is my old bathroom ?!', smallText)
  
    textRect.bottomleft = ( (200,500) )
    game_screen.blit(textSurf, textRect)
    pygame.display.update()
    # clock.tick(2)
    # #time.sleep(3)

    # textSurf, textRect2 = text_objects('But wait where is my little sister Emma...?', smallText)
    # textRect2.bottomleft = ( (200,520) )
    # game_screen.blit(textSurf, textRect2)
    # pygame.display.update()

    #game_screen.fill((0,0,0))

def crack_wall(game_screen, x, y):
    global crack_counter

    print(crack_counter)
    wall_crack = pygame.image.load(os.path.join("Images", "crack.png"))
    #background = pygame.image.load(os.path.join("Images", "bathroom.jpg")).convert()
    #game_screen.blit(background, (0, 0))
    #game_screen.fill(white)
    #game_screen.blit(background, (0, 0))
    if crack_counter.all() == 1:
        print("CONGRATS YOU CRACKED ALL!")
        #TODO: open the door 
        sys.exit()

    for i in range(3):
        for j in range(4):
            if x+45 > 451+((i+1)*45) > x and y+45 > 183+((j+1)*45) > y:
                game_screen.blit(wall_crack, (451+(i*45),183+(j*45)))
                crack_counter[j][i] = 1
    
    #pygame.display.flip()
    
