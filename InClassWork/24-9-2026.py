"""
                            Brock Griffith
                                C4NC
                           Random Numbers
                            PJ Snavely
"""
import random

# += -= /= *=

roll = random.randint(1,100)
randRange = random.randrange(10) #assumes start at 0
#randbetween = random.randbetween()
trueRandom = random.random() #random percentage if *100, i.e random chance in percent form
uniRandom = random.uniform(1,10)

print(randRange)

#Programming Challenge: single polyhedral die roll
"""
dieSides =  int(input("How many sides?"))
result =  random.randint(1, dieSides)
print(result)
"""


#if and else statements
#python if statements are based on indnents
"""
tempBool = True
if tempBool == True:
    print("True!")
else:
    print("False!")
"""

"""
#Programming Challenge: Password Checker
password = input("Enter password: ")
if password != "pa55word":
    print("Password entered is incorrect!!")
else:
    print("Password is correct!")
"""

"""
ALWAYS WRITE PSEUDOCODE FIRST!!!!!
"""

"""
Pseudocode might look like this:
    a. get a random number from 1-6
    b. if that number is greater than or equal to five, print
    c. else print
    d. ask if they want to try again
"""

"""Programming Challenge: Pseudocode"""
#ask user for a number 1-10
#computerNum = random.randint(1,10) debugging
#print(computerNum) debugging
userNum = int(input("Say a random number from 1-10"))
if userNum > 10 or userNum < 1:
    print("That number is not 1-10!")
#compare that to a random integer 1-10
computerNum = random.randint(1,10)
if userNum == computerNum:
    # if the numbers match, the user wins
    print("You guessed my number!!")
else:
    # else tell the user that they did not win
    print("You did not guess my number...")