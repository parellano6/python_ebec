"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/22/2022

Description:
    Imports turtle graphics from vowels file, then draws vowels in a random order.
    
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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
import vowels
import random


"""Write new functions below this line (starting with unit 4)."""

def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    vals = (random.sample(range(0, 5), 5)) # gets random array vals
    
    for i in vals:          # draw for loop
        if i == 0:          # draw a
            vowels.draw_a()
        elif i == 1:        # draw e
            vowels.draw_e()
        elif i == 2:        # draw i
            vowels.draw_i()
        elif i == 3:        # draw o
            vowels.draw_o()
        else:               # draw u
            vowels.draw_u()


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
