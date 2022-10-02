"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 09/04/2022

Description:
    This program asks the user for their name, and then displays
    a greeting using their name.

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
    cookies = float(input("How many cookies do you want to make? "))    # number of cookies to make

    butter = 1.25 * cookies / 48    # amount of butter needed
    sugar = 1.5 * cookies / 48      # amount of sugar needed
    flour = 2.5 * cookies / 48      # amount of flour needed

    print("To make " + format(cookies, ',.0f') + " cookies, you will need:")
    print(format(butter, '10,.2f') + " cups of butter")
    print(format(sugar, '10,.2f') + " cups of sugar")
    print(format(flour, '10,.2f') + " cups of flour")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
