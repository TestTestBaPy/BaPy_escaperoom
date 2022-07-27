import pygame, os, time, math, webbrowser
from display_components import *
from handle_userinput import handle_input

number_sequence = ''
input_rect = None
open = True


def open_endroom(reset_code = False, open_safe = False):
    """Opens i.e. displays the endroom with the safe.
    Args:
      reset_code:
       Indicates if the current code should be resetted
      open_safe:
       Indicates if the safe was already open so it can be displayed correctly
    """
    # Set the current room
    set_current_room("TRES")
    
    global number_sequence
   
    # Alternative codes have alternative endings
    if number_sequence == '1407':
        game_screen.blit(pygame.image.load(os.path.join("Images", "emma_dead.png")).convert(), (0, 0))
        text_surface = smallText.render("EMMA", True, WHITE)
        game_screen.blit(text_surface, (415, 280))
        text_surface = smallText.render("* 03.08.2014", True, WHITE)
        game_screen.blit(text_surface, (380, 320))
        text_surface = smallText.render("x 04.20.2025", True, WHITE)
        game_screen.blit(text_surface, (380, 340))
        
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "emma_alive.png")).convert(), (0, 0))

    if reset_code:
        number_sequence = ''

    # If the safe was (not) opened (do not) display the door
    if not open_safe:
        safe_door = pygame.image.load(os.path.join("Images", "tresor_closed.png"))
        game_screen.blit(safe_door,(0, 0))
    else:
        safe_door = pygame.image.load(os.path.join("Images", "tresor_opened.png"))
        game_screen.blit(safe_door,(0, 0))

    pygame.display.update()


def zoom_touchpad():
    """Zooms in on the touchpad so the user can type in a code"""
    # Set the current room
    set_current_room("TCHP")

    game_screen.blit(pygame.image.load(os.path.join("Images", "pad.png")).convert(), (0, 0))
    input_rect = pygame.Rect(50, 150, 130, 130)
    pygame.draw.rect(game_screen, (50, 150, 100), input_rect)
    pygame.display.update()


def check_for_code():
    """Returns wheter one of the right codes was entered"""
    return number_sequence == '1407' or number_sequence == '1532'


def open_safe():
    """Opens the safe with the open_endroom function"""
    pygame.mixer.Sound.set_volume(swoosh, 0.2)
    pygame.mixer.Sound.play(swoosh)
    open_endroom(open_safe = True)


def save_num(mouse):
    """Safes the inputted numbers to be able to check and display the entered code"""
    global number_sequence
    pygame.mixer.Sound.set_volume(piep, 0.1)
    pygame.mixer.Sound.play(piep)

    if len(number_sequence) < 4:   
        x = mouse[0]
        y = mouse[1]

        # Perform simple division to decide which of the numbers was clicked
        if math.ceil(x / 100) == 5: 
            if math.ceil(y / 120) == 1:
                number_sequence += '1'
            elif math.ceil(y / 120) == 2:
                number_sequence += '4'
            else:
                number_sequence += '7'
        
        elif math.ceil(x / 100) == 6:
            if math.ceil(y / 120) == 1:
                number_sequence += '2'
            elif math.ceil(y / 120) == 2:
                number_sequence += '5'
            elif math.ceil(y / 120) == 3:
                number_sequence += '8'
            else:
                number_sequence += '0'
           
        else:
            if math.ceil(y / 120) == 1:
                number_sequence += '3'
            elif math.ceil(y / 120) == 2:
                number_sequence += '6'
            else:
                number_sequence += '9'

        text_surface = bigText.render(number_sequence, True, WHITE)
            
        # Display the code
        game_screen.blit(text_surface, (50 + 5, 150 + 5))


def open_endscreen(clicked_on_exit = False):
    """Opens i.e. displays the endscreen
    Args:
      clicked_on_exit if set to True simulates a button click on "EXIT"
    """
    # Set the current room
    set_current_room("CALL")

    if clicked_on_exit:
        push_exit()   
    
    # Display alternative endings based on the entered code
    if number_sequence == '1407':

        game_screen.blit(pygame.image.load(os.path.join("Images", "call_buy.png")).convert(), (0, 0))
   
        text_surface = smallText.render("Forget the ealier text... It was just because of the stress from the funeral. ", True, BLACK)
        game_screen.blit(text_surface, (180, 90))

        text_surface = smallText.render("Can you help a man out? Yes, usual place. Okay, see you soon. Thank you.", True, BLACK)
        game_screen.blit(text_surface, (180, 120))
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "call_quit.png")).convert(), (0, 0))

        text_surface = smallText.render("Forget the ealier text... It was just because of the stress from the funeral. ", True, BLACK)
        game_screen.blit(text_surface, (180, 90))

        text_surface = smallText.render("Please delete my number. Yes, I'm quitting. Have a good life my firend.", True, BLACK)
        game_screen.blit(text_surface, (180, 120))

    # Display the monologue
    textSurf = text_objects("Hey, Escopub...", smallText)
    game_screen.blit(textSurf, (210, 490))


def open_final_words():
    """Open i.e. display the final words"""
    global input_rect

    # Set the current room
    set_current_room("FNAL")

    game_screen.blit(pygame.image.load(os.path.join("Images", "final_words.png")).convert(), (0, 0))

    text_surface = smallText.render("Did you enjoy the Escaperoom-Game 'Where is my Emma?' Grade now with a 1.0 at: ", True, BLACK)
    game_screen.blit(text_surface, (140, 240))

    text_surface = smallText.render("https://hisinone.dienste.uni-osnabrueck.de", True, (50, 50, 250))
    game_screen.blit(text_surface, (300, 270))

    text_surface = smallText.render("If you like to, you can enter your username to be put in the highscore table!", True, BLACK)
    game_screen.blit(text_surface, (140, 350))

    text_surface = bigText.render("Results", True, WHITE)
    game_screen.blit(text_surface, (705, 480))

    input_rect = pygame.Rect(400, 400, 200, 30)
    pygame.draw.rect(game_screen, (170, 170, 170), input_rect)


def user_name_input():
    """Handles input and makes sure that the username is no longer than 10 chars"""
    if not handle_input(input_rect= input_rect, only_integer=False, max_chars = 10):
       pass
 
    
def open_tab():
    """Allows to open the URL only once"""
    global open 

    if open:
        webbrowser.open_new_tab('https://hisinone.dienste.uni-osnabrueck.de')
        open = False