# Escaperoom Adventure - Where is my Emma? 

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Game structure
 * How to play the game
 * The starting screen
 * The big descision
 * Rooms in door 1
 * Rooms in door 2
 * Rooms in door 3
 * The story
 * Solutions

INTRODUCTION
---------------------
This project was created as part of the 'Basic Programming in Python' course at the University Osnabrück.
It is based on the concept of an escape room, where you can examine the individual scenes by clicking on the screen. Each scene consists of 1-2 puzzles, only when solve the respective puzzles you can switch to the next scene.
If you manage to solve all the puzzles, you win the game!

REQUIREMENTS
---------------------
Please install pygame.
```bash
pip install pygame
```
or 
```bash
conda install pygame
```
 Please install numpy. 
```bash
pip install numpy
```
or 
```bash
conda install numpy
```
Please install mathplotlib

```bash
pip install mathplotlib
```
or 
```bash
conda install mathplotlib
```

Please install pandas

```bash
pip install pandas
```
or 
```bash
conda install pandas
```
To start the game excecute the 'main.py' file
```bash
python main.py
```

GAME STRUCTURE
---------------------
| Door 1 | Door 2 | Door 3 |
|:--------------|:-------------|:--------------|
| Bathroom | Childsroom | Surprise |
| Backroom | Garden |  |
| Saferoom | Saferoom |  |
| End | End |  |

HOW TO PLAY THE GAME
---------------------
In order to solve our puzzles you need to click on something on the screen. Sometimes you find a key, sometimes you find or reveal a part of the puzzle that is needed to solve it.
We hide some hints for you to keep your eyes open, anything can be useful, maybe it helps if you use pen and paper.
If you have the correct code to solve the puzzle you have to either use your keyboard or you have to click on numbers at your screen.

THE STARTING SCREEN
---------------------
Here you can choose between starting the game or reading the story.
![Starting screen](https://github.com/jjennyy/BaPy_escaperoom/blob/main/Images/start_pushstart.PNG)

THE BIG DESCISION
---------------------
If you clicked on start, you will end up in this room where you have to decide between 3 doors.
Depending on your choice you will visit different rooms and puzzles.
![Big descision](https://github.com/jjennyy/BaPy_escaperoom/blob/main/Images/3doors.jpg)

ROOMS IN DOOR 1
---------------------
The first room will be the bathroom, here you have to solve a small puzzle by cracking the wall.
![Bathroom](https://github.com/jjennyy/BaPy_escaperoom/blob/main/Images/bathroom.PNG)
The second room will be the backroom, here you have to find and count all the red balls to solve the puzzle.
Watch out for hints, they can be very helpful!
![Backroom](https://github.com/jjennyy/BaPy_escaperoom/blob/main/Images/backroom.PNG)
The last room consists of a safe. The code can be found in room 2.
![Safe](https://github.com/jjennyy/BaPy_escaperoom/blob/main/Images/tresor_open.png)


ROOMS IN DOOR 2
---------------------
The first room willbe the childsroom, here you have to solve a puzzle that is a little bit harder, it consists of a logic puzzle which solution needs to be translated into forms in order to solve the puzzle and enter the next room.
![Childsroom](https://github.com/jjennyy/BaPy_escaperoom/blob/main/Images/childsroom.PNG)
The next room is the garden, here you can find a key that is needed if you want to enter the last room.
Please keep in mind that the code for the last room is hidden in this room, and that you can not come back.
![Garden](https://github.com/jjennyy/BaPy_escaperoom/blob/main/Images/garden_closed.PNG)
The last room consists of a safe. The code can be found in room 2.
![Safe](https://github.com/jjennyy/BaPy_escaperoom/blob/main/Images/tresor_open.png)


ROOMS IN DOOR 3
---------------------
![Surprise](https://github.com/jjennyy/BaPy_escaperoom/blob/main/Images/mysteryroom.PNG)

THE STORY 
---------------------

SOLUTIONS
---------------------
Bathroom.
```bash
Try to crack the wall in the middle of the screen by clicking on it.
```
Backroom: Key.
```bash
You can find the key in the vase on the right-hand side.
```
Backroom: Blackboard.
```bash
The correct number of red balls is 15. Please use your keyboard to enter this number.
```
Safe code.
```bash
You can finde the code for the safe in the backroom. It is 1407. This time you have to click on the right numbers on the touchpad.
```
Childsroom.
```bash
The first part of the puzzle can be found on the table. The solution is 420. 
This number has to be translated into the correct sequence of forms (can be found on the poster over the bed). The sequence is "Heard","Square","Circle".
```
Garden.
```bash
The key can be found in the birdhouse.
```
Safe code.
```bash
You can finde the code for the safe at the fence in the garden. It is 1532.
