import pygame
import sys
from door1 import * 
from display_components import *

def handle_input(screen, go = True, room = 'BACKROOM', input_rect = None):

    user_text = ''

    # create rectangle
    
    # TODO: KOORDINATEN VERALLGEMEINERN
    if input_rect == None:
        input_rect = pygame.Rect(450, 130, 30, 30)
    #pygame.draw.rect(game_screen, (250,250,250), input_rect)

    # color_active stores color which gets active when input box is clicked by user
    color_active = (30,100,30)

    # color_passive store color which is color of input box.
    color_passive = (170,170,170)
    color = color_passive

    active = True
    
    while active and go:
        for event in pygame.event.get():

        # if user types QUIT then the screen will close
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
                    go = not check_input(user_text, screen)

                # Check for backspace
                elif event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]


                # the userinput is accepted if it does not exeed the length of 5 or is a number
                elif len(user_text) < 5:
                    try:
                        # Unicode standard is used for string formation
                        user_text += str (int (event.unicode))
                    except ValueError:
                        pass
        
        # it will set background 
        if room == 'BACKROOM':
            open_backroom(screen)
        else:
            pass 
            #open_endroom(screen)

        if active:
            color = color_active
        else:
            color = color_passive
            
        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(screen, color, input_rect)

        text_surface = smallText.render(user_text, True, (255, 255, 255))
        
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)
        
        # display.flip() will update only a portion of the screen to updated, not full area
        pygame.display.flip()
        
        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        clock.tick(60)

    return go

def check_input(text, game_screen):
    print(text)
    if text == '15':
        open_display(game_screen)
        open_backroom(game_screen)
        game_screen.fill((0,0,0))
        return True
    else:
        print("NO WRONG")
        return False