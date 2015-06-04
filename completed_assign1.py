# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name.lower() == 'rock':
        return 0
    elif name.lower() == 'spock':
        return 1
    elif name.lower() == 'paper':
        return 2
    elif name.lower() == 'lizard':
        return 3
    elif name.lower() == 'scissors':
        return 4
    else:
        print("Sorry, that is not one of the choices")
        

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("Sorry, pick a number between 0 to 4") 
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print("\n")
    # print out the message for the player's choice
    print("Player chooses "+player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print("Computer chooses "+comp_choice)

    # compute difference of comp_number and player_number modulo five
    answer = (comp_number - player_number)%5
    #I ran another version of the program, with random numbers for both 
    #player and computer. I used player numbers, and assigned outcomes
    #based on what the computer drew to get the remainder, and deducting  
    #from the rules 
    # use if/elif/else to determine winner, print winner message
    #I realize it looks messy and could be refactored, but this is so I can
    #debug the if statements more easily. 
    if(answer == 1):
        if(player_number == 1):
            print("Computer wins!")
        elif(player_number == 3) :
            print("Player wins!")
        elif(player_number == 4):
            print("Computer wins")
        elif(player_number == 2):
            print("Computer wins!")
        else:
            print("Computer wins!")
             
    elif(answer == 2):
        if((player_number == 1) or (player_number == 3)):
            print("Computer wins!")
        elif(player_number == 2):
            print("Computer wins!")
        elif(player_number == 4):
            print("Computer wins!")
        else:
            print("Computer wins!") 

    elif(answer == 3):
        if((player_number == 0) or (player_number == 3)):
            print("Player wins!")
        elif(player_number == 1):
            print("Computer wins!")
        elif(player_number == 2):
            print("Player wins!")
        else:
            print("Player wins!")
    elif(answer == 4):
        if(player_number == 0):
            print("Computer wins!")
        elif(player_number == 1):
            print("Player wins!")
        elif(player_number == 4):
            print("Player wins!")
        elif(player_number == 2):
            print("Player wins!")
        else:
            print ("Player wins!") 
    else:
        print("Player and computer tie!")

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


