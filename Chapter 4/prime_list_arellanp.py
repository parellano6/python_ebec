"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 04.5 - Prime List
Date: 10/01/2022

Description:
    This program lists all of the
    primes from 2 up to a user specified limit. 

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
import math    # imports math

"""Write new functions below this line (starting with unit 4)."""

def is_prime(num):
    if num == 0 or num == 1:        # 1 or 0
        return bool(False)      # if 1 or 0
    
    for i in range(2, int(math.sqrt(num)) + 1):     # check prime loop
        if (num % i) == 0:      # check if prime
            return bool(False)  # return if false
    return bool(True)       # return if true

def main():
    arr = []        # initial array
    num = int(input("Enter a positive integer: "))  # user input postive int
    for i in range(num + 1):    # for loop for user input
        if is_prime(i):         # checks if prime
            arr.append(i)       # append to array
    
    print("The primes up to " + str(num) + " are: ", end="")    # print
    print(', '.join(map(str, arr))) # print array

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
