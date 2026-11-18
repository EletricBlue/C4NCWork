"""
                            Brock Griffith
                                C4NC
                Python Ch 6: Functions Pt. 3: Scope
"""

"""
Scope is the word for areas in your program that are separate from other areas
every function has its own LOCAL SCOPE
the main program has GLOBAL SCOPE
there are ways to reach the global scope while working in the local scope
Ex:

main program

    function1()
    var1
    
    func2()
    var2
    
variable0
those variables in those functions are ENCAPSULATED in that function, it cannot be accessed by the main program

however, you can access a global variable directly from inside a function by making it a GLOBAL VARIABLE

BAD EXAMPLE:

    def damage():
    health = 10
    health -= 2
health = 10
print(health)
damage()
print(health)

this is called VARIABLE SHADOWING a variable. DO NOT DO IT.

Better Example:
def damage():
    global health
    health -= 2
health = 10
print(health)
damage()
print(health)

BE CAREFUL it's easy and useful, and can lead to bad habits and sloppy code

BEST Example:
def damage(life):
    life -= 2
    return life
health = 10
print(health)
health = damage(health)
print(health)
"""

### Programming Challenge: Shop Function: Global Variables ###

"""
### MY ATTEMPT ###
#player should start with money and marbles
cash = 100
marbles = 0

#write a shop() function for buying marbles
def shop(dollars, quantity):
    #use a global var to deduct money from within the function
    global cash
    cash = dollars
    #Marbles should cost 2 cents, stored in a var called cost
    cost = 0.2
    #function should ask how many marbles the player wants to buy, checks if affordable
    amount = int(input("how many marbles do you want to buy? "))
    if cash < cost * amount:
        return "You don't have enough money!"
    else:
        cash -= cost * amount
        quantity += amount
        print("You have", cash, quantity)
        return cash, quantity

print(shop(cash, marbles))

"""
"""
### ACTUAL SOLUTION ###
def shop():
    global money
    cost = 2
    print("Marbles cost",cost,"cents each. You have",money,"cents.")
    number = int(input("How many marbles would you like to buy? "))
    if number*cost > money:
        print("Sorry, you don't have enough.")
        return 0
    else:
        money = money - number*cost
        return number
money = 13
marbles = 0
marbles += shop()
"""

"""
Global Constants

we can store values that don't change as CONSTANTS

no special type or command in python for constants, but conventionally do some things:
    Use ALL CAPS: GRAVITY = 9.8
    Declare them all in one location: The Beginning of a program (or the first file in the project)
    USE CONSTANTS INSTEAD OF VALUES IN BODY OF A PROGRAM
        using numbers are called "magic numbers", because you don't know what they mean
    
"""