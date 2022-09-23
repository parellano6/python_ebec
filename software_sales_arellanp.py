"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/19/2022

Description:
    This program asks the user  to enter the number of packages purchased.
    The program then displays the amount of the discount (if any) and the total amount of
    the purchase after the discount.

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
    packages = int(input("How many packages will be purchased: "))       # packages purchased
    discount = 0        # discount which is changed according to quantity
    outVal = 0          # total amount according to quantity discount
    if packages < 0:
        print("  Invalid Input!")
    elif packages >= 0 and packages < 4:
        discount = 0
        print("  No discount applied.")
    elif packages >= 4 and packages <= 39:
        discount = 0.1
    elif packages > 39 and packages <= 199:
        discount = 0.15
    elif packages > 199 and packages <= 999:
        discount = 0.3
    else:
        discount = 0.42
        
    if discount != 0:
        print("  " + str(int(discount * 100)) + "% discount applied.")
    
    if packages >= 0:   # total price
        outVal = (1 - discount) * packages * 880
        print("  The total price to purchase " + str(packages) + " packages is $" + "{:,.2f}".format(outVal) + ".")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
