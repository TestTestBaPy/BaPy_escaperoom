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
        print("FUNCTION: "+ msg + " IS OPENING")

        print(current_room)
        # speech_rect = speech_bubble.get_rect()
        # speech_rect.x = 150
        # speech_rect.y = 300
        pygame.display.update()
        if 'START' in msg and current_room == 'STRT':
            current_room = 'DOOR'
            open_3doors(game_screen)

        if 'STORY' in msg and current_room == 'STRT':
            current_room = 'STRY'
            open_story(game_screen)

        if "DOOR" in msg and (current_room == 'DOOR' or current_room == 'BATHEND'):
            
            if current_room == 'DOOR':
                #display_loading_screen()
                open_door_1(game_screen)
                current_room = 'BATH'
            if current_room == 'BATHEND':
                open_backroom(game_screen)
                current_room = 'BACK'
        if "CRACK" in msg and current_room == 'BATH':
            if crack_wall(game_screen, mouse[0], mouse[1]):
                current_room = 'BATHEND'

        if "VASE" in msg and current_room == 'BACK':
            crack_vase(game_screen)
            cracked_vase = True

        if "KLAPPE" in msg and current_room == 'BACK' and cracked_vase:
            print('ÖFFEN KLAPEE')
            open_klappe(game_screen)
        
        if "TUCH" in msg and current_room == 'BACK':
            print('SCHIEB TUCH')
            push_tuch(game_screen)

        if "DISPLAY" in msg and current_room == 'BACK':
            print("get user input NOw")
            if not handle_input(game_screen):
                print('i set current room on BACVKEND')
                current_room = 'BACKEND'

        if current_room == 'BACKEND':
            open_backroom(game_screen)
            if "DISPLAYDOOR" in msg:
                open_endroom(game_screen)
                current_room = 'TRES'

        if 'TOUCHPAD' in msg and current_room == 'TRES':
            zoom_touchpad(game_screen)
            current_room = 'TCHP'

        if 'TRESOR' in msg and current_room == 'TRES':
            open_endscreen(game_screen)
            

        if 'ABORT' in msg and current_room == 'TCHP':
            open_endroom(game_screen, reset_code=True)
            current_room = 'TRES'

        if 'CHECK' in msg and current_room == 'TCHP':
            if check_for_code():
                open_endroom(game_screen, open_tresor=True)
                current_room = 'TRES'

        if 'NUMBERS' in msg and current_room == 'TCHP':
            save_num(game_screen, mouse)
    else:
        pass
        #print("missed on door")
        
# set up the game (startscreen)
if  Screen == 0: 
    open_startscreen(game_screen)  
    #open_3doors(game_screen)
        
        #screen.blit(Dog1, (0, 0))
        #pygame.display.update()
        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             sys.exit()
        #             pygame.display.update()

go = True 
##################################################  MAIN  #####################################################################################################################
while go:

    # tastatur spieleingaben
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        mouse_click = pygame.mouse.get_pressed()
        

        if mouse_click[0] == 1:
            mouse_pos = pygame.mouse.get_pos()
            
            if current_room == 'STRT':
                # (83, 235) (306, 310)
                # (81, 235) (306, 308)
                button("START", 80, 235, 220, 100,0,0)
                # (325, 236) (523, 310)
                button("STORY", 325, 235, 120, 100,0,0)
            if current_room == 'DOOR':
                button("DOOR 1", 253, 129, door_width, door_height,0,0)
                button("DOOR 2", 418, 129, door_width, door_height,0,0)
                button("DOOR 3", 582,129, door_width, door_height,0,0)
            elif current_room == 'BATH':
                button("CRACK", 10,10, 1000, 1000,0,0)
            elif current_room == 'BATHEND':
                button("DOOR OPEN", 447,177, 100, 150,0,0)

            elif current_room == 'BACK':

                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                #(809, 120)(891, 205)
                button("VASE", 809, 120, 90, 80, 0, 0)
                # (338, 425) (625, 516)
                button("KLAPPE", 338, 425, 300, 100,0,0)
                #button("", 809, 120, 90, 80, 0, 0)
                #(59, 168)(163, 381)
                button("TUCH", 58,168,100,220,0,0)

                # (623, 261) (451, 132) 450, 130
                button("DISPLAY", 450, 130, 100, 30, 0,0)
                #button("DISPLAY", 58,168,100,220,0,0)

                button("DISPLAYDOOR", 313, 44, (124*3), (84*3), 0,0)
            

            elif current_room == 'TCHP':
                
                time.sleep(0.5)
                # (365, 510) (465, 596)
                button('CHECK', 350, 500, 150, 100, 0,0)
                # (559, 515) (663, 597)
                button('ABORT', 550, 500, 150, 100, 0,0)
                # (368, 49) (662, 452)
                button('NUMBERS', 365, 50, 300, 400, 0,0)

            elif current_room == 'TRES':
                button('TOUCHPAD', 600, 300, 80, 80, 0,0)
                # (308, 185) (559, 441)
                if check_for_code():
                    print("CODE IS RICHTIG!!!")
                    button('TRESOR', 300, 185, 260, 260, 0, 0)


                

            # TODO if click on wanted object do wanted function
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            #go = False

    #print(event)
    
    #pygame.draw.rect(game_screen, (255,255,0), (x,y,width,height))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
#sys.exit()