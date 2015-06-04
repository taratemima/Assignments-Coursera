# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.
import random

def name_to_number(name):
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
        #player_choice() 

def number_to_name(number):
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
        print "Sorry, pick a number between 0 to 4" 
        
def player_choice():
    print("\n")
    player_choice = input("Do you pick rock, scissors, paper, Spock, or lizard?")
    player_number = name_to_number(player_choice)
    print("Player chooses "+player_choice)
    return player_number 

def computer_guess():
    print("\n")
    comp_number = random.randrange(0,4)
    comp_choice = number_to_name(comp_number)
    print("Computer chooses "+comp_choice)
    return comp_number

def game():
    player_choice()
    computer_guess()
    
game() 
    
    