#from pygameframe import * 
import pygame, sys, os
from display_components import *
import time
import numpy as np

clock = pygame.time.Clock()
speech_bubble = pygame.image.load(os.path.join("Images", "SpeechBubble2.png"))
crack_counter = np.zeros(12).reshape(4,3)
crack_side = 45

tuch_pushed = False
vase_cracked = False
klappe_open = False
display_open = False

def open_door_1(game_screen):

    background = pygame.image.load(os.path.join("Images", "bathroom.jpg")).convert()
    game_screen.blit(background, (0, 0))
    pygame.display.update()

    game_screen.blit(speech_bubble, (150,450))

    smallText = pygame.font.Font("pokemon.ttf",20)
    textSurf, textRect = text_objects('That is my old bathroom ?!', smallText)
  
    textRect.bottomleft = ( (200,500) )
    game_screen.blit(textSurf, textRect)
    pygame.display.update()

def crack_wall(game_screen, x, y):
    global crack_counter

    print(crack_counter)
    wall_crack = pygame.image.load(os.path.join("Images", "crack.png"))
    #background = pygame.image.load(os.path.join("Images", "bathroom.jpg")).convert()
    #game_screen.blit(background, (0, 0))
    #game_screen.fill(white)
    #game_screen.blit(background, (0, 0))
    
    for i in range(3):
        for j in range(4):
            if x+45 > 451+((i+1)*45) > x and y+45 > 183+((j+1)*45) > y:
                game_screen.blit(wall_crack, (451+(i*45),183+(j*45)))
                crack_counter[j][i] = 1

    if crack_counter.all() == 1:
        print("CONGRATS YOU CRACKED ALL!")
        #TODO: open the door 
        bath_door = pygame.image.load(os.path.join("Images", "bathroom_door.png"))
        game_screen.blit(bath_door,(447,177))
        return True

    return False

def open_backroom(game_screen):

    
    background = pygame.image.load(os.path.join("Images", "backroom2.png")).convert()
    game_screen.blit(background, (0, 0))
    
        
    
    # pygame.display.update()

    #game_screen.blit(speech_bubble, (150,450))

    #textSurf, textRect = text_objects('I used to hide here as a child... what the f are so many red balls here?', smallText)
  
    #textRect.bottomleft = ( (200,500) )
    #game_screen.blit(textSurf, textRect)

    board_width = 124*3
    board_height = 84*3
    if not display_open:
        board = pygame.image.load(os.path.join("Images", "board.png")).convert()
        game_screen.blit(board, (313, 44))

        smallText = pygame.font.Font("pokemon.ttf",20)     
        textSurf, textRect = text_objects('Please enter the right code:', smallText)    
        textRect.bottomleft = ( (370,90) )
        game_screen.blit(textSurf, textRect)

    
        input_rect = pygame.Rect(450, 130, 100, 30)
        pygame.draw.rect(game_screen, (170,170,170), input_rect)

    if not tuch_pushed:
        tuch = pygame.image.load(os.path.join("Images", "t.png")).convert_alpha()
        game_screen.blit(tuch, (50, 158))
    else:
        tuch = pygame.image.load(os.path.join("Images", "tuch_pushed.png")).convert_alpha()
        game_screen.blit(tuch, (50, 158))

    vase = pygame.image.load(os.path.join("Images", "vase.png")).convert_alpha()
    vase = pygame.transform.scale(vase, (90, 87))

    if not vase_cracked:
        game_screen.blit(vase, (805, 118))

    if klappe_open:
        klappe = pygame.image.load(os.path.join("Images", "klappe.png")).convert_alpha()
        game_screen.blit(klappe, (310, 316))



def crack_vase(game_screen):
    global vase_cracked
    vase_cracked = True
    open_backroom(game_screen)

def open_klappe(game_screen):
    global klappe_open
    klappe_open = True
    open_backroom(game_screen)

def push_tuch(game_screen):
    global tuch_pushed
    tuch_pushed = True
    open_backroom(game_screen)

def open_display(game_screen):
    global display_open
    display_open = True
    open_backroom(game_screen)
    

    
