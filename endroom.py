import pygame, os, time, math, webbrowser
from display_components import *
from handle_userinput import handle_input

number_sequence = ''
input_rect = None
open = True


def open_endroom(reset_code = False, open_tresor = False):
    """Opens i.e. displays the endroom with the tresor.
        Args:
            reset_code indicates if the current code should be resetted
            open_tresor indicates if the tresor was already open so it can be displayed 
                        correctly
    """
    #Ahhh
    # set the current room
    set_current_room("TRES")
    
    global number_sequence
   
    # alternative code have alternative endings
    if number_sequence == '1407':
        game_screen.blit(pygame.image.load(os.path.join("Images", "emma_dead.png")).convert(), (0, 0))
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "emma_alive.png")).convert(), (0, 0))

    if reset_code:
        number_sequence = ''

    # if the tresor was (not) opened (do not) display the door
    if not open_tresor:
        safe_door = pygame.image.load(os.path.join("Images", "tresor_closed.png"))
        game_screen.blit(safe_door,(0, 0))
    else:
        safe_door = pygame.image.load(os.path.join("Images", "tresor_opened.png"))
        game_screen.blit(safe_door,(0, 0))

    pygame.display.update()


def zoom_touchpad():
    """Zooms in on the touchpad so the user can type in a code
    """
    # set the current room
    set_current_room("TCHP")

    game_screen.blit(pygame.image.load(os.path.join("Images", "pad.png")).convert(), (0, 0))
    input_rect = pygame.Rect(50, 150, 130, 130)
    pygame.draw.rect(game_screen, (50, 150, 100), input_rect)
    pygame.display.update()


def check_for_code():
    """Returns wheter on of the right codes was enetered"""
    return number_sequence == '1407' or number_sequence == '1532'


def open_tresor():
    """Opens the tresor with the open_endroom function
    """
    pygame.mixer.Sound.set_volume(swoosh, 0.2)
    pygame.mixer.Sound.play(swoosh)
    open_endroom(open_tresor = True)


def save_num(mouse):
    """Safes the inputted numbers to be able to check and display the entered code
    """
    global number_sequence

    if len(number_sequence) < 4:   
        x = mouse[0]
        y = mouse[1]

        # perform simple division to decide which of the numbers was clicked
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

        text_surface = bigText.render(number_sequence, True, (255, 255, 255))
            
        # display the code
        game_screen.blit(text_surface, (50 + 5, 150 + 5))


def open_endscreen(clicked_on_exit = False):
    """Opens i.e. displays the endscreen
        Args:
            clicked_on_exit if set to True simulates a button click on "EXIT"
    """
    # set the current room
    set_current_room("CALL")

    if clicked_on_exit:
        push_exit()   
    
    # display alternative endings based on the entered code
    if number_sequence == '1407':

        game_screen.blit(pygame.image.load(os.path.join("Images", "call_buy.png")).convert(), (0, 0))
   
        text_surface = smallText.render("Forget the ealier text... It was just because of the stress from the funeral. ", True, (0, 0, 0))
        game_screen.blit(text_surface, (180, 90))

        text_surface = smallText.render("Can you help a man out? Yes, usual place. Okay, see you soon. Thank you.", True, (0, 0, 0))
        game_screen.blit(text_surface, (180, 120))
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "call_quit.png")).convert(), (0, 0))

        text_surface = smallText.render("Forget the ealier text... It was just because of the stress from the funeral. ", True, (0, 0, 0))
        game_screen.blit(text_surface, (180, 90))

        text_surface = smallText.render("Please delete my number. Yes, I'm quitting. Have a good life my firend.", True, (0, 0, 0))
        game_screen.blit(text_surface, (180, 120))

    # display the monologue
    textSurf, textRect = text_objects("Hey, Escopub...", smallText)
    textRect.bottomleft = ((210, 490))
    game_screen.blit(textSurf, textRect)


def open_final_words():
    """Open i.e. display the final words
    """
    global input_rect

    # set the current room
    set_current_room("FNAL")

    game_screen.blit(pygame.image.load(os.path.join("Images", "final_words.png")).convert(), (0, 0))

    text_surface = smallText.render("Did you enjoy the Escaperoom-Game 'Where is my Emma?' Grade now with a 1.0 at: ", True, (0, 0, 0))
    game_screen.blit(text_surface, (140, 240))

    text_surface = smallText.render("https://hisinone.dienste.uni-osnabrueck.de", True, (50, 50, 250))
    game_screen.blit(text_surface, (300, 270))

    text_surface = smallText.render("If you like to, you can enter your username to be put in the highscore table!", True, (0, 0, 0))
    game_screen.blit(text_surface, (140, 350))

    text_surface = bigText.render("Results", True, white)
    game_screen.blit(text_surface, (705, 480))

    input_rect = pygame.Rect(400, 400, 200, 30)
    pygame.draw.rect(game_screen, (170, 170, 170), input_rect)


def user_name_input():
    """Handles input and makes sure that the username is no longer than 10 chars
    """
    if not handle_input(input_rect= input_rect, only_integer=False, max_chars = 10):
       pass
 
    
def open_tab():
    """Allows to open the URL only once
    """
    global open 

    if open:
        webbrowser.open_new_tab('https://hisinone.dienste.uni-osnabrueck.de')
        open = False