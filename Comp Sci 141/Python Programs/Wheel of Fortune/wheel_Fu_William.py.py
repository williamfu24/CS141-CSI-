# Name: William Fu
# Date: 11/19/2015
# Class: Computer Science 141
# Pledge: I have neither given nor received unauthorized aid on this program.
# Description: This program is based off the game show wheel of fortune. Guess
    #letters until the phrase is filled
# Input: User inputs a secret phrase and then guess letters to figure out the
    #phrase
# Output: Program outputs the phrase with blanks in place for the letters and
    #keeps track of letters guessed, as well as money earned or lost for each
    #letter guessed, until the phrase is filled where it then states a win phrase
    #and displays the secret phrase as well as how much money was won

import random

# make_puzzle_string takes a secret phrase and a string representing
# the letters that Player 2 has already guessed in the game.  It
# returns a "puzzle string," which is just the secret phrase with
# all the non-guessed letters replaced with underscores.  Spaces
# remain as spaces in puzzle strings.
#
# Parameters: secret, a string with the secret phrase in it.
#             guessed_letters, a string with all of the letters guessed
#              so far in the puzzle.  This string may be empty, indicating
#              no letters have been guessed yet.
# Returns: the secret phrase with all the non-guessed letters transformed
#          into underscores.
#
# Example: make_puzzle_string("computer science", "cse") would return
# the puzzle string "c_____e_ sc_e_ce"
# Example: make_puzzle_string("computer science", "") wouuld return
# the puzzle string "________ _______"
def make_puzzle_string(secret, guessed_letters):
    puzzle_string="" #start with blank string so able to add blanks or letters
    for pos in range (0, len(secret),1):
        if secret[pos]== " ": #spaces are kept as spaces
            newchar=" "
            puzzle_string+=newchar
        elif secret[pos]in guessed_letters: #if letter is guessed then print letter
            newchar=secret[pos]
            puzzle_string+=newchar
        elif secret[pos]not in guessed_letters: #if letter is not guessed print _
            newchar="_"
            puzzle_string+=newchar
            
    return(puzzle_string)
        

# count_letter counts the number of times a given letter appears in a
# secret phrase.
#
# Parameters: secret, a string with a secret phrase in it.
#             letter, a one-character string with the letter to count.
# Returns: an integer representing the number of times the letter was
#          found in the secret phrase.
#
# Example: count_letter("computer science", 4) would return 3, because there are
#   three 'e's in the phrase 'computer science.'
def count_letter(secret, letter_guess): #counts the # of times the guessed letter in phrase
    letter_count=0
    for pos in range (0, len(secret),1):
        if secret[pos]==letter_guess:
            letter_count+=1 #counter to keep track of # of times in phrase
    return letter_count                    
        
    # Here is pseudocode to help you:

    # Make a string variable to store the letters that the user has guessed so far.
    #  This variable will start as the empty string, and will grow longer as the user
    #  guesses more letters.  As each letter is guessed, concatenate the letter to the
    #  end of this variable.
    
    # Make an integer variable to store the total amount of money won during the game.
    
    # Ask the user to enter a secret phrase.

    # Keep looping until the puzzle is solved:
        # Show the puzzle.
        # Show how much money the player has so far.
        # Spin the wheel; show how much consonants are worth.

        # Let the player guess a letter.  Use input validation to prevent
        # the player guessing a letter that they've guessed before.

        # Add the letter to the string containing the guessed letters.

        # Tell the player if their letter isn't in the puzzle.
        # Tell the player how much money they get if their letter is
        #  a consonant, or how much money they are charged if it's
        #  a vowel.

    # When the game is over, tell the player how much money they won.
    
    #pass  # Remove this line when you start coding this function.

def main():
    winnings=0 #amount of money won
    puzzle_string=" " #the puzzle string
    guessed_letters=" " #empty bank for guessed letters
    vowels="aeiou" #vowels to buy
    secret=input("Please enter the secret phrase?") #enter the secret phrase
    puzzle_string=make_puzzle_string(secret, guessed_letters) #keeps track of puzzle string
    while "_" in puzzle_string: #ensure game ends after all letters guessed/no _ left
        print("Puzzle is:", puzzle_string)
        print("You have",winnings,"dollars so far.")
        x=random.randint(1,100) #random value for consonant
        print("Consonants are worth", x,"dollars.")
        letter_guess=input("Enter a letter:")
        while letter_guess.isdigit(): #ensures guess is a letter
            letter_guess=input("That did not work. Please enter a letter:")
        for pos in range(0, len(guessed_letters),1): #ensures that you dont reguess a letter
            if letter_guess== guessed_letters[pos]:
                letter_guess=input("You already guessed that, please enter another letter:")
        letter_count=count_letter(secret,letter_guess)
        if letter_count==0:
            print("Letter not in the puzzle")
        elif letter_guess in "aeiou":
            print("You bought a vowel for 10 dollars each")
            print("There are", letter_count, letter_guess,"'s")
            money_loss= letter_count*10
            print("You spend", money_loss, "dollars.")
            winnings-=money_loss
        else:
            print ("There are", letter_count, letter_guess,"'s")
            money_gain=letter_count*x
            print("You get", money_gain, "dollars.")
            winnings+= money_gain
        guessed_letters+=letter_guess
        puzzle_string=make_puzzle_string(secret, guessed_letters)
    print("You win!!!")
    print("You won", winnings, "dollars total!!!")
    print("The phrase was", secret)



main()
