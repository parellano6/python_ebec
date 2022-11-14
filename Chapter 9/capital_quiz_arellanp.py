"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 11/13/2022

Description:
    This program loads state cpaital information from state_capitals.txt
    and puts it into a dictionary to then quiz the user.

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
import string

"""Write new functions below this line (starting with unit 4)."""
def get_state_data():
    state_dict = {}     # state & capitals dictionary
    newList = []        # line values
    with open('state_capitals.txt', 'r') as file:           # opens file
        for line in file:
            newList = line.split(',')                       # gets rid of spaces
            state_dict[newList[1].strip()] = newList[0]     # adds to dictionary
    return(state_dict)
    

def main():
    state_cap = get_state_data()        # dictionary of capitals
    leftover_cap = {}                   # for continuous iteration
    go = True                           # going through loop
    numRight = 0                        # number of right
    numTot = -1                         # number of wrong
    
    while go == True:
        numTot += 1                     # increment 
        if len(state_cap) == 0:
            keys = list(leftover_cap.keys())
            vals = list(leftover_cap.values())
            if len(keys) == 0:
                break;
            key = keys[0]
            val = vals[0]
        else:
            key, val = random.choice(list(state_cap.items()))
        
        inVal = input("What is the capital of " + key + " (enter 0 to quit)? ")
        if (string.capwords(inVal) == val):
            numRight += 1
            print("  That is correct!")
            if len(state_cap) == 0:
                del leftover_cap[key]
            else:
                del state_cap[key]
        elif inVal == '0':
            go = False
        else:
            print("  That is incorrect.")
            print("  The capital of " + key + " is " + val + ".")
            if len(state_cap) == 0:
                del leftover_cap[key]
                leftover_cap[key] = val
            else:
                leftover_cap[key] = val
                del state_cap[key]
            


    print("You answered " + str(numRight) + " out of " + str(numTot) + " questions correctly.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
