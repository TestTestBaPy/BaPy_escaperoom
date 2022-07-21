import pygame, os

pygame.init()

smallText = pygame.font.Font("pokemon.ttf",20)
bigText = pygame.font.Font("pokemon.ttf",60)
speech_bubble = pygame.image.load(os.path.join("Images", "speechbubble.png"))
clock = pygame.time.Clock()
# needed componets
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
game_screen = pygame.display.set_mode([display_width,display_height])
pygame.display.set_caption('Where is my Emma?')

def text_objects(text,font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def display_loading_screen():

    # load the frames with rate 3 per second to the backgorund
    for i in range(3):
        for j in range(7):
            background = pygame.image.load(os.path.join("Images/load", "l"+str(j+1)+".jpg")).convert()
            game_screen.blit(background, (0, 0))
            pygame.display.update()
            clock.tick(3)

            