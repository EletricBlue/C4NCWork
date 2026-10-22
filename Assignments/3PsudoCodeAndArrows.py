"""
                            Brock Griffith
                                C4NC
                    Assignment: Pseudocode and Arrows
"""
import random
#Pick a random number between 1 and 10 for the cost of the arrow
arrowPrice = random.randint(1,10)

#Tells the user the price of the arrow
print("Arrow price is", "$" + str(arrowPrice))

#Asks the user how much money they have in dollars
userCash = int(input("How much money do you have? "))

#Checks if the user can afford any whole arrows
if arrowPrice > userCash:
    print("you do not have enough money to buy any arrows")
else:
    print("you can buy ", str(userCash // arrowPrice), "arrows with", str(userCash % arrowPrice), "left over.")
#program responds
