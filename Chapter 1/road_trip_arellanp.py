"""
Author: Your Name, arellanp@purdue.edu
Assignment: 01.1 - Road Trip
Date: 09/04/2022

Description:
    This program will estimate the cost for fuel for 
    the road trip according to the inputs for distance,
    price of gas, and fuel efficiency of the vehicle.

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
import math

"""Write new functions below this line (starting with unit 4)."""


def main():
    """Write your mainline logic below this line (then delete this line)."""
    print("Road trip fuel cost estimator:")
    distance = float(input("  How far away is your destination (miles)? "))            # destination distance
    price = float(input("  What is the average price of gas (dollars per gallon)? "))  # average price of gas
    mpg = float(input("  What is the fuel efficiency of your vehicle (mpg)? "))        # fuel efficiency of vehicle
    
    tot_cost = (2 * distance) * price / mpg
    
    print("\nThe fuel cost for this trip is approximately $" + str(math.floor(tot_cost)) + ".")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
