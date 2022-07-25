import pygame, sys, time, webbrowser
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

# Musik einfügen
# https://www.python-lernen.de/pygame-spiele-sound-hintergrundmusik.htm
# pygame.mixer.music.load('sound/eine-MP3-Datei.mp3')
# pygame.mixer.music.play(-1,0.0)
# pygame.mixer.music.set_volume(.6)

def button(msg, x, y, w, h, ic, ac):
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
    if x+w > mouse[0] > x and y+h > mouse[1] > y:

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
            webbrowser.open('https://hisinone.dienste.uni-osnabrueck.de/qisserver/pages/cs/sys/portal/hisinoneStartPage.faces')

        # if want to see scipy-results save the data and open it
        elif "SCIPY" in msg:
            save_user_data()
            open_scipy_plot()
            
            stop_timer() 

        # go back to startscreen (STRY has only one button)
        elif current_room == "STRY":
            open_startscreen()

        # if book was closen open the room again
        elif current_room == "BOOK":
            open_door_2()

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
                if "1" in msg:
                    open_bathroom()
                elif "2" in msg:
                    open_door_2()
                else:
                    open_door_3()
               
            elif current_room == "BATHEND":
                open_backroom()
            
            elif current_room == "CHLD":
                open_garden()

            elif current_room == "GARD":

                from door2 import klappe_open, got_key

                if not klappe_open and got_key:
                    open_klappe_garden()
                    
                elif klappe_open:
                    open_endroom()
                    
            elif "DISPLAYDOOR" in msg:
                open_endroom()

        # if cracked 'something' in the bath, it will be displayed
        elif "CRACK" in msg:
            crack_wall(mouse[0], mouse[1])
       
        # if clicked on the vase it cracks
        elif "VASE" in msg:
            crack_vase()

        # if clicked on klappe it will open (if you found the key already)
        elif "KLAPPE" in msg:
            open_klappe()
        
        # if you clicked on tuch it will be pushed
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
                open_endroom(open_tresor=True)

        # if clicked on the numberfield save your input
        elif "NUMBERS" in msg and current_room == "TCHP":
            save_num(mouse)
        
        # if clicked on book display it
        elif "BOOK" in msg:
            open_book()

        # if clicked on exit in the birdshouse open the garden
        elif "EXIT" in msg and current_room == "BIRD":
            open_garden()

        # if clicked on tafel
        elif "TAFEL" in msg:
            rotate_number((mouse[0]/15))
 
        # if clicked on open the birdshouse
        elif "BIRD" in msg:
            open_birdshouse()

        # if clicked on the key collect it
        elif "KEY" in msg:
            get_key()

        # if clicked on nest collect it
        elif "NEST" in msg:
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

#open_door_2()
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
            
            # on startscreen you can elect between 'START' and 'STORY'
            if current_room == "STRT":
                button("START", 80, 235, 220, 100,0,0)
                button("STORY", 325, 235, 120, 100,0,0)

            # elect between three doors (each has an own story)
            elif current_room == "DOOR":
                button("DOOR 1", 253, 129, door_width, door_height,0,0)
                button("DOOR 2", 418, 129, door_width, door_height,0,0)
                button("DOOR 3", 582,129, door_width, door_height,0,0)

            # bathroom task buttons
            elif current_room == "BATH":
                button("CRACK", 10,10, 1000, 1000,0,0)

            # bathroom task solved
            elif current_room == "BATHEND":
                button("DOOR OPEN", 447,177, 100, 150,0,0)

            # in the backroom you can click on multiple interactive objects
            elif current_room == "BACK":   
                button("VASE", 809, 120, 90, 80, 0, 0) 
                button("KLAPPE", 338, 425, 300, 100,0,0)
                button("TUCH", 58,168,100,220,0,0)
                button("DISPLAY", 450, 130, 100, 30, 0,0)

            # backroom task solved
            elif current_room == "BACKEND":
                button("DISPLAYDOOR", 313, 44, (124*3), (84*3), 0,0)
            
            # on the touchpad you can click on "CHECK" "ABORT" or the number-field
            elif current_room == "TCHP":
                time.sleep(0.3)
                button('CHECK', 350, 500, 150, 100, 0, 0)
                button('ABORT', 550, 500, 150, 100, 0, 0)
                button('NUMBERS', 365, 50, 300, 400, 0, 0)

            # in the tresor room you can click on the "TOUCHPAD" or the "TRESOR" (if you typed in the right code)
            elif current_room == "TRES":
                button("TOUCHPAD", 600, 300, 80, 80, 0, 0)
                if check_for_code():
                    button("TRESOR", 300, 185, 260, 260, 0, 0)

            # in the rooms "CALL", "STRY" as well as "BOOK" you can only click on "EXIT"
            elif current_room == "CALL" or current_room == "STRY" or current_room == "BOOK":
                button("EXIT", 680, 470, 220, 100, 0, 0)

            # in the childsroom you can click on the book and the tafel (and if solved on the door)
            elif current_room == "CHLD":
                button("BOOK", 590, 250, 60, 40, 0, 0)
                button("TAFEL", 385, 100, 200, 85, 0, 0)

                if get_solved_door2():
                    button("DOOR",440, 270, 100, 100, 0,0 )
            
            # in the garden you can click on the birdshouse and the door
            elif current_room == "GARD":
                button("BIRD", 700, 190, 100, 100, 0, 0)
                button("DOOR", 40, 360, 150, 80, 0, 0)
            
            # in the birdshouse you can click on the nest, key or exit button
            elif current_room == "BIRD":
                button("NEST", 320, 260, 370, 200, 0, 0)
                button("KEY", 380, 360, 100, 100, 0, 0)
                button("EXIT", 680, 470, 220, 100, 0, 0)

            # in the final room you can click a link, the scipy button or the name field
            elif current_room == "FNAL":
                button("URL", 300, 270, 400, 20,0,0)
                button("SCIPY", 680, 470, 220, 100, 0, 0)
                button("NAME", 400, 400, 200, 30, 0, 0)

            # only for testing purposes
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)

    pygame.display.update()
    clock.tick(60)