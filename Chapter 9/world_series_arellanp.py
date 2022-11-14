"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 09.2 - World Series
Date: 11/13/2022

Description:
    This program asks the user for a year to then disply the team
    who won the World Series that year (if it exists) and how many times they've
    won.

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
def load_winners_data():
    year_dict = {}          # years and team dict
    times_dict = {}         # times won and team dict
    year = 1903
    with open('WorldSeriesWinners.txt', 'r') as file:           # opens file
        for line in file:
            if year == 1904 or year == 1994:                # checks if 1904 or 1994
                year += 1
            year_dict[year] = line.strip()      # adds to dictionary
            if line.strip() in times_dict.keys():
                times_dict[line.strip()] = times_dict.get(line.strip()) + 1        # adds to dictionary
            else:
                times_dict[line.strip()] = 1
            year += 1
    return times_dict, year_dict

def main():
    times_dict, year_dict = load_winners_data()         # dictionaries
    year = int(input("Enter a year in the range 1903 -- 2021: "))       # input
    if year in year_dict.keys():
        winner = year_dict[year]        # team name
        times = times_dict[winner]      # times won
        print("  The " + winner + " won the World Series in " + str(year) + ".")
        print("  They have won the World Series " + str(times) + " times.")
    elif year == 1904 or year == 1994:
        print("  The World Series wasn't played in the year " + str(year) + ".")
    else:
        print("  Data for the year "+ str(year) +" is not included in this system.")
        


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
