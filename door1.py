import pygame, os, numpy
from display_components import *
from handle_userinput import *

crack_counter = numpy.zeros(12).reshape(4, 3)
crack_side_len = 45

tuch_pushed = False
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
    textSurf = text_objects('Oh, my old bathroom. Even Henry and Odette, the rubber ducks are here.', smallText)
    game_screen.blit(textSurf, (190, 510))
    textSurf = text_objects('Hmph, it seems Emma is not here.', smallText)
    game_screen.blit(textSurf, (190, 530))
    
    pygame.display.update()


def crack_wall(x, y):
    """Cracks the wall at the given coordinates i.e. displays a crack on the wall
    Args:
      x:
       The x coordinate (from 0 to 2)
      y:
       The y coordinate (from 0 to 3)
    Returns:
      True, if all tiles are cracked. Else False.
    """
    global crack_counter
    wall_crack = pygame.image.load(os.path.join("Images", "crack.png"))
    
    # Each crack is crack_side_len(45) * crack_side_len(45) pixels big, 
    # so regarding of the coordinates decide where to place it
    for i in range(3):
        for j in range(4):
            if x + 45 > 451 + ((i + 1) * crack_side_len) > x and y + 45 > 183 + ((j + 1) * crack_side_len) > y:
                pygame.mixer.Sound.set_volume(kling, 0.1)
                pygame.mixer.Sound.play(kling)
                game_screen.blit(wall_crack, (451 + (i * crack_side_len), 183 + (j * crack_side_len)))
                crack_counter[j][i] = 1

    if crack_counter.all() == 1:
        game_screen.blit(pygame.image.load(os.path.join("Images", "bathroom_door.png")), (0, 0))
        set_current_room("BATHEND")


def open_backroom():
    """Opens i.e. displays the backroom"""
    global input_rect

    if get_current_room() == "BATHEND":
        pygame.mixer.Sound.set_volume(footsteps, 0.1)
        pygame.mixer.Sound.play(footsteps)
       
    # Set the current room
    set_current_room("BACK")
    
    game_screen.blit(pygame.image.load(os.path.join("Images", "backroom.png")).convert(), (0, 0))
    
    # If the trapdoor was opened, display it
    if trap_open:
        klappe = pygame.image.load(os.path.join("Images", "klappe.png")).convert_alpha()
        game_screen.blit(klappe, (0, 0))

    # If the BLACKboard is not open, the code was not (yet) entered correctly
    if not display_open:
        game_screen.blit(pygame.image.load(os.path.join("Images", "board.png")).convert(), (313, 44))
        textSurf = text_objects('Please enter the right code: ', smallText)    
        game_screen.blit(textSurf, (370, 90))
     
        textSurf = text_objects('(Press enter, when done)', smallText)    
        game_screen.blit(textSurf, (380, 110))

        input_rect = pygame.Rect(450, 130, 100, 30)
        pygame.draw.rect(game_screen, (170, 170, 170), input_rect)

        input_correct(go = False)

    # If the correct code was entered...
    else:
        game_screen.blit(speech_bubble, (SPEECH_BUBBLE_X, SPEECH_BUBBLE_Y))
        textSurf = text_objects("That was correct! I think I'm going crazy, I see numbers everywhere.", smallText)    
        game_screen.blit(textSurf, (SPEECH_BUBBLE_X + 50, SPEECH_BUBBLE_Y + 65))
        textSurf = text_objects('Maybe I should remeber them....', smallText)    
        game_screen.blit(textSurf, (SPEECH_BUBBLE_X + 50, SPEECH_BUBBLE_Y + 85))

    if not tuch_pushed:
        game_screen.blit(pygame.image.load(os.path.join("Images", "tuch.png")).convert_alpha(), (0, 0))
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "tuch_pushed.png")).convert_alpha(), (0, 0))

    if not vase_cracked:
        game_screen.blit(pygame.image.load(os.path.join("Images", "vase.png")).convert_alpha(), (0, 0))

 
def input_correct(go):
    """Handle and check the input from the user on the text field (input rect)
    Args:
      If go is true, the field is active, else it is inactive and only display (if given) prior input
    Returns:
      True, if input was coorect/wanted. Else or when go was set to False, False.
    """
    if not go:
        display_num_sequence(input_rect)
        return go
    else:
        return handle_input(go = go, input_rect = input_rect, max_chars = 2, only_integer = True)  


def display_solved():
    """If the display is solved, displays it"""
    pygame.mixer.Sound.set_volume(correct, 0.1)
    pygame.mixer.Sound.play(correct)
               
    open_backroom()
    clock.tick(2)
    open_display()


# Returns wheter the code was entered correctly
def check_input():
    return get_input_text() == '15'

# The following functions sets the global status-variables to keep track of players actions and display them
def crack_vase():
    global vase_cracked
    if not vase_cracked:
        pygame.mixer.Sound.set_volume(kling, 0.1)
        pygame.mixer.Sound.play(kling)
        vase_cracked = True
        open_backroom()


def open_klappe():
    global trap_open
    global vase_cracked
    if vase_cracked:
        if not trap_open:
            pygame.mixer.Sound.set_volume(clicking, 0.1)
            pygame.mixer.Sound.play(clicking)
            trap_open = True
            open_backroom()


def push_tuch():
    global tuch_pushed
    if not tuch_pushed:
        pygame.mixer.Sound.set_volume(cloth_sound, 1)
        pygame.mixer.Sound.play(cloth_sound)    
        tuch_pushed = True
        open_backroom()


def open_display():
    global display_open

    pygame.mixer.Sound.set_volume(popping, 0.7)
    pygame.mixer.Sound.play(popping)

    display_open = True
    open_backroom()

    # Set the current room
    set_current_room("BACKEND")