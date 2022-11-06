"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 08.4 - Number Writer
Date: 11/05/2022

Description:
    This program asks the user how many random numbers it should generate.
    and then outputs that many random numbers to random_numbers.txt

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
import random

"""Write new functions below this line (starting with unit 4)."""


def main():
    message = input("How many numbers would you like? ")    # number of values asked
    with open('random_numbers.txt', 'w') as file:           # opens file
        for i in range(int(message)):                       # range of num
            randNum = random.randint(1019, 1215)            # random value
            file.write(format(randNum) + '\n')              # adds to file
    
    file.close()    # close file



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
