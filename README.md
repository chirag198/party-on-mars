# Mars Rover Problem Solution:
# Party-on-mars


# How To Run:
Step-1: Open the Terminal.<br/>
Step-2: Navigate to the directory: /party-on-mars/<br/>
Step-3: Enter following command on your terminal: python3 main.py.<br/>
Step-4: Follow the instructions and party on mars!  ;)<br/>

#

MARS ROVER

We have succesfully managed to land a rover on mars.

Now we have to enter the size of the platue first in our system so that it won't run out of our reach and won't topple. ⚡

A rover's position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, we need string of letters. The possible letters are 'F', 'B' and 'L' and 'R'.

F -> Move forward on current heading
B -> Move backwards on current heading
L -> Rotate left by 90 degrees
R -> Rotate right by 90 degrees 


# Input:

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0 0.
Make sure you just enter the co-ordinates(integer) with just a space as delimiter.

The rest of the input is information pertaining to the rovers that have been deployed. Rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.

Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.

# Output:

The output for each rover should be its final co-ordinates and heading.

Test Input:
Please enter the size of mars (2 numbers, separated by a space and higher than 0.):
10 10

Please enter the current rover's initial position(Two Integers and one Direction SAPARATED BY SPACE).
(eg. 3 4 S)Remember to keep inside Mars limits!:
6 4 N
Rover initiated on 6 4 facing N

Please enter the operations you wish for this rover to execute.:
FLFFFRFLB

Expected Output:<br/>
--------------- Output ---------------<br/>
ROVER is on position: 4 6 facing W <br/>
--------------------------------------<br/>


Test Input-2:

Test Input:
Please enter the size of mars (2 numbers, separated by a space and higher than 0.):
10 10

Please enter the current rover's initial position(Two Integers and one Direction SAPARATED BY SPACE).
(eg. 3 4 S)Remember to keep inside Mars limits!:
6 4 N
Rover initiated on 4 2 facing E

Please enter the operations you wish for this rover to execute.:
FLFFFRFLB

Expected Output:<br/>
--------------- Output ---------------<br/>
ROVER is on position: 6 4 facing N<br/>
--------------------------------------<br/>

