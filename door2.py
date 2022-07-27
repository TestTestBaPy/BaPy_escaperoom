"""This file manages all the rooms behind the second door, their interactive functions, status variables and displays them"""
import pygame, os
from display_components import *

pointer_1 = 9
pointer_2 = 9
pointer_3 = 9

solved_chld = False
trap_open = False
got_nest = False
got_key = False


def open_childsroom():
    """Opens i.e. display the childsroom"""
    # Set the current room
    set_current_room("CHLD")
    
    background = pygame.image.load(os.path.join("Images", "childsroom.png")).convert()
    game_screen.blit(background, (0, 0))
    pygame.display.update()

    game_screen.blit(speech_bubble, (SPEECH_BUBBLE_X, SPEECH_BUBBLE_Y))
    textSurf = text_objects("The nostalgia... that's my old room. I didn't know my parents kept my stuff.", small_text)    
    game_screen.blit(textSurf, (SPEECH_BUBBLE_X + 30, SPEECH_BUBBLE_Y + 40))

    textSurf = text_objects("Even my old friend. I loved reading stories to my teddybear. ", small_text)    
    game_screen.blit(textSurf, (SPEECH_BUBBLE_X + 30, SPEECH_BUBBLE_Y + 65))

    display_pointer()
    pygame.display.update()


def display_pointer():
    """Displays the numbers on the blackboard"""
    base_font = pygame.font.Font("pokemon.ttf", 70) 
    text_surface = base_font.render(str(pointer_1 % 10), True, WHITE) 
    game_screen.blit(text_surface, (400, 110))

    text_surface = base_font.render(str(pointer_2 % 10), True, WHITE) 
    game_screen.blit(text_surface, (470, 110))

    text_surface = base_font.render(str(pointer_3 % 10), True, WHITE) 
    game_screen.blit(text_surface, (540, 110))

    check_code()


def check_code():
    """Checks if the current blackboard numbers are correct"""
    global solved_chld
    
    if str(pointer_1 % 10) + str(pointer_2 % 10) + str(pointer_3 % 10) == '420':
        solved_chld = True
        game_screen.blit(pygame.image.load(os.path.join("Images", "wall.png")).convert_alpha(), (0, 0))

    pygame.display.update()


def open_book():
    """Displays the inside of the book in the childsroom"""
    pygame.mixer.Sound.set_volume(PAGE, 0.1)
    pygame.mixer.Sound.play(PAGE)

    # Set the current room
    set_current_room("BOOK")
    
    game_screen.blit(pygame.image.load(os.path.join("Images", "book.png")).convert(), (0, 0))
    pygame.display.update()

    small_text = pygame.font.Font("pokemon.ttf", 30)

    # First hint
    textSurf = text_objects('6  8  0', small_text)
    game_screen.blit(textSurf, (280, 50))

    textSurf = text_objects('One number is correct', small_text)
    game_screen.blit(textSurf, (180, 80))

    textSurf = text_objects('and is postioned right.', small_text)
    game_screen.blit(textSurf, (180, 110))

    # The second hint
    textSurf = text_objects('6  1  2', small_text)
    game_screen.blit(textSurf, (640, 95))

    textSurf = text_objects('One number is correct', small_text)
    game_screen.blit(textSurf, (540, 125))

    textSurf = text_objects('but is postioned false.', small_text)
    game_screen.blit(textSurf, (540, 155))

    # The third hint
    textSurf = text_objects('0  4  6', small_text)
    game_screen.blit(textSurf, (280, 210))
    
    textSurf = text_objects('Two numbers are correct', small_text)
    game_screen.blit(textSurf, (170, 240))

    textSurf = text_objects('but postioned false.', small_text)
    game_screen.blit(textSurf, (180, 270))

    # The fourth hint
    textSurf = text_objects('7  3  8', small_text)
    game_screen.blit(textSurf, (640, 255))
 
    textSurf = text_objects('Nothing is correct.', small_text)
    game_screen.blit(textSurf, (540, 285))

    # The fifth hint
    textSurf = text_objects('8  7  4', small_text)
    game_screen.blit(textSurf, (280, 370))

    textSurf = text_objects('One number is correct', small_text)
    game_screen.blit(textSurf, (180, 400))


    textSurf = text_objects('but is postioned false.', small_text)
    game_screen.blit(textSurf, (180, 430))

    # The question
    textSurf = text_objects('What is the correct code?', small_text)
    game_screen.blit(textSurf, (340, 530))


