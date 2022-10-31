"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 10/29/2022

Description:
    This program returns the probability that the sum of
    two dice will equal a certain number. This is determined by
    rolling simulating two dice rolling a million times.

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

def roll_d6():
    return random.randint(1, 6)

def get_2d6_rolls(numRolls):
    outList = []
    for i in range(numRolls):
        num1 = roll_d6()        # first val
        num2 = roll_d6()        # second val
        tot = num1 + num2       # add vals
        outList.append(tot)     # appends vals
    
    return outList


def main():
    numTimes = 1000000      # num times to run
    
    print("Roll  Frequency")
    listVals = get_2d6_rolls(numTimes)      # gets rand list vals
    for i in range(2, 13):
        numIn = listVals.count(i) / numTimes * 100      # gets percentage
        print('{:3.0f}'.format(i) + "   " + '{:6.2f}'.format(numIn) + "%")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
