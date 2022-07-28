"""This file manages all the rooms behind the first door, 
their interactive functions, status variables and displays them"""
import pygame, os, numpy
from display_components import *
from handle_userinput import *

crack_counter = numpy.zeros(12).reshape(4, 3)
CRACK_SIDE_LEN = 45

cloth_pushed = False
vase_cracked = False
trap_open = False
display_open = False
input_rect = None


def open_bathroom():
    """Opens i.e. displays the bathroom"""
    # Set the current room
    set_current_room("BATH")

    # Display background
    game_screen.blit(pygame.image.load(os.path.join("Images", "bathroom.png")).convert(), (0, 0))

    # Display monologue
    textSurf = text_objects('Oh, my old bathroom. Even Henry and Odette, the rubber ducks are here.', small_text)
    game_screen.blit(textSurf, (190, 490))
    textSurf = text_objects('Hmph, it seems Emma is not here.', small_text)
    game_screen.blit(textSurf, (190, 510))
    
    pygame.display.update()


def crack_wall(x, y):
    """Cracks the wall at the given coordinates i.e. displays a crack on the wall
    Args:
      x: the x coordinate (from 0 to 2)
      y: the y coordinate (from 0 to 3)
    Returns:
      True, if all tiles are cracked. Else False.
    """
    global crack_counter
    wall_crack = pygame.image.load(os.path.join("Images", "crack.png"))
    
    # Each crack is of the size CRACK_SIDE_LEN(45) * CRACK_SIDE_LEN(45) pixels, 
    # so regarding of the coordinates decide where to place it
    for i in range(3):
        for j in range(4):
            if x + 45 > 451 + ((i + 1) * CRACK_SIDE_LEN) > x and y + 45 > 183 + ((j + 1) * CRACK_SIDE_LEN) > y:
                pygame.mixer.Sound.set_volume(KLING, 0.1)
                pygame.mixer.Sound.play(KLING)
                game_screen.blit(wall_crack, (451 + (i * CRACK_SIDE_LEN), 183 + (j * CRACK_SIDE_LEN)))
                crack_counter[j][i] = 1

    if crack_counter.all() == 1:
        game_screen.blit(pygame.image.load(os.path.join("Images", "bathroom_door.png")), (0, 0))
        set_current_room("BATHEND")


def open_backroom():
    """Opens i.e. displays the backroom"""
    global input_rect

    if get_current_room() == "BATHEND":
        pygame.mixer.Sound.set_volume(FOOTSTEPS, 0.1)
        pygame.mixer.Sound.play(FOOTSTEPS)
       
    # Set the current room
    set_current_room("BACK")
    
    game_screen.blit(pygame.image.load(os.path.join("Images", "backroom.png")).convert(), (0, 0))
    
    # If the trapdoor was opened, display it
    if trap_open:
        klappe = pygame.image.load(os.path.join("Images", "klappe.png")).convert_alpha()
        game_screen.blit(klappe, (0, 0))

    # If the blackboard is not open, the code was not (yet) entered correctly
    if not display_open:
        game_screen.blit(pygame.image.load(os.path.join("Images", "board.png")).convert(), (313, 44))
        textSurf = text_objects('Please enter the right code: ', small_text)    
        game_screen.blit(textSurf, (370, 60))
     
        textSurf = text_objects('(Press enter, when done)', small_text)    
        game_screen.blit(textSurf, (380, 80))

        input_rect = pygame.Rect(450, 130, 100, 30)
        pygame.draw.rect(game_screen, (170, 170, 170), input_rect)

        input_correct(go = False)

    # If the correct code was entered...
    else:
        game_screen.blit(speech_bubble, (SPEECH_BUBBLE_X, SPEECH_BUBBLE_Y))
        textSurf = text_objects("That was correct! I think I'm going crazy, I see numbers everywhere.", small_text)    
        game_screen.blit(textSurf, (SPEECH_BUBBLE_X + 50, SPEECH_BUBBLE_Y + 45))
        textSurf = text_objects('Maybe I should remeber them....', small_text)    
        game_screen.blit(textSurf, (SPEECH_BUBBLE_X + 50, SPEECH_BUBBLE_Y + 65))

    if not cloth_pushed:
        game_screen.blit(pygame.image.load(os.path.join("Images", "tuch.png")).convert_alpha(), (0, 0))
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "tuch_pushed.png")).convert_alpha(), (0, 0))

    if not vase_cracked:
        game_screen.blit(pygame.image.load(os.path.join("Images", "vase.png")).convert_alpha(), (0, 0))

 
def input_correct(go):
    """Handles and checks the input from the user on the text field (input rect)
    Args:
      go: if go is true, the field is active, else it is inactive and only displays (if given) prior input
    Returns:
      True, if input was coorect/wanted. Else or when go was set to False, False.
    """
    if not go:
        display_num_sequence(input_rect)
        return go
    else:
        return handle_input(go = go, input_rect = input_rect, max_chars = 2, only_integer = True)  


def display_solved():
    """If the display is solved, display it"""
    pygame.mixer.Sound.set_volume(CORRECT, 0.1)
    pygame.mixer.Sound.play(CORRECT)
               
    open_backroom()
    clock.tick(2)
    open_display()


def check_input():
    """Get the information if the enetered code was correct"""
    return get_input_text() == '15'


# The following functions sets the global status-variables to keep track of players actions and display them
def crack_vase():
    """Cracks the vase and displays it"""
    global vase_cracked
    if not vase_cracked:
        pygame.mixer.Sound.set_volume(KLING, 0.1)
        pygame.mixer.Sound.play(KLING)
        vase_cracked = True
        open_backroom()


def open_trap():
    """Opens the trapdoor and displays it"""
    global trap_open
    global vase_cracked
    if vase_cracked:
        if not trap_open:
            pygame.mixer.Sound.set_volume(CLICKING, 0.1)
            pygame.mixer.Sound.play(CLICKING)
            trap_open = True
            open_backroom()


def push_cloth():
    """Pushes the cloth and displays it"""
    global cloth_pushed
    if not cloth_pushed:
        pygame.mixer.Sound.set_volume(CLOTH_SOUND, 1)
        pygame.mixer.Sound.play(CLOTH_SOUND)    
        cloth_pushed = True
        open_backroom()


def open_display():
    """Opens the display and displays it"""
    global display_open

    pygame.mixer.Sound.set_volume(POPPING, 0.7)
    pygame.mixer.Sound.play(POPPING)

    display_open = True
    open_backroom()

    # Set the current room
    set_current_room("BACKEND")