def rotate_number(field):
    """Rotates the number on the blackboard
    Args:
      field: after dividing the mouse-coordinate by 15 the resulting numbers (ranges)
        indicate which of the three squares was clicked. 
    """
    global pointer_1 
    global pointer_2 
    global pointer_3 

    pygame.mixer.Sound.set_volume(RCLICK, 0.1)
    pygame.mixer.Sound.play(RCLICK)

    # Increment the respective pointer and display the new code
    if field >= 26 and field <= 30:
        pointer_1 += 1  
        
    elif field >= 30 and field <= 35:
        pointer_2 += 1
             
    else:
       pointer_3 += 1
       
    open_childsroom()
    display_pointer()


def open_flyer(): 
    """Opens and displays the flyer"""
    # Set the current room
    set_current_room("TRAS")
    game_screen.blit(pygame.image.load(os.path.join("Images", "flyer.png")).convert(), (0, 0))
    pygame.display.update()


def open_garden():
    """Opens i.e. displays the garden"""
    # Set the current room
    set_current_room("GARD")
  
    game_screen.blit(pygame.image.load(os.path.join("Images", "garden.png")).convert(), (0, 0))

    # If the side entrace was opened display it
    if trap_open:
        game_screen.blit(speech_bubble, (SPEECH_BUBBLE_X,SPEECH_BUBBLE_Y))
        textSurf = text_objects("That was correct! But why are there so many holes in the fence?", small_text)   
        game_screen.blit(textSurf, (SPEECH_BUBBLE_X + 50 ,SPEECH_BUBBLE_Y + 45))
        textSurf = text_objects('Maybe I should remeber them....', small_text)    
        game_screen.blit(textSurf, (SPEECH_BUBBLE_X + 50 ,SPEECH_BUBBLE_Y + 65))
        
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "garden_klappe.png")).convert_alpha(), (0, 0))   
    
    pygame.display.update()


def get_chld_solved():
    """Get if the childsroom is solved"""
    return solved_chld


# The following functions set the global status-variables to keep track of players actions and display them
def open_birdhouse():
    """Opens i.e. displays the birdhouse"""
    pygame.mixer.Sound.set_volume(BIRD, 0.1)
    pygame.mixer.Sound.play(BIRD)
    
    # Set the current room
    set_current_room("BIRD")
   
    # Check the variables an display what is needed
    if got_key:
        game_screen.blit(pygame.image.load(os.path.join("Images", "birdshouse_COLLECTedkey.png")).convert(), (0, 0))
    elif got_nest:
        game_screen.blit(pygame.image.load(os.path.join("Images", "birdshouse.png")).convert(), (0, 0))
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "birdshouse_with_nest.png")).convert(), (0, 0))

    pygame.display.update()

# the following functions set the global status-variables to keep track of players actions and display them

def get_key():
    """Collect the key if possible and display it"""
    global got_key
    if not got_key and got_nest:
        pygame.mixer.Sound.set_volume(COLLECT, 0.1)
        pygame.mixer.Sound.play(COLLECT)
        got_key = True
        open_birdhouse()


def remove_nest():
    """Remove the nest if possible and display it"""
    global got_nest
    if not got_nest:
        pygame.mixer.Sound.set_volume(NEST, 0.5)
        pygame.mixer.Sound.play(NEST)
        got_nest = True
        open_birdhouse()


def open_trap_garden():
    """Open the trap if the key is collected and display it"""
    global trap_open

    pygame.mixer.Sound.play(OPENS)
    pygame.mixer.Sound.set_volume(POPPING, 0.7)
    pygame.mixer.Sound.play(POPPING)

    trap_open = True
    open_garden()


def get_trap_open():
    """Get if the trap is open"""
    return trap_open


def get_got_key():
    """Get if you got the key"""
    return got_key