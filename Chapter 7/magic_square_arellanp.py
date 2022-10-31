"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 07.4 - Magic Square
Date: 10/29/2022

Description:
    This program checks that a 9x9 box is a Lu Shu Magic
    Square. Which means each row, column, and diagonal sum up
    to 15, and the grid contains values 1-9 only once throughout.

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
import numpy as np

"""Write new functions below this line (starting with unit 4)."""
def print_square(listIn):       # prints square
    for i in listIn:
        print("  ", end="")     # prints columns
        count = 0
        for j in i:
            if count != 2:
                print(j, end=" ")   # prints rows
                count += 1
            else:
                print(j, end="")    # prints rows
        print("")
    return

def is_magic(listIn):       # checks to see if quare is Lo Shu
    checkList = []
    for i in listIn:    # checks to see if value occurs once
        for j in i:
            if j in checkList:
                return False
            else:
                checkList.append(j)
                
    for i in range(3):  # checks columns
        sumCol = sum([col[i] for col in listIn])
        if sumCol != 15:
            return False
        
    for i in range(3): # checks rows
        sumCol = sum(listIn[i])
        if sumCol != 15:
            return False

    diagonal1 = sum([row[-i] for i, row in enumerate(listIn, start=1)])
    diagonal2 = sum(np.diag(listIn))
    
    if diagonal1 != 15 or diagonal2 != 15:      # checks diagonal values
        return False

    return True      # returns true if is Lo Shu

def print_out(inBool):  # prints if true or false
    if inBool:
        print("It is a Lo Shu magic square!\n")
    else:
        print("It is not a Lo Shu magic square.\n")
    return

def main():
    square1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]     # first square
    square2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]     # second square
    square3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]     # third square
    
    print("Your square is:")
    print_square(square1)
    print_out(is_magic(square1))
    
    print("Your square is:")
    print_square(square2)
    print_out(is_magic(square2))
    
    print("Your square is:")
    print_square(square3)
    print_out(is_magic(square3))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
