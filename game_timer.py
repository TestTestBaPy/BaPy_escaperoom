"""
 Show how to put a timer on the screen.
 
"""
from display_components import *
import pygame
 
 
# Loop until the user clicks the close button.

def timer():
    pygame.init()
    font = pygame.font.Font(None, 25)
        
    frame_count = 0
    frame_rate = 60
        
    while True:

    
        
        # Used to manage how fast the screen updates
        #clock = pygame.time.Clock()
        
        
        total_seconds = frame_count // frame_rate

        minutes = total_seconds // 60

        seconds = total_seconds % 60

        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

        text = font.render(output_string, True, black)
        timer_rect = pygame.Rect(450, 15, 100, 30)
        pygame.draw.rect(game_screen, (190,190,190), timer_rect)
        game_screen.blit(text, (450, 20))

        frame_count += 1
        

        
        clock.tick(frame_rate)

        
        pygame.display.update()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
    pygame.quit()