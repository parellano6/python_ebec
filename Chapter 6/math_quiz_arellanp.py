"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/10/2022

Description:
    This program gives the user a simple math quiz. The program
    displays a random two digit number and a random three digit 
    number that are to be added.

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
import random as rm

"""Write new functions below this line (starting with unit 4)."""
def random_number(digits):
    start = 10 ** (digits - 1)      # starting val
    end = (10 ** digits) - 1        # ending val
    return rm.randint(start, end)   # random integer

def main():
    rand_2 = random_number(2)       # 2 digit rand
    rand_3 = random_number(3)       # 3 digit rand
    print("   " + str(rand_2))
    print("+ " + str(rand_3))
    print("-----")
    in_val = int(input("= "))       # user input
    tot = rand_2 + rand_3           # tot val
    if tot != in_val:               # incorrect
        print("Incorrect. The correct answer is " + str(tot) + ".")
    else:                           # correct
        print("Correct -- Good Work!")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
