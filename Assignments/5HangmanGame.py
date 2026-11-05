"""
Brock Griffith
Assignment: Checklist
"""
#imports
import random

#CONSTANTS
GALLOW = (
"""
------
|    |
|
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|   -+-
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|    |
|    |
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   | |
|   | |
|
----------
""")

MAX_WRONG = len(GALLOW) - 1
WORDS = ("OVERSIZED", "CLAIM", "SNAKE", "COBRA", "YOSEMITE")

#Computer picks a random word
word = random.choice(WORDS)

soFar = "-" * len(word)     #dashes for the number of letters in the word
wrong = 0                   #number of wrong guesses guessed
used =[]                    #to be filled with letters already used

#The player must guess one word at a time
print("Welcome to hangman. Good Luck!")
while wrong < MAX_WRONG and soFar != word:
    print(GALLOW[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", soFar)
    guess = input("Enter a letter here: ").upper()

    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("Enter a letter here: ").upper()

    used.append(guess)
#If the player can't guess the word in time, hangman gets the noose
    if guess in word:
        print("\nCorrect!", guess, "is in the word!")

        #create a new soFar to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += soFar[i]
        soFar = new
    else:
        print("wrong")
        wrong += 1
if wrong == MAX_WRONG:
    print(GALLOW[wrong])
    print("\nYou've been hanged! :(")
else:
    print("You've got it!")

print("\n The word was", word)

input("\nPress the enter key to exit.")