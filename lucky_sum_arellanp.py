"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 10/01/2022

Description:
    This program asks the user for two integer values, then it calculate 
    and return the sum of the “lucky numbers” which are all of the numbers from
    the smallest argument to the largest argument that are not divisible by 3.

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
    int1 = input("Enter the first integer: ")
    int2 = input("Enter the second integer: ")
    
    tot = lucky_sum(int(int1), int(int2))
    print("The sum of the lucky numbers is " + "{:,.0f}".format(tot) + ".")


def lucky_sum(val1, val2):
    sum = 0
    if val2 < val1:
        temp = val1
        val1 = val2
        val2 = temp
    for i in range(val1, val2 + 1):
        if i % 3 != 0:
            sum = sum + i
    return sum

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
