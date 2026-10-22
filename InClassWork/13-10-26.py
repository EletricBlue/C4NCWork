"""
                            Brock Griffith
                                C4NC
            Python Ch 4: Strings, immutability, Slicing, tuples
"""

### Indexing Strings
"""
    you can use in to find a character anywhere in a string
    you can also step through a string one character at a time, sequential access
    You can also directly access what you want, called random access
    
    ex:
    word = index
    print("The word is:', word, "/n" 
    high = len(word)
    for i in range (high):
        print("word[", i, "]", word[i]
    """
"""
### PROGRAMMING CHALLENGE: Sequence using len() ###
#asks the user to input a word
userWord = input("type a word and press enter: ")
length = len(userWord)
#asks the user which character of the word to display by order
#subtract 1 to whatever the input is
userCount = int(input("enter a number: "))-1

#if the user enters a number out of range, it should say so
if (userCount > length):
    print("outside of letter range")
else:
    #shows the correct character
    print(userWord[userCount])
"""

# STRINGS ARE IMMUTABLE
# they cannot be changed
# some sequences can be changed, they are mutable
# you cannot do this:
"""
    fruit = "Pineapple"
    fruit[0] = "w"
    print(fruit)
"""
# but you CAN slice, similar to indexing:
"""
    word = "pizza"
    print(word[0:5]) #pizza
    print(word[1:3]) #iz
"""
# you can then use that slice, "iz" in a new string:
"""
    word = "pineapple"
    temp = word[1:] {assumes the end!}
    newString = "W" + temp
"""
#if the slice is impossible, it will return an empty sequence (string)

### TUPLES ###
# our first of three big data types
"""
tuple_name = (item1, item2, item3)
"""
# they can include any data type, including tuples, but also strings, ints, floats, etc.
# sometimes its helpful to write tuples like this:
"""
inventory = ("sword",
            "Helmet",
            "potion")
"""

#tuples do not care what data type you put into them

### PROGRAMMING CHALLENGE: Tuples

#the program should run in a loop
#make a tuple with three items, and call it inventory
#the program should display your inventory
#it should ask if you'd like to look at something in the inventory
#if you type the name of something in you inventory, it should print a descr. of it
#if you type something that isn't there, it should complain
#when the user types "end", the program should terminate

#declare inventory
inventory = ("Sword", "Shield", "Merch")
#declare description
description = ("This is a sword", "this is a shield")
while True:
    #print tuple
    print(inventory)
    #ask for input, or end
    userItem = input("What item do you want to inspect? or type end: ")
    if userItem == "end":
        break
    elif userItem not in inventory:
        print("I don't see any", userItem, "here.")
    elif userItem == inventory[0]:
        print("It's wickedly sharp.")
    elif userItem == inventory[1]:
        print("It smells like feet.")
    else:
        print("It has a picture of Spongebob on it.")
    print("See you later, adventurer.")

### USE TUPLES FOR USER INPUT, USE THIS FOR YOUR PROJECT:
"""
combatCommands = ("fight", "run", "heal")
command = input("What would you like to do? ")
while command not in combatCommands:
print("Valid commands are:",combatCommands)
command = input("What would you like to do? ")
print("You", command)
"""

### there are many ways to do user controls, this is one version