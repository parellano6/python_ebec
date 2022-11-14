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
    first = {}          # first dictionary
    with open('python_1.txt', 'r') as file:           # opens file
        for line in file:
            for word in line.split():
                val = (word.strip()).lower()
                inVal = ''
                for i in val:
                    if (i.isalpha()) or i == '-' or i == "'" or i == '/':       # values to look out for
                        inVal += i
                if inVal == 'https//wwwpythonorg/':
                    inVal = "https://www.python.org"
                if inVal == "walls'":
                    inVal = "walls"
                if inVal in first.keys():
                    first[inVal] = first.get(inVal) + 1        # adds to dictionary
                else:
                    first[inVal] = 1
    first = OrderedDict(sorted(first.items()))      # orders dictionary
                    
    #print(first)
    with open("python_1_word_frequency.txt", 'w') as file:
        for key, val in first.items():
            file.write('%s: %s\n' % (key, val))
            
    second = {}         # second dictionary
    with open('python_2.txt', 'r') as file:           # opens file
        for line in file:
            for word in line.split():
                val = (word.strip()).lower()
                inVal = ''
                for i in val:
                    if (i.isalpha()) or i == '-' or i == "'" or i == '/' or i == "1":   # values to look out for
                        inVal += i
                if inVal == 'https://www.python.org/':
                    inVal = "https://www.python.org"
                if inVal == "walls'":
                    inVal = "walls"
                if inVal == "c/c/java":
                    inVal = "c/c++/java"
                if inVal in second.keys():
                    second[inVal] = second.get(inVal) + 1        # adds to dictionary
                else:
                    second[inVal] = 1
    second = OrderedDict(sorted(second.items()))        # orders dictionary
                    
    #print(second)
    with open("python_2_word_frequency.txt", 'w') as file:
        for key, val in second.items():     # iterates through dictionary
            file.write('%s: %s\n' % (key, val))     # writes values in both files
            
    notIn = {}      # not in dictionary
    with open("common_words.txt", 'w') as file:
        for firstKey in first:      # iterates through dictionary
            #print(firstKey)
            if firstKey in second.keys():
                file.write(firstKey + "\n")
            else:
                notIn[firstKey] = 0
    
    for secondKey in second:            # iterates through dictionary
        if secondKey not in first.keys():
            notIn[secondKey] = 0
    
    notIn = OrderedDict(sorted(notIn.items()))      # orders dictionary
    #print(notIn)
    
    with open("eitherbutnotboth.txt", 'w') as file:
        for key in notIn:       # iterates through dictionary
            file.write(key + "\n")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
