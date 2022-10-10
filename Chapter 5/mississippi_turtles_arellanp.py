"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 05.4 - Mississippi Turtles
Date: 10/09/2022

Description:
    Completes each of the letter functions so that they
    will draw that letter on the screen

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
count = 0

def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    color("purple")
    #speed(speed=0)

def draw_e():       # draws e
    """Write this function."""
    penup()
    setheading(0)
    forward(70)
    setheading(90)
    forward(10)
    pendown()
    setheading(40)
    circle(30, -300)
    setheading(180)
    forward(58)
    penup()
    setheading(270)
    forward(35)
    setheading(0)
    forward(60)


def draw_i():       # draws i
    """Write this function."""
    penup()
    setheading(0)
    forward(20)
    setheading(90)
    pendown()
    forward(50)
    penup()
    forward(20)
    setheading(0)
    pendown()
    circle(2, 360)
    penup()
    setheading(270)
    forward(70)
    
def draw_l():       # draws l
    """Write this function."""
    penup()
    setheading(0)
    forward(20)
    pendown()
    setheading(90)
    forward(120)
    setheading(270)
    forward(120)

def draw_M():       # draws M
    """Write this function."""
    penup()
    goto(-290, 40)
    pendown()
    goto(-290, 120)
    setheading(-90)
    circle(15, -180)
    setheading(-90)
    circle(15, -180)
    penup()
    goto(-260, 120)
    pendown()
    goto(-260, 40)
    penup()
    goto(-230, 120)
    pendown()
    goto(-230, 40)


def draw_p():       # draws p
    """Write this function."""
    penup()
    setheading(0)
    forward(22)
    setheading(270)
    forward(60)
    pendown()
    setheading(90)
    forward(110)
    setheading(270)
    forward(30)
    circle(30, 360)
    penup()
    setheading(270)
    forward(20)
    setheading(0)
    forward(60)

def draw_r():       # draws r
    """Write this function."""
    penup()
    setheading(0)
    forward(20)
    pendown()
    setheading(90)
    forward(60)
    setheading(270)
    forward(30)
    circle(30, -90)
    penup()
    setheading(270)
    forward(60)

def draw_s():       # draws s
    """Write this function."""
    penup()
    setheading(0)
    forward(20)
    pendown()
    forward(20)
    circle(10, 180)
    setheading(180)
    forward(15)
    circle(-10, 180)
    forward(20)
    penup()
    setheading(270)
    forward(40)
    

def draw_t():       # draws t
    """Write this function."""
    global count
    penup()
    if count == 0:
        setheading(180)
        forward(400)
        setheading(270)
        forward(200)
        count = 1
    else:
        setheading(0)
        forward(60)
        count = 1
    pendown()
    setheading(90)
    forward(120)
    setheading(270)
    forward(40)
    setheading(180)
    forward(40)
    setheading(0)
    forward(80)
    penup()
    setheading(270)
    forward(80)

def draw_u():
    """Write this function."""
    penup()
    setheading(0)
    forward(20)
    setheading(90)
    forward(60)
    pendown()
    setheading(270)
    forward(30)
    circle(30, 180)
    setheading(90)
    forward(30)
    setheading(270)
    forward(60)


def main():
    """After these lines, call your letter drawing functions
    as needed to draw the words "Mississippi turtles".
    """
    draw_M()
    draw_i()
    draw_s()
    draw_s()
    draw_i()
    draw_s()
    draw_s()
    draw_i()
    draw_p()
    draw_p()
    draw_i()
    
    draw_t()
    draw_u()
    draw_r()
    draw_t()
    draw_l()
    draw_e()
    draw_s()


"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
