"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 04.1 - Falling
Date: 10/01/2022

Description:
    This program uses an object's falling time (in seconds) to
    calculate and returns the distance in meters that the object will fall
    during that time. 

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
    print("Time (s)  Distance (m)")         # print table label
    print("----------------------")         # print --
    for i in range(5, 51, 5):
        time = falling_dist(i)              # time falling
        print("{:8.0f}".format(i) + "     " + "{:9.1f}".format(time))   # return

def falling_dist(fall_time):
    dist = 0.5 * 8.87 * (fall_time ** 2)    # distance falling
    return dist


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
