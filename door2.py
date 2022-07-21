import pygame, os
from display_components import *

pointer_1 = 0
pointer_2 = 0
pointer_3 = 0

solved_door2 = False
got_key = False
klappe_open = False
possible_nums = [0,1,2,3,4,5,6,7,8,9]

def open_door_2():

    background = pygame.image.load(os.path.join("Images", "childsroom.png")).convert()
    game_screen.blit(background, (0, 0))
    pygame.display.update()

    #game_screen.blit(speech_bubble, (150,450))
    # smallText = pygame.font.Font("pokemon.ttf",20)
    # textSurf, textRect = text_objects('Wow, that is my old room.', smallText)
    # textRect.bottomleft = ( (190,510) )
    # game_screen.blit(textSurf, textRect)

    display_pointer()
    pygame.display.update()

def display_pointer():

    base_font = pygame.font.Font("pokemon.ttf",70) 
    text_surface = base_font.render(str(possible_nums[pointer_1 % 10]), True, (255, 255, 255)) 
    game_screen.blit(text_surface, (400,110))

    text_surface = base_font.render(str(possible_nums[pointer_2 % 10]), True, (255, 255, 255)) 
    game_screen.blit(text_surface, (470,110))

    text_surface = base_font.render(str(possible_nums[pointer_3 % 10]), True, (255, 255, 255)) 
    game_screen.blit(text_surface, (540,110))

    check_code()

def check_code():
    global solved_door2
    
    if str(possible_nums[pointer_1 % 10]) + str(possible_nums[pointer_2 % 10]) + str(possible_nums[pointer_3 % 10]) == '420':
        solved_door2 = True
        game_screen.blit(pygame.image.load(os.path.join("Images", "wall.png")).convert_alpha(), (0, 0))

    pygame.display.update()


def open_book():
    
    game_screen.blit(pygame.image.load(os.path.join("Images", "book.png")).convert(), (0, 0))
    pygame.display.update()

    smallText = pygame.font.Font("pokemon.ttf",30)

    # first hint
    textSurf, textRect = text_objects('6  8  0', smallText)
    textRect.bottomleft = ( (280,80) )
    game_screen.blit(textSurf, textRect)

    
    textSurf, textRect = text_objects('One number is correct', smallText)
    textRect.bottomleft = ( (180,110) )
    game_screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects('and is postioned right.', smallText)
    textRect.bottomleft = ( (180,140) )
    game_screen.blit(textSurf, textRect)

    # second

    textSurf, textRect = text_objects('6  1  2', smallText)
    textRect.bottomleft = ( (640,125) )
    game_screen.blit(textSurf, textRect)

    
    textSurf, textRect = text_objects('One number is correct', smallText)
    textRect.bottomleft = ( (540,155) )
    game_screen.blit(textSurf, textRect)


    textSurf, textRect = text_objects('but is postioned false.', smallText)
    
    textRect.bottomleft = ( (540,185) )
    game_screen.blit(textSurf, textRect)

    # third

    textSurf, textRect = text_objects('0  4  6', smallText)
    textRect.bottomleft = ( (280,240) )
    game_screen.blit(textSurf, textRect)

    
    textSurf, textRect = text_objects('Two numbers are correct', smallText)
    textRect.bottomleft = ( (170,270) )
    game_screen.blit(textSurf, textRect)


    textSurf, textRect = text_objects('but postioned false.', smallText)
    
    textRect.bottomleft = ( (180,300) )
    game_screen.blit(textSurf, textRect)

    # fourth
    textSurf, textRect = text_objects('7  3  8', smallText)
    textRect.bottomleft = ( (640,285) )
    game_screen.blit(textSurf, textRect)
 
    textSurf, textRect = text_objects('Nothing is correct.', smallText)
    textRect.bottomleft = ( (540,315) )
    game_screen.blit(textSurf, textRect)

    # fifth
    textSurf, textRect = text_objects('8  7  4', smallText)
    textRect.bottomleft = ( (280,400) )
    game_screen.blit(textSurf, textRect)

    
    textSurf, textRect = text_objects('One number is correct', smallText)
    textRect.bottomleft = ( (180,430) )
    game_screen.blit(textSurf, textRect)


    textSurf, textRect = text_objects('but is postioned false.', smallText)
    
    textRect.bottomleft = ( (180,460) )

    game_screen.blit(textSurf, textRect)

    # question:

    textSurf, textRect = text_objects('What is the correct code?', smallText)
    textRect.bottomleft = ( (340,560) )
    game_screen.blit(textSurf, textRect)

def rotate_number(field):

    global pointer_1 
    global pointer_2 
    global pointer_3 

    if field >= 26 and field <= 30:
        pointer_1 += 1  
        
    elif field >= 30 and field <= 35:
        pointer_2 += 1
             
    else:
       pointer_3 += 1
       

    open_door_2()
    display_pointer()


def open_garden():

    if klappe_open:
        game_screen.blit(pygame.image.load(os.path.join("Images", "garden.png")).convert(), (0, 0))
        
    else:
        game_screen.blit(pygame.image.load(os.path.join("Images", "garden_closed.png")).convert(), (0, 0))   
    
    pygame.display.update()

def open_birdshouse():
   
    if got_key:
        background = pygame.image.load(os.path.join("Images", "birdshouse_collectedkey.png")).convert()
        game_screen.blit(background, (0, 0))
    else:
        background = pygame.image.load(os.path.join("Images", "birdshouse.png")).convert()
        game_screen.blit(background, (0, 0))

    pygame.display.update()

def get_key():
    global got_key
    got_key = True
    open_birdshouse()

def open_klappe_garden():
    global klappe_open
    klappe_open = True
    open_garden()

       
    
    

    





