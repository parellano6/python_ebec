"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 11/19/2022

Description:
    This program reads data for the average price of gas in the US in 2008. 
    Then plots the data as a line graph.

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
import matplotlib.pyplot as plt
import numpy as np

"""Write new functions below this line (starting with unit 4)."""


def main():
    data = []
    with open('2008_Weekly_Gas_Averages.txt', 'r') as file:           # opens file
        for line in file:
            data.append(float(line.strip()))        # adds value to data list
    
    x = np.arange(1, 53)        # range of values from 1-53
    
    fig, ax = plt.subplots()                            # creates figure
    ax.margins(x=0)   
    ax.set_ylim(1.5, 4.25)                                  # eliminates x margins
    ax.set_title('2008 Weekly Gas Prices')              # title
    ax.set_xlabel('Weeks (by number)')                  # x axis title
    ax.set_ylabel('Average Price (dollars/gallon)')     # y axis title
    ax.grid()                                           # enables grid
    ax.plot(x, data)                                    # plots data
    plt.show()                                          # shows plot
    
            
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
