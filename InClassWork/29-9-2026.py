"""
                            Brock Griffith
                                C4NC
                           Python Ch 3
          elif, and if, elif, and else statement limitations
                            PJ Snavely
"""
import random

# if [logic statement]:
#   tab and then code
# else:
#   tab and more code

# x is dividable by y if x % y == 0

""" WHAT IF IT'S NOT AN EITHER OR???? """
#that is what elif is for
"""
if logical comparison 1:
    statement 1
elif logic 2: 
    statement 2
else:
    statement 3
"""

""" DO NOT MAKE A WALL OF ELIF STATEMENTS EVEN THOUGH YOU CAN I.E, DON'T PULL AN UNDERTALE """
# The else is always optional, but good for error checking

"""
### PROGRAMMING CHALLENGE 1: elif ###

#ask the user to enter a number from 1 to 10
userNum = int(input("give me a number from 1 - 10 "))
#generate a random integer from 1 to 10
compNum = random.randint(1,10)

#compare those numbers, print win if equal
if userNum == compNum:
    print("You've won!!")

#otherwise, tell which is greater
elif userNum > compNum:
    print("your number is higher")
elif userNum < compNum:
    print("your number is lower")
else:
    print("ERROR")
"""

""" 
optional, technically more efficient way:
if == :
    print win
elif > :
    print higher
else:
    print lower
"""

#if Clauses
"""
if x is greater than 10, print D
if x is greater than 5, print C
if x is greater than 1, print A
else, print B

### NESTED IF STATEMENTS ###
if x>=5:
    if x>10:
        print(D)
    else:
        print(C)
else:
    if x<= 1:
        print(A)
    else:
        print(B)
"""

### PROGRAMMING CHALLENGE 2: Nested if Statements ###

#ask the user to enter a number from 1 to 10
userNum = int(input("give me a number from 1 - 10 "))
#generate a random integer from 1 to 10
compNum = random.randint(1,10)

#compare those numbers, print win if equal
if userNum == compNum:
    print("You've won!!")

#otherwise, tell which is greater
else:
    if userNum > compNum:
        print("your number is higher")
    else:
        print("your number is lower")