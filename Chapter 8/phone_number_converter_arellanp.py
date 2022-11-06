"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 11/05/2022

Description:
    This program asks the user for the numerical & alphabetical equivalent
    for a phone number, then it returns the numerical equivalent.

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
def convert_number(number):
    newNum = ''         # value with alphabetic equivalent
    
    for index, value in enumerate(number.upper()):
        for i in value:
            if i == 'A' or i == 'B' or i == 'C':    # A B C
                newNum = newNum + '2'
            elif i == 'D' or i == 'E' or i == 'F':  # D E F
                newNum = newNum + '3'
            elif i == 'G' or i == 'H' or i == 'I':  # G H I
                newNum = newNum + '4'
            elif i == 'J' or i == 'K' or i == 'L':  # J K L
                newNum = newNum + '5'
            elif i == 'M' or i == 'N' or i == 'O':  # M N O
                newNum = newNum + '6'
            elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':  # P Q R S
                newNum = newNum + '7'
            elif i == 'T' or i == 'U' or i == 'V':  # T U V
                newNum = newNum + '8'
            elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':  # W X Y Z
                newNum = newNum + '9'
            else:
                newNum = newNum + i
                
    return newNum


def main():
    phone = input("Enter a telephone number: ")     # user input
    
    phone = convert_number(phone)           # converted phone number
    print("The phone number is " + phone)


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
