import pygame, sys, os
from door1 import *
from display_components import *
'''Display.flip will update the entire surface. Basically the entire screen. Display.update can just update specific areas of the screen'''

pygame.init()

# set width and height (orignial images are 325x200)
display_width = 325*3
display_height = 200*3

# door postions for startscreen (top left corner)
door_1 = [(253, 129)]
door_2 = [(418, 129)]
door_3 = [(582,129)]

door_width = 150
door_height = 220

black = (0,0,0)
white = (255,255,255)

# needed componets
game_screen = pygame.display.set_mode([display_width,display_height])
pygame.display.set_caption('Where is my Emma?')
background = pygame.image.load(os.path.join("Images", "3doors.jpg")).convert()
speech_bubble = pygame.image.load(os.path.join("Images", "SpeechBubble2.png"))

clock = pygame.time.Clock()

Screen = 0 

def display_loading_screen():
     # load the level to the backgorund
    for i in range(3):
        background = pygame.image.load(os.path.join("Images/load", "l1.jpg")).convert()
        game_screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(5)
        background = pygame.image.load(os.path.join("Images/load", "l2.jpg")).convert()
        game_screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(5)
        background = pygame.image.load(os.path.join("Images/load", "l3.jpg")).convert()
        game_screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(5)
        background = pygame.image.load(os.path.join("Images/load", "l4.jpg")).convert()
        game_screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(5)
        background = pygame.image.load(os.path.join("Images/load", "l5.jpg")).convert()
        game_screen.blit(background, (0, 0))
        clock.tick(5)
        background = pygame.image.load(os.path.join("Images/load", "l2.jpg")).convert()
        game_screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(2)
        background = pygame.image.load(os.path.join("Images/load", "l1.jpg")).convert()
        game_screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(2)


def button(msg, x,y,w,h,ic,ac):

    # get postion of mouse
    mouse = pygame.mouse.get_pos()

    # if clicked on a valid button...
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        print("FUNCTION: "+ msg + "IS OPENING")

        # speech_rect = speech_bubble.get_rect()
        # speech_rect.x = 150
        # speech_rect.y = 300
        # pygame.display.update()
        smallText = pygame.font.Font("pokemon.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        game_screen.blit(textSurf, textRect)
       
        display_loading_screen()
        open_door_1(game_screen)
        #pygame.draw.rect(game_screen, ac,(x,y,w,h))
    else:
        print("missed on door")
        #pygame.draw.rect(game_screen, ic,(x,y,w,h))




# set up the game
if  Screen == 0:   
        game_screen.blit(background, (0, 0))
        game_screen.blit(speech_bubble, (150,450))

        #game_screen.fill((255,255,255))
        #x = pygame.font.get_fonts()
  
        # c = 0
        # grenze_unten = 179
        # grenze_oben = 181
        # for i in x:
            
        #     if c < grenze_oben and c > grenze_unten:
        #         print("TRUE________________________________")
        #         largeText = pygame.font.SysFont('OCR A Extended', 60)
        #         #largeText = pygame.font.Font(pygame.font.SysFont+".ttf",20)
        #         TextSurf, TextRect = text_objects("Wait... How did I get here??...", largeText)
        #         TextRect.center = ((240),( 20 + (  c-grenze_unten) * 20))
        #         game_screen.blit(TextSurf, TextRect)
        #     else:
        #         pass
            
        #     c += 1


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

            button("DOOR 1", 253, 129, door_width, door_height,0,0)
            button("DOOR 2", 418, 129, door_width, door_height,0,0)
            button("DOOR 3", 582,129, door_width, door_height,0,0)
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