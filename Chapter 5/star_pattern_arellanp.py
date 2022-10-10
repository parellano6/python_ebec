"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 10/08/2022

Description:
   Draws a star pattern that has a user specified number of points. 

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    points = int(input("How many points do you want on the star? "))    # user input
    
    color('black', 'pink')      # color for line and fill
    begin_fill()                # begins filling
    angleA = 360 / points       # angle A
    angleB = 2 * angleA         # angle B
    
    right((180 - angleB ) / 2)  # initial angle
    for i in range(points * 2): # looping for whole thing
        forward(60)             # moves
        if i % 2 == 1:          # angle B
            right(180 - angleB)
        else:                   # angle A
            left(180 - angleA)
    end_fill()                  # ends filling

"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
