import pygame, sys, time
from threading import Thread
from door1 import *
from door2 import *
from door3 import *
from display_components import *
from endroom import *
from startscreen import *
from scipy_analysis import *
from game_timer import *

# initialze pygame first
pygame.init()

# First of all we want some nice backgroundmusic, therefore we load some mp3, 
# we want that the music repeats the whole time, so we set -1 and we set our volume to 0.1
pygame.mixer.music.load('Sounds/columbianische machenschaften.mp3')
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(.1)


def button(msg, x, y, w, h):
    """This universal function simulates a button so if the click is in the given coordinates and width/height 
        of the 'button' the respective function will be called.
        Args:
            msg short description of the button-field to check (helps to decide how to handle)
            x the x-coordinate of the upper right corner of the button field
            y the y-coordinate of the upper right corner of the button field
            w the width of the button 
            h the height of the button
    """ 
    global current_room

    # get postion of mouse to decide wheter the button was clicked
    mouse = pygame.mouse.get_pos()

    # if clicked on a valid button...
    if x + w > mouse[0] > x and y + h > mouse[1] > y:

        current_room = get_current_room()
        print("CURRENT ROOM IS " + current_room + " \n---------------------------------" +msg + " IS CLICKED ON----------------------------------------")

        # in the room "CALL" there is only one button, so no need to check for msg
        if current_room == "CALL":
            open_endscreen(True)
            pygame.display.update()
            time.sleep(0.3)
            open_final_words()

        # if clicked on name field the user can enter his or her name
        if "NAME" in msg:
           user_name_input()
                
        # if clicked on the url open it
        elif "URL" in msg:
            print("OPEN WEBBROWSER")
            open_tab()     

        # if you want to see scipy-results save the data and open it
        elif "SCIPY" in msg:
            save_user_data()
            open_scipy_plot()
            stop_timer() 

        # go back to startscreen (STRY has only one button)
        elif current_room == "STRY":
            push_exit()
            open_startscreen()

        # if book was closen open the room again
        elif current_room == "BOOK":
            push_exit()
            open_childsroom()

        # if clicked on start, load the first room
        elif "START" in msg:
            open_3doors()

        # if clicked on story load the storyscreen
        elif 'STORY' in msg and current_room == 'STRT':
            open_story()

        # if clicked on a door open the respective room
        elif "DOOR" in msg:
            
            if current_room == 'DOOR':
                #display_loading_screen()       
                pygame.mixer.Sound.set_volume(opens, 0.1)
                pygame.mixer.Sound.play(opens)
                if "1" in msg:
                    open_bathroom()
                elif "2" in msg:
                    open_childsroom()
                else:
                    open_door_3()
               
            elif current_room == "BATHEND": 
                open_backroom()
            
            elif current_room == "CHLD":
                open_garden()

            elif current_room == "GARD":

                if not get_klappe_open() and get_got_key():
                    pygame.mixer.Sound.play(opens)
                    open_klappe_garden()
                    
                elif get_klappe_open():
                    open_endroom()
                    
            elif "DISPLAYDOOR" in msg:
                open_endroom()

        # if cracked 'something' in the bath, it will be displayed
        elif "CRACK" in msg:
            crack_wall(mouse[0], mouse[1])
       
        # if clicked on the vase it cracks
        elif "VASE" in msg:
            crack_vase()

        # if clicked on trapdoor it will open (if you found the key already)
        elif "KLAPPE" in msg:
            open_klappe()
        
        # if you clicked on cloth it will be pushed
        elif "TUCH" in msg:
            push_tuch()

        # if click on the tresor (after putting in the right code) open the endscreen
        elif "TRESOR" in msg:
            open_endscreen()

        # if clicked on the touchpad zoom in
        elif "TOUCHPAD" in msg:
            zoom_touchpad()
            
        # if click on abort go back and delete your input
        elif "ABORT" in msg:
            open_endroom(reset_code=True)

        # if clicked on check, check if input was correct
        elif "CHECK" in msg and current_room == "TCHP":
            if check_for_code():
                open_tresor()

        # if clicked on the numberfield save your input
        elif "NUMBERS" in msg and current_room == "TCHP":
            save_num(mouse)
        
        # if clicked on book display it
        elif "BOOK" in msg:
            pygame.mixer.Sound.set_volume(page, 0.1)
            pygame.mixer.Sound.play(page)
            open_book()

        # if clicked on exit in the birdshouse open the garden
        elif "EXIT" in msg and current_room == "BIRD":
            push_exit()
            open_garden()

        # if clicked on blackboard
        elif "TAFEL" in msg:
            rotate_number((mouse[0] / 15))

        # if clicked on the garbage can
        elif "TRASH" in msg:
            open_flyer()

        elif current_room == "TRAS":
            push_exit()
            open_childsroom()
 
        # if clicked on open the birdshouse
        elif "BIRD" in msg:
            pygame.mixer.Sound.set_volume(bird, 0.1)
            pygame.mixer.Sound.play(bird)
            open_birdshouse()

        # if clicked on the key collect it
        elif "KEY" in msg:
            get_key()

        # if clicked on nest collect it
        elif "NEST" in msg:
            pygame.mixer.Sound.set_volume(nest, 0.1)
            pygame.mixer.Sound.play(nest)
            get_nest()  
            
        # if you clicked on the display you can type something in
        elif "DISPLAY" in msg and current_room == "BACK":
            if not input_correct(True) and check_input():
                display_solved()
                reset_text()
           
