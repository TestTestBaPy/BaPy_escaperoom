"""This file manages status variables (e.g. current room) and offers constants and functions for the majority of the other files"""
import pygame, os, time

pygame.init()

# Needed componets
small_text = pygame.font.Font("pokemon.ttf", 20)
big_text = pygame.font.Font("pokemon.ttf", 60)
speech_bubble = pygame.image.load(os.path.join("Images", "speechbubble.png"))
clock = pygame.time.Clock()

# Needed for scipy
click_counter = 0

# The current room is saved here
current_room = 'STRT'

# Set width and height (original images are 325x200)
DISPLAY_WIDTH = 325 * 3
DISPLAY_HEIGHT = 200 * 3

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
PIEP = pygame.mixer.Sound('Sounds/piep.mp3')
SWOOSH = pygame.mixer.Sound('Sounds/tresor.mp3')
COLLECT = pygame.mixer.Sound('Sounds/collect.mp3')
OPENS = pygame.mixer.Sound('Sounds/Tuerknarren.wav')
KLING = pygame.mixer.Sound('Sounds/Bier.mp3')
CLICKING = pygame.mixer.Sound('Sounds/klappe.mp3')
FOOTSTEPS = pygame.mixer.Sound('Sounds/Running.wav') 
CORRECT = pygame.mixer.Sound('Sounds/correct-6033.wav')
CLOTH_SOUND = pygame.mixer.Sound('Sounds/Tuch-schieben.wav')
RCLICK = pygame.mixer.Sound('Sounds/rclick.mp3')
PAGE = pygame.mixer.Sound('Sounds/page.mp3')
RUSTLE = pygame.mixer.Sound('Sounds/Meeresrauschen.wav')
BUTTON_PUSHED = pygame.mixer.Sound('Sounds/Button.mp3')
BIRD = pygame.mixer.Sound('Sounds/bird.mp3')
NEST = pygame.mixer.Sound('Sounds/nest.mp3')
POPPING = pygame.mixer.Sound('Sounds/popping.mp3')

 
def text_objects(text, font):
    """Creates a tailored textsurface.
    Args:
      text: the Text that should be displayed
      font: the font in which the text should be displayed 
    Returns:
      A textsurface that contains the given text in the given font
    """
    textSurface = font.render(text, True, BLACK)
    return textSurface


def display_loading_screen():
    """Load the frames with rate 3 per second to the backgorund"""
    for i in range(3):
        for j in range(7):
            background = pygame.image.load(os.path.join("Images/load", "l" + str(j + 1) + ".jpg")).convert()
            game_screen.blit(background, (0, 0))
            pygame.display.update()
            clock.tick(3)


def push_exit():
    """Pushes the exit button"""
    pygame.mixer.Sound.play(BUTTON_PUSHED)
    game_screen.blit(pygame.image.load(os.path.join("Images", "pushed_exit.png")).convert_alpha(), (0, 0))
    time.sleep(0.3)


def set_current_room(room):
    """Sets the current room by looking at the global situation
    Args:
      room: string of the shortform of the room that is entered  
    """
    global current_room
    current_room = room


def get_current_room():
    """Get current room"""
    return current_room


def click():
    """Increases the counter by one"""
    global click_counter
    click_counter += 1


def get_clicks():
    """Get amount of clicks"""
    return click_counter          