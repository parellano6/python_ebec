"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/23/2022

Description:
    This program uses nested loops to collect data and
    calculate the average rainfall over a period of years

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
import datetime

"""Write new functions below this line (starting with unit 4)."""

def main():
    years = int(input("Enter the number of years: "))
    if years < 1:   # if < 1
        print("Invalid input; years must be greater than 0.")
    else:
        for i in range(1, years + 1):   # goes through each year
            totRain = 0             # total rain
            print("  For year No. " + str(i))
            j = 1               # iterator variable
            while j < 13:       # goes through each month
                month = datetime.date(1900, j, 1).strftime('%b')    # declares month
                print("    Enter the rainfall for " + month, end='')
                rainfall = float(input(".: ")) # user input for rainfall
                if rainfall < 0:        # if rain < 0
                    print("    Invalid input; rainfall cannot be negative.")
                else:
                    j += 1
                    totRain += rainfall
        totMonths = 12 * years
        avgVal = totRain / totMonths
        print("There are " + str(totMonths) + " months.")
        print("The total rainfall was " + "{:.2f}".format(totRain) + " inches.")
        print("The monthly average rainfall was " + "{:.2f}".format(avgVal) + " inches.")
            

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
