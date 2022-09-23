"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 01.2 - Interest
Date: 09/04/2022

Description:
    This program displays the balance of the user's bank acccount
    after a certain number of years they input. The program uses
    inputs for intial depost, interest rate, time to earn interest,
    and number of times the interest is compounded per year.

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
    print("Enter the following parameters.")
    deposit = float(input("  The initial deposit? "))                              # intital deposit
    interest = float(input("  The annual interest rate in percent? "))                 # annual interest rate (%)
    years = float(input("  The number of years the account earn interest? "))         # years the account earns interest
    times = float(input("  The number of times interest is compounded each year: "))  # number of times interest is compounded per year

    balance = deposit * (1 + ((interest / 100) / times)) ** (times * years)
    print("The balance of this account will be $" + "{:,.2f}".format(balance) + " after " + "{:,.1f}".format(years) + " years.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
