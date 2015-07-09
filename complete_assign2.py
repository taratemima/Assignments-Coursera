# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

list_of_guesses = []
thousand = False 
max_range = 100
guesses = 7
secret_number = random.randint(0, max_range)
counter = 0

#will need function that changes global variable thousand when a button is pressed
#print message 
def new_game():
    global max_range
    print("New game. Range is from 0 to "+str(max_range))
        
def input_guess(guess):
    player_number = int(guess)
    global guesses
    guesses_left = guesses
    global counter
    while(counter < guesses_left):
        print("Guess was "+str(player_number))
        print("Number of guesses remaining "+str(guesses_left - counter))
        if player_number == secret_number:
            print("Correct")
            print "\n"
            counter = 0
            new_game()
            break 
        elif player_number > secret_number:
            print("Lower")
            counter = counter + 1
            print "\n"
            break
        elif player_number < secret_number:
            print("Higher")
            counter = counter + 1
            print "\n"
            break
    if counter == guesses_left:
        print("You ran out of guesses \n")
        new_game()
        
    
def range100():
    global thousand
    thousand = False
    global max_range 
    max_range = 100
    global guesses 
    guesses = 7
    global secret_number
    secret_number = random.randint(0, max_range)
    new_game()
    
    
   

def range1000():
    global thousand
    thousand = True
    global max_range
    max_range = 1000
    global guesses
    guesses = 10
    global secret_number
    secret_number = random.randint(0,max_range)
    new_game()
 
    
    
#Why do neither of these change the global variable?

        
frame = simplegui.create_frame("Guess the number game", 200, 200)
guess_number = frame.add_input("Guess the number", input_guess, 50)
frame.add_button("Range is (0-100)", range100, 200)
frame.add_button("Range is (0-1000)", range1000, 200)

#range100()
#range1000()
new_game()
frame.start()