Screen = 0  
# set up the game (here you can decide in which room you want to start) default shouold be open_startscreen()
open_startscreen()
#open_3doors()
#open_bathroom()
#open_backroom()

#open_childsroom()
#open_garden()

#open_door_3()

#open_endroom()
#open_endscreen()
#open_final_words()

frame_count = 0
frame_rate = 60

# this thread is needed because else the timer (e.g. if put in main-loop) does not perform in real time
t1 = Thread(target = timer)
# set to daemon so when the user clicks on exit the timer-thread is closed as well
t1.daemon = True
# start the thread
t1.start()

##################################################  MAIN  #####################################################################################################################
while True:
    # each interactive event is saved here
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        mouse_click = pygame.mouse.get_pressed()

        # if there was a left-click, check if a valid button was pressed in dependence of the current room
        if mouse_click[0] == 1:    
            click()
            current_room = get_current_room()
            
            # at the startscreen you can elect between 'START' and 'STORY'
            if current_room == "STRT":
                button("START", 80, 235, 220, 100)
                button("STORY", 325, 235, 120, 100)

            # elect between three doors (each has an own story)
            elif current_room == "DOOR":
                button("DOOR 1", 253, 129, door_width, door_height)
                button("DOOR 2", 418, 129, door_width, door_height)
                button("DOOR 3", 582, 129, door_width, door_height)

            # bathroom task buttons
            elif current_room == "BATH":
                button("CRACK", 10, 10, 1000, 1000)

            # bathroom task solved
            elif current_room == "BATHEND":
                pygame.mixer.Sound.play(footsteps)
                button("DOOR", 447, 177, 100, 150)

            # in the backroom you can click on multiple interactive objects
            elif current_room == "BACK":   
                button("VASE", 809, 120, 90, 80) 
                button("KLAPPE", 338, 425, 300, 100)
                button("TUCH", 58, 168, 100, 220)
                button("DISPLAY", 450, 130, 100, 30)

            # backroom task solved
            elif current_room == "BACKEND":
                button("DISPLAYDOOR", 313, 44, (124 * 3), (84 * 3))
            
            # on the touchpad you can click on "CHECK" "ABORT" or the number-field
            elif current_room == "TCHP":
                time.sleep(0.3)
                button('CHECK', 350, 500, 150, 100)
                button('ABORT', 550, 500, 150, 100)
                button('NUMBERS', 365, 50, 300, 400)

            # in the tresor room you can click on the "TOUCHPAD" or the "TRESOR" (if you typed in the right code)
            elif current_room == "TRES":
                button("TOUCHPAD", 600, 300, 80, 80)
                if check_for_code():
                    button("TRESOR", 300, 185, 260, 260)

            # in the rooms "CALL", "STRY" as well as "BOOK" you can only click on "EXIT"
            elif current_room == "CALL" or current_room == "STRY" or current_room == "BOOK" or current_room == "TRAS":
                button("EXIT", 680, 470, 220, 100)

            # in the childsroom you can click on the book and the tafel (and if solved on the door)
            elif current_room == "CHLD":
                button("TRASH", 600, 330, 50, 70)
                button("BOOK", 590, 250, 60, 40)
                button("TAFEL", 385, 100, 200, 85)

                if get_solved_door2():
                    button("DOOR", 440, 270, 100, 100)
            
            # in the garden you can click on the birdshouse and the door
            elif current_room == "GARD":
                button("BIRD", 700, 190, 100, 100)
                button("DOOR", 40, 360, 150, 80)
            
            # in the birdshouse you can click on the nest, key or exit button
            elif current_room == "BIRD":
                button("KEY", 380, 360, 100, 100)
                button("NEST", 320, 260, 370, 200) 
                button("EXIT", 680, 470, 220, 100)

            # in the final room you can click a link, the scipy button or the name field
            elif current_room == "FNAL":
                button("SCIPY", 680, 470, 220, 100)
                button("NAME", 400, 400, 200, 30)
                button("URL", 300, 270, 375, 20)
                
            # only for testing purposes
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)

    pygame.display.update()
    clock.tick(60)