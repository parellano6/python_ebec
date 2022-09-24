"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 03.4 - Organisms
Date: 09/24/2022

Description:
    This program asks the user to enter the starting number of organisms, 
    the average daily population increase (as a percentage), and the number
    of days the organisms will be left to multiply. Predicts the approximate 
    size of a population of organisms.

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
    popul = input("Starting population, in thousands: ")        # starting population
    dayPer = input("Average daily increase, in percent: ")      # avg daily increase
    days = int(input("Number of days to multiply: "))           # num days to multiply
    
    totVal = float(popul)
    print("Day   Approx. Pop")
    for i in range(days + 1):
        print("{:3.0f}".format(i) + "{:14.3f}".format(totVal))
        totVal += totVal * float(dayPer) * 0.01


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
