import pygame, os
from display_components import *
from handle_userinput import *
import time
import numpy as np

crack_counter = np.zeros(12).reshape(4,3)
crack_side_len = 45

tuch_pushed = False
vase_cracked = False
klappe_open = False
display_open = False
input_rect = None
    
def open_bathroom():

    # set the current room
    set_current_room("BATH")

    # display background
    game_screen.blit(pygame.image.load(os.path.join("Images", "bathroom.png")).convert(), (0, 0))
    #game_screen.blit(speech_bubble, (speech_bubble_x,speech_bubble_y))

    # display monologue
    textSurf, textRect = text_objects('Oh, my old bathroom. Even Henry and Odette, the rubber ducks are here.', smallText)
    textRect.bottomleft = ( (190,510) )
    game_screen.blit(textSurf, textRect)
    textSurf, textRect = text_objects('Hmph, it seems Emma is not here.', smallText)
    textRect.bottomleft = ( (190,530) )
    game_screen.blit(textSurf, textRect)

    pygame.display.update()


def crack_wall(x, y):
    """Cracks the wall at the given korrdinates i.e. displays a crack on the wall
       Args:
            x the x coordinate (from 0 to 2)
            y the y coordinate (from 0 to 3)
        Returns:
            True, if all tiles are cracked. Else returns False.
        """

    global crack_counter
    wall_crack = pygame.image.load(os.path.join("Images", "crack.png"))
    
    # each crack is crack_side_len(45) * crack_side_len(45) pixels big, 
    # so regarding of the koordinates decide where to place it
    for i in range(3):
        for j in range(4):
            if x+45 > 451+((i+1)*crack_side_len) > x and y+45 > 183+((j+1)*crack_side_len) > y:
                game_screen.blit(wall_crack, (451+(i*crack_side_len),183+(j*crack_side_len)))
                crack_counter[j][i] = 1

    if crack_counter.all() == 1:
        game_screen.blit(pygame.image.load(os.path.join("Images", "bathroom_door.png")),(0,0))
        set_current_room("BATHEND")


def open_backroom():

    global input_rect

    # set the current room
    set_current_room("BACK")
    

    game_screen.blit(pygame.image.load(os.path.join("Images", "backroom.png")).convert(), (0, 0))
    

    if klappe_open:
        klappe = pygame.image.load(os.path.join("Images", "klappe.png")).convert_alpha()
        game_screen.blit(klappe, (310, 316))

    # if the display is not open the code was not (yet) entered correctly
    if not display_open:
    
        game_screen.blit(pygame.image.load(os.path.join("Images", "board.png")).convert(), (313, 44))

        textSurf, textRect = text_objects('Please enter the right code: ', smallText)    
        textRect.bottomleft = ((370,90))
        game_screen.blit(textSurf, textRect)
     
        textSurf, textRect = text_objects('(Press enter, when done)', smallText)    
        textRect.bottomleft = ((380,110))
        game_screen.blit(textSurf, textRect)

        input_rect = pygame.Rect(450, 130, 100, 30)
        pygame.draw.rect(game_screen, (170,170,170), input_rect)

        #correct = handle_input(input_rect)

    else:

        game_screen.blit(speech_bubble, (speech_bubble_x,speech_bubble_y))
        textSurf, textRect = text_objects("That was correct! I think I'm going crazy, I see numbers everywhere.", smallText)    
        textRect.bottomleft = ((speech_bubble_x + 50 ,speech_bubble_y + 65))
        game_screen.blit(textSurf, textRect)
        textSurf, textRect = text_objects('Maybe I should remeber them....', smallText)    
        textRect.bottomleft = ((speech_bubble_x + 50 ,speech_bubble_y + 85))
        game_screen.blit(textSurf, textRect)

    if not tuch_pushed:
        game_screen.blit(pygame.image.load(os.path.join("Images", "tuch.png")).convert_alpha(), (0, 0))
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "tuch_pushed.png")).convert_alpha(), (0, 0))

    vase = pygame.image.load(os.path.join("Images", "vase.png")).convert_alpha()
    vase = pygame.transform.scale(vase, (90, 87))

    if not vase_cracked:
        game_screen.blit(vase, (805, 118))

   

def input_correct():
    x =  handle_input(input_rect = input_rect, max_chars = 2, only_integer=True)
    open_backroom()
    return x

def display_solved():
    open_backroom()
    clock.tick(2)
    open_display()

        

# the following functions set the global status-variables to keep track of players actions and display them
def crack_vase():
    global vase_cracked
    vase_cracked = True
    open_backroom()


def open_klappe():
    global klappe_open
    global vase_cracked
    if vase_cracked:
        klappe_open = True
        open_backroom()


def push_tuch():
    global tuch_pushed
    tuch_pushed = True
    open_backroom()


def open_display():

    
    global display_open
    display_open = True
    open_backroom()

    # set the current room
    set_current_room("BACKEND")
    

    
