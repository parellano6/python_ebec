"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 10/29/2022

Description:
    This program asks the user 10 numbers. Then returns
    the highest, lowest, total, and average of the numbers.

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
from statistics import mean

"""Write new functions below this line (starting with unit 4)."""

def get_number_list():
    outList = []        # default list
    for i in range(1, 11):
        outList.append(float(input("  number " + '{:2.0f}'.format(i) + " of 10: ")))
        
    return outList      # returns list

def main():
    print("Enter 10 numbers:")
    listVal = get_number_list()     # gets list from user input
    maxVal = max(listVal)           # max val
    minVal = min(listVal)           # min val
    tot = sum(listVal)              # sum of list vals
    avg = mean(listVal)             # avg of list vals
    
    print("Highest number: " + '{:.2f}'.format(maxVal))
    print("Lowest number: " + '{:.2f}'.format(minVal))
    print("Total: " + '{:.2f}'.format(tot))
    print("Average: " + '{:.2f}'.format(avg))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
