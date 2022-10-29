"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 10/29/2022

Description:
    This program asks the user for an integer and a list of integers.
    Then it returns a new list with only the multiples of the first integer
    input from the list input.

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

def multiples_of(numVal, listVal):      # finds if has multiple in list
    outList = []
    for i in listVal:
        if i % numVal == 0:
            outList.append(i)
    return outList


def main():
    multi = 13      # checks value
    listIn = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406]  # list to check
    outVal = multiples_of(multi, listIn)    # output list val
    print("Original list of numbers:")
    print("  " + format(listIn))
    print("Numbers in the list that are multiples of " + format(multi) + ":")
    print("  " + format(outVal))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
