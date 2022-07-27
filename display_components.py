import pygame, os, time

pygame.init()

current_room = "STRT"

# Needed componets
smallText = pygame.font.Font("pokemon.ttf", 20)
bigText = pygame.font.Font("pokemon.ttf", 60)
speech_bubble = pygame.image.load(os.path.join("Images", "speechbubble.png"))
clock = pygame.time.Clock()

# Needed for scipy
click_counter = 0

# All escape-rooms
rooms = ['STRT', 'STRY', 'DOOR', 'BATH', 'CHLD', 'BACK', 'TRES',]
current_room = 'STRT'

# Set width and height (orignial images are 325x200)
DISPLAY_WIDTH = 325 * 3
DISPLAY_HEIGHT = 200 * 3

# Door postions for startscreen (top left corner)
door_1 = [(253, 129)]
door_2 = [(418, 129)]
door_3 = [(582, 129)]

DOOR_WIDTH = 150
DOOR_HEIGHT = 220

SPEECH_BUBBLE_WIDTH = 650
SPEECH_BUBBLE_HEIGHT = 100

SPEECH_BUBBLE_X = 150
SPEECH_BUBBLE_Y = 450

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
game_screen = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])
pygame.display.set_caption('Where is my Emma?')

# Sounds
woosh = pygame.mixer.Sound('Sounds/spruh.mp3')
piep = pygame.mixer.Sound('Sounds/Piep.mp3')
swoosh = pygame.mixer.Sound('Sounds/tresor.mp3')
collect = pygame.mixer.Sound('Sounds/collect.mp3')
opens = pygame.mixer.Sound('Sounds/Tuerknarren.wav')
kling = pygame.mixer.Sound('Sounds/Bier.mp3')
clicking = pygame.mixer.Sound('Sounds/klappe.mp3')
footsteps = pygame.mixer.Sound('Sounds/Running.wav') 
correct = pygame.mixer.Sound('Sounds/correct-6033.wav')
cloth_sound = pygame.mixer.Sound('Sounds/Tuch-schieben.wav')
rclick = pygame.mixer.Sound('Sounds/rclick.mp3')
page = pygame.mixer.Sound('Sounds/page.mp3')
rustle = pygame.mixer.Sound('Sounds/Meeresrauschen.wav')
button_pushed = pygame.mixer.Sound('Sounds/Button.mp3')
bird = pygame.mixer.Sound('Sounds/bird.mp3')
nest = pygame.mixer.Sound('Sounds/nest.mp3')
popping = pygame.mixer.Sound('Sounds/popping.mp3')

 
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def display_loading_screen():
    """Load the frames with rate 3 per second to the backgorund """
    for i in range(3):
        for j in range(7):
            background = pygame.image.load(os.path.join("Images/load", "l" + str(j + 1) + ".jpg")).convert()
            game_screen.blit(background, (0, 0))
            pygame.display.update()
            clock.tick(3)


# Push exit button
def push_exit():
    pygame.mixer.Sound.play(button_pushed)
    game_screen.blit(pygame.image.load(os.path.join("Images", "pushed_exit.png")).convert_alpha(), (0, 0))
    time.sleep(0.3)


# Get our current room by looking at the global situation
def set_current_room(room):
    global current_room
    current_room = room


# Return the current room
def get_current_room():
    return current_room


# Counter increases by 1
def click():
    global click_counter
    click_counter += 1


# Returns the total number of clicks
def get_clicks():
    return click_counter          