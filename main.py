"""Executable file that contains the main loop in order to keep the game running. 
Manages the interactivity with mouse click and checks if a valid button was clicked
and forwards onto the respective functions.
"""
import pygame, sys, time
from threading import Thread
from door1 import *
from door2 import *
from door3 import *
from display_components import *
from endscreen import *
from startscreen import *
from resultscreen import *
from game_timer import *

# Initialze pygame first
pygame.init()

# First of all we want some nice backgroundmusic, therefore we load a mp3, 
# we want that the music repeats the whole time, so we set -1 and we set our volume to 0.1
pygame.mixer.music.load('Sounds/columbianische machenschaften.mp3')
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(.1)


def button(msg, x, y, w, h):
    """This universal function simulates a button so if the click is in the given coordinates and width/height 
       of the 'button' the respective function will be called.
    Args:
      msg: short description of the button-field to check (helps to decide how to handle)
      x: the x-coordinate of the upper right corner of the button field
      y: the y-coordinate of the upper right corner of the button field
      w: the width of the button 
      h: the height of the button
    """ 
    global current_room

    # Get postion of mouse to decide wheter the button was clicked
    mouse = pygame.mouse.get_pos()

    # If clicked on a valid button...
    if x + w > mouse[0] > x and y + h > mouse[1] > y:

        current_room = get_current_room()

        # In the room "CALL" there is only one button, so no need to check for msg
        if current_room == "CALL":
            open_endscreen(True)
            pygame.display.update()
            time.sleep(0.3)
            open_final_words()

        # If clicked on name field the user can enter his or her name
        if "NAME" in msg:
           user_name_input()
                
        # If clicked on the url open it
        elif "URL" in msg:
            open_tab()     

        # If you want to see scipy-results save the data and open it
        elif "SCIPY" in msg:
            save_user_data()
            open_scipy_plot()
            stop_timer() 

        # Go back to startscreen (STRY has only one button)
        elif current_room == "STRY":
            push_exit()
            open_startscreen()

        # If book was closen open the room again
        elif current_room == "BOOK":
            push_exit()
            open_childsroom()

        # If clicked on start, load the first room
        elif "START" in msg:
            open_3doors()

        # If clicked on story load the storyscreen
        elif 'STORY' in msg and current_room == 'STRT':
            open_story()

        # If clicked on a door open the respective room
        elif "DOOR" in msg:
            
            if current_room == 'DOOR':     
                pygame.mixer.Sound.set_volume(OPENS, 0.1)
                pygame.mixer.Sound.play(OPENS)
                if "1" in msg:
                    open_bathroom()
                elif "2" in msg:
                    open_childsroom()
                else:
                    open_door_3()
               
            elif current_room == "BATHEND":
                pygame.mixer.Sound.play(FOOTSTEPS) 
                open_backroom()
            
            elif current_room == "CHLD":
                open_garden()

            elif current_room == "GARD":

                if not get_trap_open() and get_got_key():
                    open_trap_garden()
                    
                elif get_trap_open():
                    open_endroom()
                    
            elif "DISPLAYDOOR" in msg:
                open_endroom()

        # If cracked 'something' in the bath, it will be displayed
        elif "CRACK" in msg:
            crack_wall(mouse[0], mouse[1])
       
        # If clicked on the vase it cracks
        elif "VASE" in msg:
            crack_vase()

        # If clicked on trapdoor it will open (if you found the key already)
        elif "KLAPPE" in msg:
            open_trap()
        
        # If clicked on cloth it will be pushed
        elif "TUCH" in msg:
            push_cloth()

        # If click on the safe (after putting in the right code) open the endscreen
        elif "TRESOR" in msg:
            open_endscreen()

        # If clicked on the touchpad zoom in
        elif "TOUCHPAD" in msg:
            zoom_touchpad()
            
        # If clicked on abort go back and delete input
        elif "ABORT" in msg:
            open_endroom(reset_code=True)

        # If clicked on check, check if input was correct
        elif "CHECK" in msg and current_room == "TCHP":
            if check_for_code():
                open_safe()

        # If clicked on the numberfield, save input
        elif "NUMBERS" in msg and current_room == "TCHP":
            pygame.mixer.Sound.set_volume(PIEP, 0.1)
            pygame.mixer.Sound.play(PIEP)
            save_num(mouse)
        
        # If clicked on book, display it
        elif "BOOK" in msg:
            open_book()

        # If clicked on exit in the birdhouse, open the garden
        elif "EXIT" in msg and current_room == "BIRD":
            push_exit()
            open_garden()

        # If clicked on blackboard
        elif "TAFEL" in msg:
            rotate_number((mouse[0] / 15))

        # If clicked on the garbagecan
        elif "TRASH" in msg:
            open_flyer()

        # If you are in the trashcan you can only go back
        elif current_room == "TRAS":
            push_exit()
            open_childsroom()
 
        # If clicked on, open the birdhouse
        elif "BIRD" in msg:
            open_birdhouse()

        # If clicked on the key collect it
        elif "KEY" in msg:
            get_key()

        # If clicked on nest collect it
        elif "NEST" in msg:
            remove_nest()  
            
        # If you clicked on the display you can type something in
        elif "DISPLAY" in msg and current_room == "BACK":
            if not input_correct(True) and check_input():
                display_solved()
                reset_text()
        
           
