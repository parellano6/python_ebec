"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 08.6 - Step Counter
Date: 11/06/2022

Description:
    This program uses the steps.txt for the number of steps a person
    has taken each day for a year. Then it displays the average number of steps
    each month

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
from calendar import monthrange, month_name

"""Write new functions below this line (starting with unit 4)."""


def main():
    numSteps = []                                           # steps list
    with open('steps.txt', 'r') as file:                    # opens file
        for line in file:
            numSteps.append(line.rstrip())                  # adds value to list
    numSteps = list(map(int, numSteps))                     # converts list to int vals
    
    monthAvg = []           # avg list values
    nextVal = 0
    for i in range(1, 13):
        numDays = monthrange(2019, i)[1]    # number of days in each month
        monthAvg.append(mean(numSteps[nextVal:(nextVal + numDays)]))    # gets avg
        nextVal += numDays
    
    print("The average steps taken each month were:")
    for i in range(1, 13):
        print(" " + '{:>9}'.format(month_name[i]) + " : " + '{:.2f}'.format(monthAvg[i - 1]))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
