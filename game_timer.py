"""Manages the realtime displaying of elapsed time"""
from display_components import *

minutes = seconds = 0
go = True


def timer():
    """Displays the elapsed time and clicks on the gamescreen"""  
    global minutes
    global seconds
        
    frame_count = 0

    # Update the timer every second
    frame_rate = 60

    # Loop until the user clicks the close button.
    while go:
        # Manage how fast the screen updates
        total_seconds = frame_count // frame_rate
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time: {0:02}:{1:02} Clicks: {2}".format(minutes, seconds, get_clicks())

        text = small_text.render(output_string, True, BLACK)
        timer_rect = pygame.Rect(450, 12, 200, 30)
        pygame.draw.rect(game_screen, (190, 190, 190), timer_rect)
        game_screen.blit(text, (460, 17))
        frame_count += 1
        clock.tick(frame_rate)
        pygame.display.update()


def get_needed_time():
    """Get the elapsed time at moment of calling this function"""
    return minutes + seconds / 100


def stop_timer():
    """Stops the time displaying"""
    global go
    go = False