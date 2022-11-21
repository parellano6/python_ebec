"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 10.3 - COVID 19 Cases
Date: 11/20/2022

Description:
    This program takes data about COVID-19 in Indiana and
    calculates the total number of cases for each week and 
    displays it as a graph.

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
import datetime
import numpy as np

"""Write new functions below this line (starting with unit 4)."""


def main():
    data = []
    dateVals = []
    val = 0
    with open('indiana_covid-19_data_fall_2022.txt', 'r') as file:           # opens file
        for line in file:
            count = 0
            for word in line.split():   # gets each value
                if count == 2:
                    val += (float(word.strip()) / 1000) # gets each cases val
                    data.append(val)        # adds value to data list
                if count == 0:
                    y, m, d = (word.strip()).split('-')
                    dt = datetime.date(int(y), int(m), int(d))
                    dateVals.append(dt)     # adds date to list
                count += 1
        
    fig, ax = plt.subplots()                            # creates figure
    plt.bar(dateVals, height=data, width=7)                                    # plots data
    ax.set_xlim(datetime.date(2020, 1, 1), datetime.date(2022, 11, 1))      # sets x axis limits
    ax.set_title('Weekly Positive COVID-19 Cases in Indiana')              # title
    ax.set_xlabel('Date')                  # x axis title
    ax.set_ylabel('Number of Cases (in thousands)')     # y axis title
    fig.autofmt_xdate()     # formats date
    plt.yticks(np.arange(0, 2251, 250))
    plt.show()                                          # shows plot


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
