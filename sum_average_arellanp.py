"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 03.2 - Sum Average
Date: 09/23/2022

Description:
    This program asks the user to enter a series of non-negative numbers
    (positive numbers or zero). The user should enter a negative number to signal the end of
    the series. After all the non-negative numbers have been entered, the program should display
    their sum and average.

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
    numVal = 0      # input value
    sumVal = 0      # summed value of inputs
    count = 0       # tot num of inputs
    
    while numVal >= 0:      # loop through inputs
        sumVal += numVal
        count += 1;
        numVal = float(input("Enter a non-negative number (negative to quit): "))
    
    count -= 1
    
    if count == 0:      # prints if no inputs
        print("  You didn't enter any numbers.")
    else:               # goes through if inputs
        mean = sumVal / count   # mean val
        
        print("  You entered " + str(count) + " numbers.")
        print("  Their sum is " + "{:.3f}".format(sumVal) + " and their average is " + "{:.3f}".format(mean) + ".")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
