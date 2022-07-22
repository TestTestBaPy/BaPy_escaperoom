import pygame, sys, os
from display_components import *
import time
import numpy as np
import math

from handle_userinput import get_input_text, handle_input

number_sequence = ''
input_rect = None

def open_endroom(reset_code = False, open_tresor = False):

    # set the current room
    set_current_room("TRES")
    
    global number_sequence
    if reset_code:
        number_sequence = ''
    game_screen.blit(pygame.image.load(os.path.join("Images", "tresor_open.png")).convert(), (0, 0))

    if not open_tresor:
        safe_door = pygame.image.load(os.path.join("Images", "tresor_zu.png"))
        game_screen.blit(safe_door,(300,180))
    else:
        safe_door = pygame.image.load(os.path.join("Images", "tresor_auf.png"))
        game_screen.blit(safe_door,(155,130))

    pygame.display.update()

def zoom_touchpad():

    # set the current room
    set_current_room("TCHP")

    game_screen.blit(pygame.image.load(os.path.join("Images", "pad.png")).convert(), (0, 0))
    input_rect = pygame.Rect(50, 150, 130, 130)
    pygame.draw.rect(game_screen, (50,150,100), input_rect)
    pygame.display.update()

def check_for_code():
    return number_sequence == '1407' or number_sequence == '1532'

def open_tresor():
    open_endroom(open_tresor=True)

def save_num(mouse):
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

        
        if math.ceil(x/100) == 5: 
            if math.ceil(y/120) == 1:
                number_sequence += '1'
            elif math.ceil(y/120) == 2:
                number_sequence += '4'
            else:
                number_sequence += '7'
        
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

        base_font = pygame.font.Font("pokemon.ttf",60) 
        text_surface = base_font.render(number_sequence, True, (255, 255, 255))
            
        # render at position stated in arguments
        game_screen.blit(text_surface, (50+5, 150+5))

def open_endscreen(clicked_on_exit = False):

    # set the current room
    set_current_room("CALL")

    if clicked_on_exit:
        game_screen.blit(pygame.image.load(os.path.join("Images", "endscreen_pushexit.png")).convert(), (0, 0))
       
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "endscreen.png")).convert(), (0, 0))
    
    textSurf, textRect = text_objects("Hey, Escopub...", smallText)
    textRect.bottomleft = ( (210,490) )
    game_screen.blit(textSurf, textRect)
    
    text_surface = smallText.render("Forget the ealier text... It was just because of the stress from the funeral. ", True, (0, 0, 0))
    game_screen.blit(text_surface, (180, 90))

    text_surface = smallText.render("Can you help a man out? Yes, usual place. Okay, see you soon. Thank you.", True, (0, 0, 0))
    game_screen.blit(text_surface, (180, 120))

def open_final_words():

    global input_rect

    # set the current room
    set_current_room("FNAL")

    game_screen.blit(pygame.image.load(os.path.join("Images", "final_words.png")).convert(), (0, 0))

    text_surface = smallText.render("Did you enjoy the Escaperoom-Game 'Where is my Emma?' Grade now with a 1.0 at: ", True, (0, 0, 0))
    game_screen.blit(text_surface, (140, 240))

    text_surface = smallText.render("https://hisinone.dienste.uni-osnabrueck.de", True, (50, 50, 250))
    game_screen.blit(text_surface, (300, 270))

    text_surface = smallText.render("If you like to, you can enter your user_name to be put in the highscore table!", True, (0, 0, 0))
    game_screen.blit(text_surface, (140, 350))

    input_rect = pygame.Rect(400, 400, 200, 30)
    pygame.draw.rect(game_screen, (170,170,170), input_rect)

    #handle_input(room="FNAL", input_rect= input_rect, only_integer=False, max_chars=20)

def user_name_input():
    return handle_input(input_rect= input_rect, only_integer=False, max_chars=20)

def check_input():
    return get_input_text() == '15'
    

    
