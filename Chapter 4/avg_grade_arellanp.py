"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 08/24/2022

Description:
    This program asks the user to enter a valid score five times. The program then displays
    a letter grade after each score is entered. After all the scores are entered, it displays the
    average of the scores and the letter grade corresponding to that average.

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
from statistics import mean

"""Write new functions below this line (starting with unit 4)."""


def main():
    score = []              # score array
    for i in range(5):      # iterage through score
        score.append(get_valid_score())     # adds values to score
        grade_calc = determine_grade(score[i])  # calculates grade
        print("  The letter grade for " + "{:.1f}".format(score[i]) + " is " + grade_calc + ".")        # print 
    
    avg = calc_average(score)       # average grade calc
    grade = determine_grade(avg)    # letter grade
    print("")
    print("Results:")
    print("  The average score is " + "{:.2f}".format(avg) + ".")
    print("  The letter grade for " + "{:.2f}".format(avg) + " is " + grade + ".")

def get_valid_score():
    val = 101       # intial val
    while val > 100 or val < 0:     # checks val 
        val = float(input("Enter a score: "))   # asks for input
        if val > 100 or val < 0:    # checks ouput
            print("  Invalid Input. Please try again.")     # prints
    return float(val)
    
def calc_average(val):
    average = float(mean(val))      # gets average
    return average                  # return
    
def determine_grade(val):
    if val >= 92:   # A
        letter = 'A'
    elif val >= 82: # B
        letter = 'B'
    elif val >= 73: # C
        letter = 'C'
    elif val >= 64: # D
        letter = 'D'
    else:           # F
        letter = 'F'
        
    return letter
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
