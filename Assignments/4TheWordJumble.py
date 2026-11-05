"""
Brock Griffith
Assignment: Word Jumble
"""

#the computer picks a random word and then jumbles it
#the player then has to guess the original word

import random

#create a sequence of words to choose from
WORDS = ("python", "snake", "mixed", "jump", "extremely", "excommunicate")

#pick one word randomly from the sequence
word = random.choice(WORDS)

#create a variable to use later to see if the guess is correct
correct = word

#create an empty jumble word
jumble = ""
#while the chosen word has letters in it
while word:
    #slice a random letter from the chosen word
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
    #append the random letter to the jumble word

#start the game
print(
    """
            Welcome to Word Jumble!
            
    Unscramble the letters to make a word.
        (Press the enter key to quit.)
    """
)

print("the Jumble is:", jumble)
#get input from user and check if it is correct
guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that was incorrect.")
    guess = input("Your guess: ")
#congratulate player if they are correct
if guess == correct:
    print("That's it! You guessed the word!\n")
    print("Thanks for playing.")
    input("\n\nPress the enter key to exit.")