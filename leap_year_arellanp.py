"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/19/2022

Description:
    This program asks the user asks the user to enter a year. The program then displays
    the number of days in February that year. 

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
    year = input("Enter a year: ")      # takes the input for the year
    if (int(year) % 100 == 0 and int(year) % 400 == 0) or (int(year) % 100 != 0 and int(year) % 4 == 0): # checks to see if the year is a leap year
        print("The year " + str(year) + " is a leap year.")     # first
        print("February of " + str(year) + " has 29 days.")     # second
    else:
        print("The year " + year + " is not a leap year.")      # first
        print("February of " + year + " has 28 days.")          # second


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
