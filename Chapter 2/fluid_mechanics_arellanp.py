"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 08/24/2022

Description:
    This program asks the user for the velocity of the
    water flowing through a pipe (V ), for the pipe’s diameter (d),
    and to select the water’s temperature (T ) from 5 ◦C, 20 ◦C, 
    and 50 ◦C. The program then calculates the Reynolds
    number based on the input values.

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
    temp = float(input("Enter the temperature in °C as 5, 20, or 50: "))    # temperature
    vel = float(input("Enter the velocity of water in the pipe (m/s): "))   # velocity
    dia = float(input("Enter the pipe's diameter (m): "))                   # diameter

    outVal = 0      # Reynolds number
    
    if temp == 5:   # checks if 5
        outVal = (vel * dia) / (1.52 * (10 ** (-1 * 6)))
    if temp == 20:  # checks if 20
        outVal = (vel * dia) / (1 * (10 ** (-1 * 6)))
    if temp == 50:  # checks if 50
        outVal = (vel * dia) / (5.54 * (10 ** (-1 * 7)))
    
    print("At " + str(temp) + "°C, the Reynolds number for flow at " + str(vel) + " m/s in a " + str(dia) + " m diameter pipe is " + "{:.2e}".format(outVal) + ".")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
