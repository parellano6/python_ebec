"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 09.3 - Course Info
Date: 11/13/2022

Description:
    This program asks the user for a course name, and then
    outputs the description if it exists.

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
def get_course_data():
    course_info = {
        "CS101" : {
            "room" : '3004',
            "instructor" : "Django",
            "time" : "9:00 a.m."
        },
        "CS102" : {
            "room" : '4501',
            "instructor" : "Idle",
            "time" : "10:00 a.m."
        },
        "CS103" : {
            "room" : '6755',
            "instructor" : "Rich",
            "time" : "11:00 a.m."
        },
        "NT110" : {
            "room" : '1244',
            "instructor" : "Marshal",
            "time" : "12:00 p.m."
        },
        "CM241" : {
            "room" : '1411',
            "instructor" : "Pickle",
            "time" : "2:00 p.m."
        }
    }
    return course_info

def main():
    course_info = get_course_data()     # gets nested dictionary
    course = input("Enter a course number: ")   # user input
    if course in course_info.keys():    # finds if course exists
        print("  The details for course " + course + " are:")       # prints out details
        print("    Instructor: " + course_info[course]["instructor"])
        print("          Room: " + str(course_info[course]["room"]))
        print("          Time: " + course_info[course]["time"])
    else:
        print("  " + course + " is an invalid course number.")      # prints if does not exist


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
