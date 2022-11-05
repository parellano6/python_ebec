"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 11/05/2022

Description:
    This program asks the user for a string input and returns it
    converted to Pig Latin.

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

def pig(message):
    message = message.split()               # splits user input
    
    for index, value in enumerate(message):
        message[index] = value[1:].lower() + value[0].lower() + 'ay'    # adds 'ay'
        if index == 0:
            message[index] = (message[index]).capitalize()  # capitalizes first letter
        
    return ' '.join(message)


def main():
    message = input("Enter a string: ")     # user input
    message = pig(message)
        
    print("Pig latin: ", end="")    # prints
    print(message)


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
