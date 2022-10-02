"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 09/19/2022

Description:
    This program asks the user to choose a pocket number, and then displays
    the color of that pocket (either green, red, or black).

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


"""Write new functions below this line (starting with unit 4)."""


def main():
    pocket = int(input("Please choose a pocket number: "))   # pocket input variable
    color = ""      # color of pocket
    
    if pocket < 0 or pocket > 36:
        print("  Invalid Input!")
    elif pocket == 0:
        color = "green"
    elif pocket <= 10:
        if pocket % 2 == 0:
            color = "black"
        else:
            color = "red"
    elif pocket <= 18:
        if pocket % 2 == 0:
            color = "red"
        else:
            color = "black"
    elif pocket <= 28:
        if pocket % 2 == 0:
            color = "black"
        else:
            color = "red"
    elif pocket <= 36:
        if pocket % 2 == 0:
            color = "red"
        else:
            color = "black"
    
    if pocket >= 0 and pocket <= 36:
        print("  Pocket number " + str(pocket) + " is " + color + ".")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
