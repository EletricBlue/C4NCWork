"""
                            Brock Griffith
                                C4NC
                    Python Ch 4: Strings: Immutability and Slicing
"""

#Diagram via flow charts, then pseudocode

# Subjects:
### STEPWISE REFINEMENT: how to write longer programs without getting bogged down in bugs.
### Using print() to debug our programs.

"""
STEPWISE REFINEMENT
1. start with a flow chart, figure out all complex logic
2. write pseudocode, then convert to comments
3. write code. GET ONE SMALL PIECE TO WORK, THEN TEST
4. test and correct until it works. Then move to the next bit
5. repeat steps 3 and 4 until project is done
"""
### it's easier to solve ten small problems than one giant problem
# if you are writing a small bit of code and there's a bug, you know exactly where it is
# you can use print() statements to test code, then comment it out using #
#print(var)
#add details to make it clearer: print("die roll: " + die_1)

"""
CRAPS GAME OUTLINE
a. user bets some money
b. two 6 sided dice are rolled
c. if a 7 or 11 is rolled, user wins
d. if a 2, 3, or 12 is rolled, user loses
e. if anything else is rolled, that number is saved, call that point number
f. if the point number is rolled before the 7, you win
g. if a 7 is rolled before the point number you lose
h. you win or lose money
i. you can choose to keep playing or stop
"""

#""coding"" ""challenge"", map out code via flow chart

#then, create pseudocode:

import random

#start game while loop

#declare user balance
userBalance = 500
print("You have", userBalance, "dollars")
    #get a bet from user
userBet = int(input("What do you bet? "))
    #roll two six sided dice, random(1,6)
roll1 = random.randint(1,6)
roll2 = random.randint(1,6)
rollSum = roll1 + roll2
print(roll1, roll2, rollSum)
    #compare sum to 7 or 11, user wins
if rollSum == 7 or rollSum == 11:
    print("player wins")
    userBalance += userBet
    #if sum == 2, 3, or 12, user loses
elif rollSum == 2 or rollSum == 3 or rollSum == 12:
    print("player loses")
    userBalance -= userBet
    #else save sum as point total
else:
    points = rollSum
    print("you have", points, "points")
    #in loop roll 2 more dice
    while True:
        rollOff1 = random.randint(1, 6)
        rollOff2 = random.randint(1, 6)
        rollOffSum = rollOff1 + rollOff2
        print("rolloff total:",rollOffSum)
        #if sum == point total, win
        if rollOffSum == points:
            print("player wins")
            userBalance += userBet
            break
        #if sum == 7, lose
        elif rollOffSum == 7:
            print("player loses")
            userBalance -= userBet
            break

        #keep rolling dice until outcome

    #ask user if they want to keep going or quit
    #if quit then break

"""
This piece of code is note done, that is what we do as homework
DO NOT JUST COPY PASTE MY CODE, I fear PJ will recognize my comments
"""