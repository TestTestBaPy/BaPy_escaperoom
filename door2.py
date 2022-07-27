import pygame, os
from display_components import *

pointer_1 = 9
pointer_2 = 9
pointer_3 = 9

solved_door2 = False
klappe_open = False
got_nest = False
got_key = False


def open_childsroom():
    """Opens i.e. display the childsroom"""
    # Set the current room
    set_current_room("CHLD")
    
    background = pygame.image.load(os.path.join("Images", "childsroom.png")).convert()
    game_screen.blit(background, (0, 0))
    pygame.display.update()

    game_screen.blit(speech_bubble, (speech_bubble_x, speech_bubble_y))
    textSurf, textRect = text_objects("The nostalgia... that's my old room. I didn't know my parents kept my stuff.", smallText)    
    textRect.bottomleft = ((speech_bubble_x + 30, speech_bubble_y + 60))
    game_screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects("Even my old friend. I loved reading stories to my teddybear. ", smallText)    
    textRect.bottomleft = ((speech_bubble_x + 30, speech_bubble_y + 85))
    game_screen.blit(textSurf, textRect)

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
    global solved_door2
    
    if str(pointer_1 % 10) + str(pointer_2 % 10) + str(pointer_3 % 10) == '420':
        solved_door2 = True
        game_screen.blit(pygame.image.load(os.path.join("Images", "wall.png")).convert_alpha(), (0, 0))

    pygame.display.update()


def open_book():
    """Displays the inside of the book in the childsroom"""
    pygame.mixer.Sound.set_volume(page, 0.1)
    pygame.mixer.Sound.play(page)

    # Set the current room
    set_current_room("BOOK")
    
    game_screen.blit(pygame.image.load(os.path.join("Images", "book.png")).convert(), (0, 0))
    pygame.display.update()

    smallText = pygame.font.Font("pokemon.ttf", 30)

    # First hint
    textSurf, textRect = text_objects('6  8  0', smallText)
    textRect.bottomleft = ((280, 80))
    game_screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects('One number is correct', smallText)
    textRect.bottomleft = ((180, 110))
    game_screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects('and is postioned right.', smallText)
    textRect.bottomleft = ((180, 140))
    game_screen.blit(textSurf, textRect)

    # The second hint
    textSurf, textRect = text_objects('6  1  2', smallText)
    textRect.bottomleft = ((640, 125))
    game_screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects('One number is correct', smallText)
    textRect.bottomleft = ((540, 155))
    game_screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects('but is postioned false.', smallText)
    textRect.bottomleft = ((540, 185))
    game_screen.blit(textSurf, textRect)

    # The third hint
    textSurf, textRect = text_objects('0  4  6', smallText)
    textRect.bottomleft = ((280, 240))
    game_screen.blit(textSurf, textRect)
    
    textSurf, textRect = text_objects('Two numbers are correct', smallText)
    textRect.bottomleft = ((170, 270))
    game_screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects('but postioned false.', smallText)
    textRect.bottomleft = ((180, 300))
    game_screen.blit(textSurf, textRect)

    # The fourth hint
    textSurf, textRect = text_objects('7  3  8', smallText)
    textRect.bottomleft = ((640, 285))
    game_screen.blit(textSurf, textRect)
 
    textSurf, textRect = text_objects('Nothing is correct.', smallText)
    textRect.bottomleft = ((540, 315))
    game_screen.blit(textSurf, textRect)

    # The fifth hint
    textSurf, textRect = text_objects('8  7  4', smallText)
    textRect.bottomleft = ((280, 400))
    game_screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects('One number is correct', smallText)
    textRect.bottomleft = ((180, 430))
    game_screen.blit(textSurf, textRect)


    textSurf, textRect = text_objects('but is postioned false.', smallText)
    textRect.bottomleft = ((180, 460))
    game_screen.blit(textSurf, textRect)

    # The question
    textSurf, textRect = text_objects('What is the correct code?', smallText)
    textRect.bottomleft = ((340, 560))
    game_screen.blit(textSurf, textRect)


def rotate_number(field):
    """Rotates the number on the blackboard
    Args:
      field: 
        after dividing the mouse-coordinate by 15 the resulting numbers (ranges)
        indicate which of the three squares was clicked. 
    """
    global pointer_1 
    global pointer_2 
    global pointer_3 

    pygame.mixer.Sound.set_volume(rclick, 0.1)
    pygame.mixer.Sound.play(rclick)

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
    if klappe_open:
        game_screen.blit(speech_bubble, (speech_bubble_x,speech_bubble_y))
        textSurf, textRect = text_objects("That was correct! But why are there so many holes in the fence?", smallText)    
        textRect.bottomleft = ((speech_bubble_x + 50 ,speech_bubble_y + 65))
        game_screen.blit(textSurf, textRect)
        textSurf, textRect = text_objects('Maybe I should remeber them....', smallText)    
        textRect.bottomleft = ((speech_bubble_x + 50 ,speech_bubble_y + 85))
        game_screen.blit(textSurf, textRect)
        
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "garden_klappe.png")).convert_alpha(), (0, 0))   
    
    pygame.display.update()


def get_solved_door2():
    return solved_door2


# The following functions set the global status-variables to keep track of players actions and display them
def open_birdshouse():
    """Opens i.e. displays the birdshouse"""
    pygame.mixer.Sound.set_volume(bird, 0.1)
    pygame.mixer.Sound.play(bird)
    
    # Set the current room
    set_current_room("BIRD")
   
    # Check the variables an display what is needed
    if got_key:
        game_screen.blit(pygame.image.load(os.path.join("Images", "birdshouse_collectedkey.png")).convert(), (0, 0))
    elif got_nest:
        game_screen.blit(pygame.image.load(os.path.join("Images", "birdshouse.png")).convert(), (0, 0))
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "birdshouse_with_nest.png")).convert(), (0, 0))

    pygame.display.update()

# the following functions set the global status-variables to keep track of players actions and display them

def get_key():
    global got_key
    if not got_key:
        pygame.mixer.Sound.set_volume(collect, 0.1)
        pygame.mixer.Sound.play(collect)
        got_key = True
        open_birdshouse()


def remove_nest():
    global got_nest
    if not got_nest:
        pygame.mixer.Sound.set_volume(nest, 0.5)
        pygame.mixer.Sound.play(nest)
        got_nest = True
        open_birdshouse()


def open_klappe_garden():
    global klappe_open

    pygame.mixer.Sound.play(opens)
    pygame.mixer.Sound.set_volume(popping, 0.7)
    pygame.mixer.Sound.play(popping)

    klappe_open = True
    open_garden()


def get_klappe_open():
    return klappe_open


def get_got_key():
    return got_key