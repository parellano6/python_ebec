"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 11/20/2022

Description:
    This program prints out a sine and cosine graph from 0 to 2pi.

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
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""


def main():
    x = np.arange(0, (np.pi * 2) + 0.1, 0.1)        # x range of values
    ampS = np.sin(x)                                # sin vals
    ampC = np.cos(x)                                # cos vals
    
    fig, ax = plt.subplots()        # plots stuff
    ax.spines['bottom'].set_position('zero')        # bottom frame moves
    ax.spines['left'].set_position('zero')          # moves left frame
    ax.spines['right'].set_color('none')            # deletes right frame
    ax.spines['top'].set_color('none')              # deletes top frame
    ax.set_xlim(0, np.pi * 2)                       # sets x limit
    pi = np.pi
    plt.xticks(np.arange(pi/2, pi * 2 +pi/2, step=(pi/2)), ['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$']) # x tick labels
    plt.yticks([-1, 1])     # y ticks
    plt.plot(x, ampS, color='red')  # sin
    plt.plot(x, ampC, color='blue') # cos
    plt.show()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
