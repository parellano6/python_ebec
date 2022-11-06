"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 08.5 - Number Reader
Date: 11/05/2022

Description:
    This program reads the random_numbers.txt file, then calculates
    and displays the number of random numbers, minimum of the numbers,
    maximum of the numbers, sum of the numbers, and the average of the
    numbers.

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


def main():
    numVals = []                                            # vals list
    with open('random_numbers.txt', 'r') as file:           # opens file
        for line in file:
            numVals.append(line.rstrip())                   # adds value to list
           
    numVals = list(map(int, numVals))       # converts list to int vals
    maxVal = max(numVals)                   # max
    minVal = min(numVals)                   # min
    sumVal = sum(numVals)                   # sum
    avgVal = mean(numVals)                  # avg
    lenVals = len(numVals)                  # len
    
    print('{:,.0f}'.format(lenVals) + " numbers were read from the file.")
    print("Min: " + '{:,.0f}'.format(minVal))
    print("Max: " + '{:,.0f}'.format(maxVal))
    print("Sum: " + '{:,.0f}'.format(sumVal))
    print("Avg: " + '{:,.1f}'.format(avgVal))
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
