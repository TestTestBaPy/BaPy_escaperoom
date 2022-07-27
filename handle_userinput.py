import pygame, sys
from display_components import *

user_text = ''


def handle_input(go = True, active = True, input_rect = None, max_chars = 10, only_integer = False):
    """This function takes an arbitrary pygame rectangle and uses it as an input textbox
    Args:
      input_rect:
        The pygame-rectangle to display the inputted text on
      max_chars:
        Limits the amount of chars to type in
      only_integer:
        If set to true, only integers are accepted
    Returns: 
      go: 
        go is eighter set to false in the arguments or if the input needs to be checked.
        Go is true if the textfield is deactivated. 
    """
    global user_text

    # Color_active stores color which gets active when input box is clicked by user
    color_active = (30, 100, 30)

    # Color_passive store color which is color of input box.
    color_passive = (170, 170, 170)
    color = color_passive

    active = True
    
    while active and go:
        for event in pygame.event.get():

        # If user types QUIT (while the input field is active) then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # If the user clicked on the rect it gets active
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN: 
                    active = False 
                    go = False 

                # Check for backspace
                elif event.key == pygame.K_BACKSPACE:

                    # Get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # The userinput is accepted if it does not exeed the length of 5 or is a number
                elif len(user_text) < max_chars:
                    try:
                        # Unicode standard is used for string formation
                        if only_integer:
                            user_text += str(int(event.unicode))
                        else:
                            user_text += str((event.unicode))

                    except ValueError:
                        pass

        if active:
            color = color_active
        else:
            color = color_passive
            
        # Draw rectangle and argument passed which should be on screen
        pygame.draw.rect(game_screen, color, input_rect)
        display_num_sequence(input_rect)
        
        # display.flip() will update only a portion of the screen to updated, not full area
        pygame.display.flip()

    return go


def display_num_sequence(input_rect):
    text_surface = small_text.render(user_text, True, WHITE) 
   
    # Render at position stated in arguments
    game_screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    
    # display.flip() will update only a portion of the screen to updated, not full area
    pygame.display.flip()


def get_input_text():
    return user_text


def reset_text():
    global user_text
    user_text = ''