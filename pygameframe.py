import pygame, sys, os
from door1 import *
from display_components import *
from handle_userinput import *
from endroom import *
import time

'''Display.flip will update the entire surface. Basically the entire screen. Display.update can just update specific areas of the screen'''

pygame.init()

# all escape-rooms
rooms = ['STRT', 'STRY', 'DOOR', 'BATH', 'CHLD', 'BACK', 'TRES',]
current_room = 'STRT'

# set width and height (orignial images are 325x200)
display_width = 325*3
display_height = 200*3

# door postions for startscreen (top left corner)
door_1 = [(253, 129)]
door_2 = [(418, 129)]
door_3 = [(582,129)]

door_width = 150
door_height = 220

speech_bubble_width = 650
speech_bubble_height = 100

speech_bubble_x = 150
speech_bubble_y = 450

black = (0,0,0)
white = (255,255,255)

# needed componets
game_screen = pygame.display.set_mode([display_width,display_height])
pygame.display.set_caption('Where is my Emma?')

speech_bubble = pygame.image.load(os.path.join("Images", "SpeechBubble2.png"))

clock = pygame.time.Clock()

Screen = 0 # zero is start, one is frist room, two is second room etc.

def open_startscreen(game_screen):
    background = pygame.image.load(os.path.join("Images", "start.png")).convert()
    game_screen.blit(background, (0, 0))
    # smallText = pygame.font.Font("pokemon.ttf",60)
    
    # textSurf, textRect = text_objects('WHERE IS MY EMMA?', smallText)
    #textRect.left
    
    # textRect.bottomleft = ( (70,160) )
    # game_screen.blit(textSurf, textRect)
    pass

def open_3doors(game_screen):
    background = pygame.image.load(os.path.join("Images", "3doors.jpg")).convert()
    game_screen.blit(background, (0, 0))
    game_screen.blit(speech_bubble, (speech_bubble_x,speech_bubble_y))

    smallText = pygame.font.Font("pokemon.ttf",20)
    
    textSurf, textRect = text_objects('Wait... How did I get HERE ?!', smallText)
    #textRect.left
    
    textRect.bottomleft = ( (200,500) )
    game_screen.blit(textSurf, textRect)
    textSurf, textRect = text_objects('This better be a joke... or a dream...', smallText)
    textRect.bottomleft = ( (200,520) )
    game_screen.blit(textSurf, textRect)

def open_story(game_screen):
    pass

def display_loading_screen():

    # load the level to the backgorund
    for i in range(3):
        for j in range(7):
            background = pygame.image.load(os.path.join("Images/load", "l"+str(j+1)+".jpg")).convert()
            game_screen.blit(background, (0, 0))
            pygame.display.update()
            clock.tick(3)

# weil ich es grad nicht besser weiss
cracked_vase = False
#pushed_tuch = False

