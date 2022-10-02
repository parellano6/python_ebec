"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 10/01/2022

Description:
    This program asks the user for an integer as an argument and returns True
    if the argument is a prime number, or False otherwise. Then prompts the
    user to enter a number. If the user enters -1, the program ends. Otherwise it
    display a message indicating whether or not the number is prime.

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
import math     #import math

"""Write new functions below this line (starting with unit 4)."""


def main():
    val = 0         # prime check value
    while val != -1:        # checks val
        val = int(input("Enter a positive integer (-1 to quit): "))      # asks user for value
        if val != -1:       # to output
            prime_bool = is_prime(val)      # bool prime value
            if prime_bool:              # checks prime
                print("  " + str(val) + " is prime!")   # true
            else:
                print("  " + str(val) + " is not prime.") # false
        
    

def is_prime(num):
    if num == 0 or num == 1:        # 1 or 0
        return bool(False)      # if 1 or 0
    
    for i in range(2, int(math.sqrt(num)) + 1):     # check prime loop
        if (num % i) == 0:      # check prime
            return bool(False)  # return
    return bool(True)       # return 

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
