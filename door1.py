#from pygameframe import * 
import pygame, sys, os
from display_components import *
import time

clock = pygame.time.Clock()
speech_bubble = pygame.image.load(os.path.join("Images", "SpeechBubble2.png"))

def open_door_1(game_screen):


    background = pygame.image.load(os.path.join("Images", "bathroom.jpg")).convert()
    game_screen.blit(background, (0, 0))
    pygame.display.update()

    game_screen.blit(speech_bubble, (150,450))

    smallText = pygame.font.Font("pokemon.ttf",20)
    #smallText = pygame.font.SysFont('ARCADECLASSIC.ttf', 20)
    textSurf, textRect = text_objects('That is my old bathroom ?!', smallText)
    #textRect.left
    # clock.tick(2)
    # 
    
    
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
