"""
                            Brock Griffith
                                C4NC
                    Python Ch 6: FUNCTIONS WOOOOO
"""


#17TH: PROJECT SKELETON

#Dec 3rd is extra credit

### PROGRAMMING CHALLENGE: Functions 4 ###
#Random Function - calculate a random num 1 - 100 and return
def randomizer():
    num = random.randrange(0, 101)
    return num

### PROGRAMMING CHALLENGE: Functions 3 ###
def confused(str1):
    print("I don't understand what", str1, "means.")

### PROGRAMMING CHALLENGE: Functions 2 ###

#this is what single-line comments are for
#you briefly describe the function just above it
#outputs command options
def helper():
    print("You can type: random, help, or end.")



"""
ABSTRACTION - functions let you think 

ENCAPSULATION - functions are protected from outside code
"""
import random
### PROGRAMMING CHALLENGE: Functions 1 ####

#start loop
while True:
    #ask for input
    userIn = input("What would you like to do? ").lower()
    #check input
    if userIn == "random":
        #generate number
        print(randomizer())
        #end program
    elif userIn == "end":
        break
        #help
    elif userIn == "help":
        helper()
        #complain
    else:
        confused(userIn)

### end challenge

"""
print and input are functions!
random.random commands are functions
ABSTRACTION: ex: randint(1,6)
    we don't need to know the EXACT lines of code to know how this function works
    that is ABSTRACTION

FUNCTION FORMAT:

def functionName(parameters):
    functionCode...

DO NOT USE PRE-EXISTING NAMES

user-defined functions should be placed at the top of the file
"""

"""
SO: WHY
if that function did many many things, that's a big time saver!
    we would have to write code over and over, and you WILL make mistakes if you do that
    you would have to change ALL of the repeated code if you wanted to change it

if you find yourself writing code over and over: make it a function!

PASSING AND RETURNING PARAMETERS
how to do it:

def funcName(parameters, parameters):
    bla bla

EX:

def multiply(num1):
    answer = num1*7
    print(answer)
    
response = float(input("blah blah")
multiply(response)

ENCAPSULATION: you CANNOT user num1 as a variable outside of that function
    (*unless its a global variable but don't do that)
    
"""

"""
GETTING INFO BACK/OUT

when a function gives you data back that is called a RETURN VALUE

format:
return answer

assign that return value to a variable or else it slips into the ether
"""