def button(msg, x,y,w,h,ic,ac):
    global speech_bubble_x
    global speech_bubble_y
    global current_room
    global cracked_vase

    # get postion of mouse
    mouse = pygame.mouse.get_pos()

    # if clicked on a valid button...
    if x+w > mouse[0] > x and y+h > mouse[1] > y:

        print("---------------------------------" +msg + " IS CLICKED ON----------------------------------------")
        pygame.display.update()

        # if you clicked on start, load the first room
        if 'START' in msg and current_room == 'STRT':
            current_room = 'DOOR'
            open_3doors(game_screen)

        # if you clicked on story load the storyscreen
        if 'STORY' in msg and current_room == 'STRT':
            current_room = 'STRY'
            open_story(game_screen)

        # if you clicked on a door open the respective room
        if "DOOR" in msg and (current_room == 'DOOR' or current_room == 'BATHEND'):
            
            if current_room == 'DOOR':
                #display_loading_screen()
                open_door_1(game_screen)
                current_room = 'BATH'
            if current_room == 'BATHEND':
                open_backroom(game_screen)
                current_room = 'BACK'
            
        # if you cracked 'something' in the bath, it will be displayed
        if "CRACK" in msg and current_room == 'BATH':
            if crack_wall(game_screen, mouse[0], mouse[1]):
                current_room = 'BATHEND'

        # if you clicked on the vase it cracks
        if "VASE" in msg and current_room == 'BACK':
            crack_vase(game_screen)
            cracked_vase = True

        # if you clicked on klappe it will open (if you found the key already)
        if "KLAPPE" in msg and current_room == 'BACK' and cracked_vase:
            open_klappe(game_screen)
        
        # if you clicked on tuch it will be pushed
        if "TUCH" in msg and current_room == 'BACK':
            push_tuch(game_screen)

        # if you clicked on the display you can type something in
        if "DISPLAY" in msg and current_room == 'BACK':
            if not handle_input(game_screen):
                current_room = 'BACKEND'

        # if you typed in the right code and click on the display the new room will open
        if current_room == 'BACKEND':
            open_backroom(game_screen)
            if "DISPLAYDOOR" in msg:
                open_endroom(game_screen)
                current_room = 'TRES'

        # if you clicked on the touchpad zoom in
        if 'TOUCHPAD' in msg and current_room == 'TRES':
            zoom_touchpad(game_screen)
            current_room = 'TCHP'

        # if you click on the tresor (after putting in the right code) open the endscreen
        if 'TRESOR' in msg and current_room == 'TRES':
            open_endscreen(game_screen)
            
        # if you click on abort go back and delete your input
        if 'ABORT' in msg and current_room == 'TCHP':
            open_endroom(game_screen, reset_code=True)
            current_room = 'TRES'

        # if you click on check, check if your input was correct
        if 'CHECK' in msg and current_room == 'TCHP':
            if check_for_code():
                open_endroom(game_screen, open_tresor=True)
                current_room = 'TRES'

        # if you clicked on the numberfield save your input
        if 'NUMBERS' in msg and current_room == 'TCHP':
            save_num(game_screen, mouse)
    else:
        pass
        
# set up the game (startscreen)
if  Screen == 0: 
    open_startscreen(game_screen)  

go = True 
##################################################  MAIN  #####################################################################################################################
while go:

    # each interactive event is saved here
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        mouse_click = pygame.mouse.get_pressed()

        # if there was a left-click- check if a valid button was pressed in dependence of the current room
        if mouse_click[0] == 1:
            mouse_pos = pygame.mouse.get_pos()
            
            # on startscreen you can elect between 'START' and 'STORY'
            if current_room == 'STRT':
                button("START", 80, 235, 220, 100,0,0)
                button("STORY", 325, 235, 120, 100,0,0)

            # elect between three doors (each has an own story)
            if current_room == 'DOOR':
                button("DOOR 1", 253, 129, door_width, door_height,0,0)
                button("DOOR 2", 418, 129, door_width, door_height,0,0)
                button("DOOR 3", 582,129, door_width, door_height,0,0)

            # bathroom task buttons
            elif current_room == 'BATH':
                button("CRACK", 10,10, 1000, 1000,0,0)

            # bathroo task solved
            elif current_room == 'BATHEND':
                button("DOOR OPEN", 447,177, 100, 150,0,0)

            # in the backroom you can click on multiple interactive objects
            elif current_room == 'BACK':   
                button("VASE", 809, 120, 90, 80, 0, 0) 
                button("KLAPPE", 338, 425, 300, 100,0,0)
                button("TUCH", 58,168,100,220,0,0)
                button("DISPLAY", 450, 130, 100, 30, 0,0)
                button("DISPLAYDOOR", 313, 44, (124*3), (84*3), 0,0)
            

            # on the touchpad you can click on 'CHECK' 'ABORT' or the number-field
            elif current_room == 'TCHP':
                time.sleep(0.5)
                button('CHECK', 350, 500, 150, 100, 0,0)
                button('ABORT', 550, 500, 150, 100, 0,0)
                button('NUMBERS', 365, 50, 300, 400, 0,0)

            # in the tresor room you can click on the 'TOUCHPAD' or the 'TRESOR' (if you typed in the right code)
            elif current_room == 'TRES':
                button('TOUCHPAD', 600, 300, 80, 80, 0,0)
                if check_for_code():
                    button('TRESOR', 300, 185, 260, 260, 0, 0)


            mouse_pos = pygame.mouse.get_pos()

            # only for testing purposes
            print(mouse_pos)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()