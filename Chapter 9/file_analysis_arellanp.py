"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 09.4 - File Analysis
Date: 11/13/2022

Description:
    This program reads the python_1.txt and python_2.txt files
    then figures out the frequency of words in each file, finds the common
    words between the two, and different words between the two.

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
from collections import OrderedDict

"""Write new functions below this line (starting with unit 4)."""


def main():
    first = {}
    with open('python_1.txt', 'r') as file:           # opens file
        for line in file:
            for word in line.split():
                val = (word.strip()).lower()
                inVal = ''
                for i in val:
                    if (i.isalpha()) or i == '-':
                        inVal += i
                if inVal in first.keys():
                    first[inVal] = first.get(inVal) + 1        # adds to dictionary
                else:
                    first[inVal] = 1
    first = OrderedDict(sorted(first.items()))
                    
    print(first)
    with open("python_1_word_frequency.txt", 'w') as file:
        for key, val in first.items():
            file.write('%s: %s\n' % (key, val))
            
    second = {}
    with open('python_2.txt', 'r') as file:           # opens file
        for line in file:
            for word in line.split():
                val = (word.strip()).lower()
                inVal = ''
                for i in val:
                    if (i.isalpha()) or i == '-':
                        inVal += i
                if inVal in first.keys():
                    second[inVal] = second.get(inVal) + 1        # adds to dictionary
                else:
                    second[inVal] = 1
    second = OrderedDict(sorted(second.items()))
                    
    print(second)
    with open("python_2_word_frequency.txt", 'w') as file:
        for key, val in second.items():
            file.write('%s: %s\n' % (key, val))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
