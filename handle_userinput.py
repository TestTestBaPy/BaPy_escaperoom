import pygame, sys
from display_components import *

user_text = ''
def handle_input(go = True, active = True, input_rect = None, max_chars = 10, only_integer = False):
    """This function takes an arbitrary pygame rectangle and uses it as a input text box
        Args:
            input_rect the pygame-rectangle to display the inputted text on
            max_chars limits the amount of chars to type in
            only_integer if set to true, only integers are accepted
        Returns: 
    """

    global user_text

    # color_active stores color which gets active when input box is clicked by user
    color_active = (30,100,30)

    # color_passive store color which is color of input box.
    color_passive = (170,170,170)
    color = color_passive

    active = True
    
    while active and go:
        for event in pygame.event.get():

        # if user types QUIT (while the input field is active) then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # if the user clicked on the rect it gets active
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN: 
                    active = False 
                    go = False # go is set to false because the input needs to be check (when hit return)

                # Check for backspace
                elif event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]


                # the userinput is accepted if it does not exeed the length of 5 or is a number
                elif len(user_text) < max_chars:
                    try:
                        # Unicode standard is used for string formation
                        if only_integer:
                            user_text += str (int(event.unicode))
                        else:
                            user_text += str ((event.unicode))

                    except ValueError:
                        pass
        
        # it will set background 
        
        # if room == 'BACKROOM':
        #     open_backroom()
        # else:
        #     pass 
        #     #open_endroom(screen)

        if active:
            color = color_active
        else:
            color = color_passive
            
        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(game_screen, color, input_rect)
        display_num_sequence(input_rect)
        
        # display.flip() will update only a portion of the screen to updated, not full area
        pygame.display.flip()

    return go

def display_num_sequence(input_rect):
   

    text_surface = smallText.render(user_text, True, (255, 255, 255)) 
   
    # render at position stated in arguments
    game_screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    
    # display.flip() will update only a portion of the screen to updated, not full area
    pygame.display.flip()

def get_input_text():
    return user_text

def reset_text():
    global user_text
    user_text = ''
