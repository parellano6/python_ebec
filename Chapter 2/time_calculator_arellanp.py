"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 09/19/2022

Description:
    This program asks the user to enter a number of seconds and then displays the total
    time entered in days, hours, minutes and seconds. Only non-zero units should be displayed
    and all units should be separated by proper punctuation. 

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
    time = int(input("Please enter a time in seconds: "))    # time input
    
    days = time / 86400     # day calculated
    hours = round((days - int(days)) * 86400) / 3600    # hours calc
    minutes = round((hours - int(hours)) * 3600) / 60   # minutes calc
    seconds = round((minutes - int(minutes)) * 60)      # seconds calc
    
    count = 0               # make sure and not there
    
    if time < 60:       # checks if less than 60
        print("  " + "{:,}".format(time) + " seconds is less than one minute.")   
    else:               # else >= 60
        print("  " + "{:,}".format(time) + " seconds equals ", end="")
        if (int(days) > 0):
            print(str(int(days)) + " day(s)", end="")
            if (int(hours) == 0 and int(minutes) == 0 and int(seconds) == 0):
                print(".")
            if (int(hours) > 0 or int(minutes) > 0 or int(seconds) > 0):
                if int(minutes) != 0 and int(seconds) != 0 and int(hours) != 0:
                    print(", ", end="")
        if (int(hours) > 0):
            if (int(days) > 0) and int(minutes) == 0 and count == 0:
                print(" and ", end="")
                count = 1
            print(str(int(hours)) + " hour(s)", end="")
            if (int(minutes) > 0 or int(seconds) > 0):
                if int(minutes) != 0 and int(seconds) != 0:
                    print(", ", end="")
            if (int(minutes) == 0 and int(seconds) == 0):
                print(".")
        if (int(minutes) > 0):
            if ((int(days) > 0) or (int(hours) > 0)) and count == 0 and int(seconds) == 0:
                print( " and ", end="")
                count = 1
            print(str(int(minutes)) + " minute(s)", end="")
            if (int(seconds) == 0):
                print(".")
        if (int(seconds) > 0):
            if ((int(days) > 0) or (int(minutes) > 0) or (int(hours) > 0)) and count == 0:
                print(" and ", end="")
                count = 1
            print(str(int(seconds)) + " second(s).")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