# Set up, the game (here you can decide in which room you want to start) default should be open_startscreen()
open_startscreen()

frame_count = 0
frame_rate = 60

# This thread is needed because else the timer (e.g. if put in main-loop) does not perform in real time
t1 = Thread(target = timer)
# Set to daemon so when the user clicks on exit the timer-thread is closed as well
t1.daemon = True
# Start the thread
t1.start()

while True:
    # Each interactive event is saved here
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        mouse_click = pygame.mouse.get_pressed()

        # If there was a left-click (or right-click), check if a valid button was pressed in dependence of the current room
        if event.type == pygame.MOUSEBUTTONUP:   
            click()
            current_room = get_current_room()
            
            # At the startscreen you can elect between 'START' and 'STORY'
            if current_room == "STRT":
                button("START", 80, 235, 220, 100)
                button("STORY", 325, 235, 120, 100)

            # Elect between three doors (each has an own story)
            elif current_room == "DOOR":
                button("DOOR 1", 253, 129, DOOR_WIDTH, DOOR_HEIGHT)
                button("DOOR 2", 418, 129, DOOR_WIDTH, DOOR_HEIGHT)
                button("DOOR 3", 582, 129, DOOR_WIDTH, DOOR_HEIGHT)

            # Bathroom task buttons
            elif current_room == "BATH":
                button("CRACK", 10, 10, 1000, 1000)

            # Bathroom task solved
            elif current_room == "BATHEND":
                button("DOOR", 447, 177, 100, 150)

            # In the backroom you can click on multiple interactive objects
            elif current_room == "BACK":   
                button("VASE", 809, 120, 90, 80) 
                button("KLAPPE", 338, 425, 300, 100)
                button("TUCH", 58, 168, 100, 220)
                button("DISPLAY", 450, 130, 100, 30)

            # Backroom task solved
            elif current_room == "BACKEND":
                button("DISPLAYDOOR", 313, 44, (124 * 3), (84 * 3))
            
            # On the touchpad you can click on "CHECK" "ABORT" or the number-field
            elif current_room == "TCHP":
                button('CHECK', 350, 500, 150, 100)
                button('ABORT', 550, 500, 150, 100)
                button('NUMBERS', 365, 50, 300, 400)

            # In the safe room you can click on the "TOUCHPAD" or the "TRESOR" (if you typed in the right code)
            elif current_room == "TRES":
                button("TOUCHPAD", 600, 300, 80, 80)
                if check_for_code():
                    button("TRESOR", 300, 185, 260, 260)

            # In the rooms "CALL", "STRY" as well as "BOOK" you can only click on "EXIT"
            elif current_room == "CALL" or current_room == "STRY" or current_room == "BOOK" or current_room == "TRAS":
                button("EXIT", 680, 470, 220, 100)

            # In the childsroom you can click on the book and the tafel (and if solved on the door)
            elif current_room == "CHLD":
                button("TRASH", 600, 330, 50, 70)
                button("BOOK", 590, 250, 60, 40)
                button("TAFEL", 385, 100, 200, 85)

                if get_chld_solved():
                    button("DOOR", 440, 270, 100, 100)
            
            # In the garden you can click on the birdhouse and the door
            elif current_room == "GARD":
                button("BIRD", 700, 190, 100, 100)
                button("DOOR", 40, 360, 150, 80)
            
            # In the birdhouse you can click on the nest, key or exit button
            elif current_room == "BIRD":
                button("KEY", 380, 360, 100, 100)
                button("NEST", 320, 260, 370, 200) 
                button("EXIT", 680, 470, 220, 100)

            # In the final room you can click a link, the scipy button or the name field
            elif current_room == "FNAL":
                button("SCIPY", 680, 470, 220, 100)
                button("NAME", 400, 400, 200, 30)
                button("URL", 300, 270, 375, 20)

    pygame.display.update()
    clock.tick(60)