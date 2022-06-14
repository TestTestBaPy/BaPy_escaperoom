import pygame, sys, os
from door1 import *
from display_components import *
'''Display.flip will update the entire surface. Basically the entire screen. Display.update can just update specific areas of the screen'''

pygame.init()

# all escape-rooms
rooms = ['BATH', 'STRT', 'CHLD', 'BACK']
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
background = pygame.image.load(os.path.join("Images", "3doors.jpg")).convert()
speech_bubble = pygame.image.load(os.path.join("Images", "SpeechBubble2.png"))

clock = pygame.time.Clock()

Screen = 0 # zero is start, one is frist room, two is second room etc.

def display_loading_screen():
     # load the level to the backgorund
    for i in range(3):
        for j in range(7):
            background = pygame.image.load(os.path.join("Images/load", "l"+str(j+1)+".jpg")).convert()
            game_screen.blit(background, (0, 0))
            pygame.display.update()
            clock.tick(3)

def button(msg, x,y,w,h,ic,ac):
    global speech_bubble_x
    global speech_bubble_y
    global current_room

    # get postion of mouse
    mouse = pygame.mouse.get_pos()

    # if clicked on a valid button...
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        print("FUNCTION: "+ msg + " IS OPENING")

        # speech_rect = speech_bubble.get_rect()
        # speech_rect.x = 150
        # speech_rect.y = 300
        # pygame.display.update()
        if "DOOR" in msg and current_room == 'STRT':
            
        
            #display_loading_screen()
            open_door_1(game_screen)
            current_room = 'BATH'
        if "CRACK" in msg and current_room == 'BATH':
            crack_wall(game_screen, mouse[0], mouse[1])
    else:
        pass
        #print("missed on door")
        
# set up the game
if  Screen == 0:   
        game_screen.blit(background, (0, 0))
        game_screen.blit(speech_bubble, (speech_bubble_x,speech_bubble_y))

       

        smallText = pygame.font.Font("pokemon.ttf",20)
        #smallText = pygame.font.SysFont('ARCADECLASSIC.ttf', 20)
        textSurf, textRect = text_objects('Wait... How did I get HERE ?!', smallText)
        #textRect.left
        
        textRect.bottomleft = ( (200,500) )
        game_screen.blit(textSurf, textRect)
        textSurf, textRect = text_objects('This better be a joke... or a dream...', smallText)
        textRect.bottomleft = ( (200,520) )
        game_screen.blit(textSurf, textRect)
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
        #if mouse_pressed[pygame.MOUSEBUTTONDOWN]:
            #print("PRESSSED NMOUSE")
            mouse_pos = pygame.mouse.get_pos()

            button("DOOR 1", 253, 129, door_width, door_height,0,0)
            button("DOOR 2", 418, 129, door_width, door_height,0,0)
            button("DOOR 3", 582,129, door_width, door_height,0,0)
            button("CRACK", 10,10, 1000, 1000,0,0)

            # TODO if click on wanted object do wanted function
            #mouse_pos = pygame.mouse.get_pos()
            #print(mouse_pos)
            #go = False


    #print(event)
    
    #pygame.draw.rect(game_screen, (255,255,0), (x,y,width,height))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
#sys.exit()