import pygame, sys, os
from door1 import *
from door2 import *
from door3 import *
from display_components import *
from handle_userinput import *
from endroom import *
from startscreen import *
import time 
import webbrowser

'''Display.flip will update the entire surface. Basically the entire screen. Display.update can just update specific areas of the screen'''

pygame.init()

rooms = [['STRT', 'DOOR', 'BATH', 'BATHEND', 'BACK', 'BACKEND', 'TRES', 'TCHP', 'CALL'],['STRT'],['STRT']]

Screen = 0 # zero is start, one is frist room, two is second room etc.

click_counter = 0

# this universal function simulates a button so if the click is in the given coordinates and width/height of the 'button' the 
# respective function will be executed (leitet quasi weiter)
def button(msg, x,y,w,h,ic,ac): 
    global current_room

    # get postion of mouse
    mouse = pygame.mouse.get_pos()

    # if clicked on a valid button...
    if x+w > mouse[0] > x and y+h > mouse[1] > y:

        print("CURRENT ROOM IS " + current_room + " \n---------------------------------" +msg + " IS CLICKED ON----------------------------------------")


        if current_room == "CALL":
            open_endscreen(True)
            pygame.display.update()
            time.sleep(0.3)
            #sys.exit()
            open_final_words()
            current_room = "FNAL"

        elif current_room == "FNAL":
            webbrowser.open('https://hisinone.dienste.uni-osnabrueck.de/qisserver/pages/cs/sys/portal/hisinoneStartPage.faces')

        elif current_room == 'STRY':
            current_room = 'STRT'
            open_startscreen()

        elif current_room == "BOOK":
            print('I OPEN DOOR TWOOOOO')
            open_door_2()
            current_room = "CHLD"

        # if you clicked on start, load the first room
        elif 'START' in msg and current_room == 'STRT':
            current_room = 'DOOR'
            open_3doors()

        # if you clicked on story load the storyscreen
        elif 'STORY' in msg and current_room == 'STRT':
            current_room = 'STRY'
            open_story()

        # if you clicked on a door open the respective room
        elif "DOOR" in msg:
            
            if current_room == 'DOOR':
                #display_loading_screen()
                if "1" in msg:
                    open_bathroom()
                    current_room = 'BATH'
                elif "2" in msg:
                    open_door_2()
                    current_room = "CHLD"
                else:
                    open_door_3()
                    open_3doors(False)
               
            elif current_room == "BATHEND":
                open_backroom()
                current_room = "BACK"
            
            elif current_room == "CHLD":
                open_garden()
                current_room = "GARD"

            elif current_room == "GARD":

                from door2 import klappe_open, got_key

                if not klappe_open and got_key:
                    open_klappe_garden()
                    
                elif klappe_open:
                    open_endroom()
                    current_room = "TRES"
                    
            elif "DISPLAYDOOR" in msg:
                open_endroom()
                current_room = "TRES"

        # if you cracked 'something' in the bath, it will be displayed
        elif "CRACK" in msg:
            if crack_wall(mouse[0], mouse[1]):
                current_room = 'BATHEND'

        # if you clicked on the vase it cracks
        elif "VASE" in msg:
            crack_vase()

        # if you clicked on klappe it will open (if you found the key already)
        elif "KLAPPE" in msg:
            open_klappe()
        
        # if you clicked on tuch it will be pushed
        elif "TUCH" in msg:
            push_tuch()

        # if you clicked on the touchpad zoom in
        elif "TOUCHPAD" in msg:
            zoom_touchpad()
            current_room = "TCHP"

        # if you click on the tresor (after putting in the right code) open the endscreen
        elif "TRESOR" in msg:
            open_endscreen()
            current_room = "CALL"
            
        # if you click on abort go back and delete your input
        elif "ABORT" in msg:
            open_endroom(reset_code=True)
            current_room = "TRES"

        # if you click on check, check if your input was correct
        elif "CHECK" in msg and current_room == "TCHP":
            if check_for_code():
                open_endroom(open_tresor=True)
                current_room = "TRES"

        # if you clicked on the numberfield save your input
        elif "NUMBERS" in msg and current_room == "TCHP":
            save_num(mouse)
        
        elif "BOOK" in msg:
            open_book()
            current_room = "BOOK"

        elif "EXIT" in msg and current_room == "BIRD":
            open_garden()
            current_room = "GARD"

        elif "TAFEL" in msg:
            # first  385 -> 450 -> 26-30
            # second  450 -> 520 -> 30-34)
            # third  520 + (35+)
            rotate_number((mouse[0]/15))

        elif "BIRD" in msg:
            open_birdshouse()
            current_room = "BIRD"

        elif "KEY" in msg:
            get_key()
            
        # if you clicked on the display you can type something in
        if "DISPLAY" in msg and current_room == "BACK":
            if not handle_input():
                
                current_room = "BACKEND"
                open_backroom()
                clock.tick(2)
                open_display()

        
        
# set up the game (startscreen)
if  Screen == 0: 
    open_startscreen()  

##################################################  MAIN  #####################################################################################################################
while True:

    # each interactive event is saved here
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        mouse_click = pygame.mouse.get_pressed()

        # if there was a left-click- check if a valid button was pressed in dependence of the current room
        if mouse_click[0] == 1:
            click_counter +=1
            print(current_room)
            mouse_pos = pygame.mouse.get_pos()
            
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
            
            # on the touchpad you can click on 'CHECK' 'ABORT' or the number-field
            elif current_room == "TCHP":
                time.sleep(0.3)
                button('CHECK', 350, 500, 150, 100, 0, 0)
                button('ABORT', 550, 500, 150, 100, 0, 0)
                button('NUMBERS', 365, 50, 300, 400, 0, 0)

            # in the tresor room you can click on the 'TOUCHPAD' or the 'TRESOR' (if you typed in the right code)
            elif current_room == "TRES":
                button("TOUCHPAD", 600, 300, 80, 80, 0, 0)
                if check_for_code():
                    button("TRESOR", 300, 185, 260, 260, 0, 0)

            elif current_room == "CALL":
                button("EXIT", 680, 470, 220, 100, 0, 0)

            elif current_room == "STRY":
                button("EXIT", 680, 470, 220, 100, 0, 0)

            elif current_room == "CHLD":

                button("BOOK", 590, 250, 60, 40, 0, 0)
                button("TAFEL", 385, 100, 200, 85, 0, 0)


                # interesting: this import statement is needed to synchronize the values of the global variable
                # 'solved_door2'
                from door2 import solved_door2
                if solved_door2:
                    button("DOOR",440, 270, 100, 100, 0,0 )
            

            elif current_room == "BOOK":
                button("EXIT", 680, 470, 220, 100, 0, 0)

            elif current_room == "GARD":
                button("BIRD", 700, 190, 100, 100, 0, 0)
                button("DOOR", 40, 360, 150, 80, 0, 0)
            
            elif current_room == "BIRD":
                print("CHECK BUTTOINS")
                button("KEY", 380, 360, 100, 100, 0, 0)
                button("EXIT", 680, 470, 220, 100, 0, 0)

            elif current_room == "FNAL":
                button("URL", 300, 270, 400, 20,0,0)

            # only for testing purposes
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()