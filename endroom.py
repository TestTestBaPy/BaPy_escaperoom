import pygame, sys, os
from display_components import *
import time
import numpy as np
import math

number_sequence = ''


def open_endroom(game_screen, reset_code = False, open_tresor = False):
    global number_sequence
    if reset_code:
        number_sequence = ''
    background = pygame.image.load(os.path.join("Images", "tresor_open.png")).convert()
    game_screen.blit(background, (0, 0))

    if not open_tresor:
        safe_door = pygame.image.load(os.path.join("Images", "tresor_zu.png"))
        game_screen.blit(safe_door,(300,180))
    else:
        safe_door = pygame.image.load(os.path.join("Images", "tresor_auf.png"))
        game_screen.blit(safe_door,(155,130))

    pygame.display.update()

def zoom_touchpad(game_screen):
    background = pygame.image.load(os.path.join("Images", "pad.png")).convert()
    game_screen.blit(background, (0, 0))
    input_rect = pygame.Rect(50, 150, 130, 30)
    pygame.draw.rect(game_screen, (50,150,100), input_rect)
    pygame.display.update()

def check_for_code():
    return number_sequence == '1407'

def open_tresor(game_screen):
    open_endroom(game_screen, open_tresor=True)

def save_num(game_screen, mouse):
    global number_sequence

    if len(number_sequence) < 4:
        

        w = 100
        h = 100

        x = mouse[0]
        y = mouse[1]

        '''
    1(374, 53) - x / 100 ->  4 y-> 1
    2(479, 56) - x / 100 -> 5
    3(582, 52) - x / 100 -> 6
    4(374, 156) - y 3 -> 2
    5(478, 158) - y/100 -> 2
    6(582, 160)
    7(371, 258)
    8(478, 258) - y/100 -> 3
    9(584, 261)
    0(478, 362)- y/100 -> 4'''

        
        if math.ceil(x/100) == 5: # entweder > 100 -> 1, 4, 7 oder < 100 < 200 -> 2, 5, 8, 0 oder > 200 -> 3, 6, 9
            if math.ceil(y/120) == 1:
                number_sequence += '1'
            elif math.ceil(y/120) == 2:
                number_sequence += '4'
            else:
                number_sequence += '7'
            print('DU HAST ENTWEDER AUF 1, 4, 7 GEKLICKT')
        
        elif math.ceil(x/100) == 6:
            if math.ceil(y/120) == 1:
                number_sequence += '2'
            elif math.ceil(y/120) == 2:
                number_sequence += '5'
            elif math.ceil(y/120) == 3:
                number_sequence += '8'
            else:
                number_sequence += '0'
           
        else:
            if math.ceil(y/120) == 1:
                number_sequence += '3'
            elif math.ceil(y/120) == 2:
                number_sequence += '6'
            else:
                number_sequence += '9'

        base_font = pygame.font.Font("pokemon.ttf",40) 
        text_surface = base_font.render(number_sequence, True, (255, 255, 255))
            
        # render at position stated in arguments
        game_screen.blit(text_surface, (50+5, 150+5))



def open_endscreen(game_screen):
    background = pygame.image.load(os.path.join("Images", "endscreen.png")).convert()
    game_screen.blit(background, (0, 0))


    smallText = pygame.font.Font("pokemon.ttf",10)
    
    textSurf, textRect = text_objects("Hey, Escopub...", smallText)
    #textRect.left
    
    textRect.bottomleft = ( (210,490) )
    game_screen.blit(textSurf, textRect)
    
    base_font = pygame.font.Font("pokemon.ttf",20) 
    text_surface = base_font.render("I know, I know it's been a while... Yes, the usal place. Okay, see you soon.", True, (0, 0, 0))
    text_surface2 = base_font.render("Yes, hallucinations. Thank you.", True, (0, 0, 0))
    

    game_screen.blit(text_surface, (180, 90))
    game_screen.blit(text_surface2, (340, 120))