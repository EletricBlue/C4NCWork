"""
                            Brock Griffith
                                C4NC
                      Python Ch 5: Nesting Sequences
"""

nested = ("1", ("2","3"),["4", "5", "6"])

"""
this is a tuple containing 1, a tuple containing 2, 3, and a list containing 4 5 6
"""

###Example###
highScores = [("HH", 1500), ("RDB",1345), ("JMJ", 1233)]
#you can index this list like normal

"""
To index inside this list, you can:
secondElement = highScores[1]
print(secondElement(0)
"""

""" But really you want to do this: print(highScores[1] [0]) """

### PROGRAMMING CHALLENGE: Nested Scores
"""
# Have a list of high scores, string and number

#ask the user the high score they want to see, convert
userIn = int(input("Which high score do you want to see? ")) - 1

#display the initials and score

print(highScores[userIn] [0], highScores[userIn] [1])
"""

"""
UNPACKING:
initials, score = ("HH",1500)
print(initials)
print(score)
"""

### PROGRAMMING CHALLENGE: Nested Scores and Unpacking

#put the previous program in a loop
while True:
    # ask the user the high score they want to see, convert
    userIn = int(input("Which high score do you want to see? "))

    #if the user enters anything other than a 1, 2, or 3 the program exits
    if 0 < userIn < 4: #this should be userIn < len(highScores) but it's fine for now
        break
    # display the initials and score
    else:
        #Unpack initials and score and display
        print(highScores[userIn - 1][0], "-", highScores[userIn - 1][1])


""" 
for entry in highScores:
    initials, score = entry
    print(initials, "-", score)
"""

"""
highScores=[("HH",1500),("RDB",1345),("JMJ", 1233)]
for entry in highScores:
initials, score = entry
print(initials, "-", score)
"""

"""
highScores=[("HH",1500),("RDB",1345),("JMJ", 1233)]
choice = input("Whose score do you want to see? ")
for entry in highScores:
initials, score = entry
if initials == choice:
print(initials, "-", score)
"""
