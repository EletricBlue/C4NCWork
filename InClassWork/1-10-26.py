"""
                            Brock Griffith
                                C4NC
                    Python Ch 3 (end): While loops
"""
import random

ran = random.random

### LOOPS ###

# while loop and for loop

"""
while logical expresion:
    statement1
    statement2
    ...
"""

# If the logical expression remains true forever it is an INFINITE LOOP (these are usually bad)

""" 
contextual example:

count = 0
while count < 10:
    count += 3
    print(count)
"""

# the proper name for 'count' is called a SENTRY VARIABLE, but no one knows that and it doesn't matter
# you HAVE to initialize the sentry variable before you begin a while loop

### PROGRAMMING CHALLENGE: Password Checker in a while loop ###
"""
prompt the user to give their password and store it in a variable
if the password is not equal to pa55word tell the user they've entered an incorrect password
the program should repeatedly ask for the password until they enter the correct one.
when they do that, the loop should end
"""

"""
passCheck = False

#the program should repeatedly ask for the password until they enter the correct one.
while passCheck == False:
    #prompt the user to give their password and store it in a variable
    userPass = input("Please input your password: ")
    if userPass == "pa55word":
        #when they do that, the loop should end
        passCheck = True
        print("welcome, user")
    #if the password is not equal to pa55word tell the user they've entered an incorrect password
    else:
        print("you've entered an incorrect password")
"""

#PJ QUOTE: "This is not ideal code." but it IS easy to understand

#BREAKING OUT OF A LOOP: you can use the word (command) 'break'
#break will end a while loop immediately

#CONTINUING... INTO(?) A LOOP: 'continue' will cause the program to jump back to the start of the loop to CONTINUE evaluating
#USE 'continue' SPARINGLY, OVERUSE CAN MAKE CODE MESSY AND CONFUSING

### PROGRAMMING CHALLENGE: Password Checker w/ while loop and w/ break or continue
"""
prompt the user to give their password and store it in a variable
if the password is not equal to pa55word tell the user they've entered an incorrect password
the program should repeatedly ask for the password until they enter the correct one.
when they do that, the loop should end, make sure to use at least one break or continue
"""

while True:
    userPass = input("please enter your password: ")
    if userPass == "pa55word": #in the real world this line would be comparing two variables, so that "pa55word" could be modified and used outside the loop
        print("welcome, user")
        break
    else:
        print("incorrect password, try again")

#according to PJ this is the cleanest version of this code, I tend to agree.

#ABOVE ALL: use them sparringly; rule of thumb: try not to put more than one in a single loop

### LOGICAL CONDITIONS ###
# another word for a logical statement or a collection of them
#you can check multiple conditions at a time by using AND:
"""
if carPrice <= 20000 and carColor == "red":
    print("buy it!!")
else:
    print("don't buy it!!!")

#just like the AND function in Excel
"""

#again, try not to overuse AND because it can also make messy code

#logical operators:
"""
and - only true if both are true
or - true if either are true
not - flips the answer, true if the statement is false

Tip: work from the inside out when figuring out not():
var1 = true var2 = true
not(var1 == false and var2 == true)
var1 == false and var2 == true <-- this is false
not(false) <-- this is true

kinda like exponentials inside of parenthesis when doing math by hand
"""

### PROGRAMMING CHALLENGE ###
"""
store your own first and last names as variables
ask the user for their first name and store it
ask the user for their last name and store it
compare the names using a compound condition. 
If Both names match, it says so
If exactly one name matches, it says so
if no names match, it says so
"""

#store your own first and last names as variables
devName1 = "brock"
devName2 = "griffith"

#ask the user for their first name and store it
userName1 = input("Type your first name and press enter ").lower #used .lower because string comparisons are case-sensitive
#ask the user for their last name and store it
userName2 = input("Type your last name and press enter ").lower

#compare the names using a compound condition.
if (devName1 == userName1) and (devName2 == userName2):
    print("we have the exact same name!")
elif (devName1 == userName1) or (devName2 == userName2):
    print("We have a name in common!")
else:
    print("get a better name...")

#what does not work is if devName1 and userName2 match, if logical conditions get to big, you can break it out of the 'if' statement.

"""
HW: 
book ch 3 three-yer-old simulator assignment
complete ch 3 reading quiz
complete ch 3 guess my number game
start reading ch 4
"""