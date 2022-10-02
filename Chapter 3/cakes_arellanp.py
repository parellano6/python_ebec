"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 03.1 - Cakes
Date: 09/22/2022

Description:
    This program asks the user to enter a number of layers,
    and then uses nested loops to draw the ASCII art cake pattern

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
    layers = int(input("Enter the number of layers: "))  # num layers input
    for i in range(layers * 2):     # get layers
        if i % 2 == 0:      # checks to make sure divisible by 2
            print(' ' * int((((layers * 2) - 2 - i) / 2)), end='')
        for j in range((i + 1)):
            if j == 0 and i % 2 == 0: # checks to make sure divisible by 2
                print('[', end='')
            if i % 2 == 0: # checks to make sure divisible by 2
                print('*', end='')
        if i % 2 == 0: # checks to make sure divisible by 2
            print(']')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
