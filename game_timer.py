"""
 Show how to put a timer on the screen.
 
"""
from display_components import *
import pygame

minutes = seconds = 0
 
 
# Loop until the user clicks the close button.

def timer():
    pygame.init()
    
    global minutes
    global seconds
        
    frame_count = 0
    frame_rate = 60
        
    while True:

    
        
        # Used to manage how fast the screen updates
        #clock = pygame.time.Clock()
        
        
        total_seconds = frame_count // frame_rate

        minutes = total_seconds // 60

        seconds = total_seconds % 60

        output_string = "Time: {0:02}:{1:02} Clicks: {2}".format(minutes, seconds, get_clicks())

        text = smallText.render(output_string, True, black)
        timer_rect = pygame.Rect(450, 12, 200, 30)
        pygame.draw.rect(game_screen, (190,190,190), timer_rect)
        game_screen.blit(text, (460, 17))

        frame_count += 1
        

        
        clock.tick(frame_rate)

        
        pygame.display.update()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
    pygame.quit()

def get_needed_time():
    return str(minutes) + ':' + str(seconds)