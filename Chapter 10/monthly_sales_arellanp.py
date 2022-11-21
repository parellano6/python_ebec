"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 11/19/2022

Description:
    This program asks the user for monthly sales data and then plots
    the slaes as a pie chart.

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
import calendar
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""


def main():
    fig, ax = plt.subplots()        # subplot
    month = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')  # month vals
    col = ['#4D4038', '#BAA892', '#5B6870', '#6E99B4', '#A3D6D7', '#085C11', '#849E2A', '#C3BE0B', '#E9E45B', '#6B4536', '#B46012', '#FF9B1A']  # color vals
    vals = []   # user input vals
    for i in range(1, 13):
        numVal = input("Enter the sales for " + calendar.month_name[i] + ": ")  # user input for each month
        vals.append(numVal)     # adds value to vals list
        
    ax.pie(vals, colors=col, labels=month)  # plots piechart
    ax.set_title('Monthly Sales Values')    # chart title
    plt.show()                              # plots the piechart and title


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
