"""
                            Brock Griffith
                                C4NC
            Python Ch 4: The for loop, range(), and len() [length]
"""

import random

### WHEN SHOULD I USE A FOR LOOP AND A WHILE LOOP?

"""
while loops repeat some part of your program WHILE something is true, a CONDITION

for loops repeats a code, but not based on a CONDITION, it uses a SEQUENCE
repeats for each item in that sequence
"""

"""
format:
for COUNTING_VARIABLE in SEQUENCE:
    statement1
    statement2
    
example:
print("counting")
for i in range(10);
    print i, end=" ")
    
range() is a python function that returns a sequence of numbers STARTING AT ZERO
ex: range(10) gives a sequence of numbers from 0 to 9, 9 is the 10th item in that sequence
"""
"""
### PROGRAMMING CHALLENGE: for loop ###

#count from 1 to 100
for i in range(100):
    #display each number that is divisible by either 3 OR 5 (or BOTH)
    #print(i, end=" ")
    if (i % 3==0) or (i % 5==0) or (i % 3==0 and i % 5==0): ## "(i % 3==0 and i % 5==0)" is unnecessary, but I'm keeping it anyway
        print(i, end=" ")
    #Don't display anything else
"""

"MORE ABOUT RANGE()"
"""
range(positive integer) generates a sequence from 0
range(starting point, ending point, stepsize)
meaning range() can count by 2's, 8's, 3's, etc.
starting point is INCLUSIVE, ending point is NON-INCLUSIVE
range(5, 1, -1) counts backwards to 2
"""

"""
### PROGRAMMING CHALLENGE: for loop revisited ###

# count from 1 to 100
for i in range(1, 101, 1): #includes step size, but technically 1 is assumed if left blank
    # display each number that is divisible by either 3 OR 5 (or BOTH)
    # print(i, end=" ")
    if (i % 3 == 0) or (i % 5 == 0) or (
            i % 3 == 0 and i % 5 == 0):  ## "(i % 3==0 and i % 5==0)" is unnecessary, but I'm keeping it anyway
        print(i, end=" ")
    # Don't display anything else
"""

"""
WHILE VS FOR LOOPS
    use either or depending on the example, yeah that is basically what he said :(
    you can use strings instead of range:
    for i in "squid":
        this will iterate based on the length of "squid"
        
THE IN OPERATOR
    in checks to see if an element is a member of the sequence
        "is this data IN this box?"
    if yes, true, if not, false
    
    if "v" in word:
        print("there is a v in " + word)
        
THE LEN() FUNCTION
    len() returns the length of a sequence
    number = len("howdy")
    print(number)
    #this will print 5
"""

### PROGRAMMING CHALLENGE: Sequence using len() ###
"""
#ask the user to enter a message
message = input("Type a message and press enter: ")
#tell the user the number of characters in their message
print("your message is " + str(len(message)) + " characters long")
print("the length of your message is:", len(message))
"""
### PROGRAMMING CHALLENGE PART 2: ###

#ask the user to enter a message
message = input("Type a message and press enter: ").lower()
#tell the user the number of characters in their message
print("your message is", len(message), "characters long") #Refined length statement
#if the letter e appears in the message, it should say so
if "e" in message:
    print("The most common letter in the English language, 'e', is in your message")
#otherwise not
else:
    print("The most common letter in the English language, 'e', is NOT in your message")

#what about "E", it won't catch it, so added .lower() to input
