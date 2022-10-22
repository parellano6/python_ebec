"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 06.4 - Log Spiral
Date: 10/22/2022

Description:
    Draws a log spiral using turtle commands.

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
import math


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    a = 4           # starting a value
    b = 0.22        # starting b value
    
    penup()
    goto(a, 0)      # starting location
    pendown()
    
    for i in range(0, 1081, 1):
        deg = math.radians(i)       # degree val
        x = a * math.exp(b * deg) * math.cos(deg)   # x coordinate
        y = a * math.exp(b * deg) * math.sin(deg)   # y coordinate
        goto(x, y)
        


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
