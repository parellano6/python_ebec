"""
Author: Paloma Arellano, arellanp@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 08/24/2022

Description:
    This program lets the user play a game of Rock, Paper,
    Scissors against the computer.

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
import random as rm

"""Write new functions below this line (starting with unit 4)."""
def get_computer_choice():
    out = rm.randint(1, 3)      # gets random value
    if out == 1:                # scissors
        return "scissors"
    elif out == 2:              # rock
        return "rock"
    else:                       # paper
        return "paper"

def get_player_choice():
    in_val = ""                 # intial value
    while in_val != "rock" and in_val != "paper" and in_val != "scissors":  # checks if valid
        in_val = input("Choose rock, paper, or scissors: ")
        if in_val != "rock" and in_val != "paper" and in_val != "scissors": # invalid
            print("You made an invalid choice. Please try again.")
    return in_val

def get_winner(computer, person):
    if computer != person:      # checks who won
        if computer == "rock" and person == "scissors":
            return "computer"
        elif person == "rock" and computer == "scissors":
            return "player"
        elif computer == "paper" and person == "scissors":
            return "player"
        elif person == "paper" and computer == "scissors":
            return "computer"
        elif computer == "paper" and person == "rock":
            return "computer"
        else:
            return "player"
    else:                   # returns a tie
        return "tie"

def main():
    result = "tie"          # keeps repeating
    while result == "tie":
        comp = get_computer_choice()    # computer
        pers = get_player_choice()      # player
        print("  The computer chose " + comp + ", and you chose " + pers + ".")
        result = get_winner(comp, pers) # winner
        if result == "computer":        # computer wins
            print("  " + comp + " beats " + pers)
            print("  You lost.  Better luck next time.")
        elif result == "player":        # player wins
            print("  " + pers + " beats " + comp)
            print("  You won the game!")
        else:                           # tie
            print("  It's a tie. Starting over.\n")
    print("Thanks for playing.")
        


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
