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
    textSurf, textRect = text_objects('Oh, my old bathroom. Even Henry and Odette, the rubber ducks are here.', smallText)
    textRect.bottomleft = ( (190,510) )
    game_screen.blit(textSurf, textRect)

    smallText = pygame.font.Font("pokemon.ttf",20)
    textSurf, textRect = text_objects('Hmph, it seems Emma is not here.', smallText)
    
  
    textRect.bottomleft = ( (190,530) )
    game_screen.blit(textSurf, textRect)

    pygame.display.update()

def crack_wall(game_screen, x, y):
    global crack_counter

    print(crack_counter)
    wall_crack = pygame.image.load(os.path.join("Images", "crack.png"))
    
    for i in range(3):
        for j in range(4):
            if x+45 > 451+((i+1)*45) > x and y+45 > 183+((j+1)*45) > y:
                game_screen.blit(wall_crack, (451+(i*45),183+(j*45)))
                crack_counter[j][i] = 1

    if crack_counter.all() == 1:
        bath_door = pygame.image.load(os.path.join("Images", "bathroom_door.png"))
        game_screen.blit(bath_door,(447,177))
        return True

    return False

def open_backroom(game_screen):

    background = pygame.image.load(os.path.join("Images", "backroom2.png")).convert()
    game_screen.blit(background, (0, 0))
    
    board_width = 124*3
    board_height = 84*3

    if klappe_open:
        klappe = pygame.image.load(os.path.join("Images", "klappe.png")).convert_alpha()
        game_screen.blit(klappe, (310, 316))

    # if the display is not open the code was not entered correctly
    if not display_open:
        
        
        board = pygame.image.load(os.path.join("Images", "board.png")).convert()
        game_screen.blit(board, (313, 44))

        smallText = pygame.font.Font("pokemon.ttf",20)     
        textSurf, textRect = text_objects('Please enter the right code: ', smallText)    
        textRect.bottomleft = ( (370,90) )
        game_screen.blit(textSurf, textRect)

        smallText = pygame.font.Font("pokemon.ttf",20)     
        textSurf, textRect = text_objects('(Press enter, when done)', smallText)    
        textRect.bottomleft = ( (380,110) )
        game_screen.blit(textSurf, textRect)

    
        input_rect = pygame.Rect(450, 130, 100, 30)
        pygame.draw.rect(game_screen, (170,170,170), input_rect)

    else:
        game_screen.blit(speech_bubble, (speech_bubble_x,speech_bubble_y))
        smallText = pygame.font.Font("pokemon.ttf",20)
        textSurf, textRect = text_objects("That was correct! I think I'm going crazy, I see numbers everywhere.", smallText)    
        textRect.bottomleft = ( (speech_bubble_x + 50 ,speech_bubble_y + 65) )
        game_screen.blit(textSurf, textRect)
        textSurf, textRect = text_objects('Maybe I should remeber them....', smallText)    
        textRect.bottomleft = ( (speech_bubble_x + 50 ,speech_bubble_y + 85) )
        game_screen.blit(textSurf, textRect)

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

    


# the following functions set the global status-variables to keep track of players actions and display them
def crack_vase(game_screen):
    global vase_cracked
    vase_cracked = True
    open_backroom(game_screen)

def open_klappe(game_screen):
    global klappe_open
    global vase_cracked
    if vase_cracked:
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
    

    
