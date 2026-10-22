"""
                            Brock Griffith
                                C4NC
                       Assignment: Buying Potions
"""

#get user's name and capitalize it (title case)
username = input("What is your name? ")
username = username.title()
#Asks how many potions they would like to buy, and converts it properly.
potNum = int(input("How Many potions? "))
#This should be stored in a variable called cost.
#Shows a subtotal based on the price of potions costing $2.43 cents each.
cost = 2.43
subtotal = potNum * cost
print("$" + str(subtotal) + " this is the subtotal")
#Calculates an 8 percent tax rate (multiply by 1.08) using an augment assignment operator.
subtotal *= 1.08
#Responds in the following format:  Hello Jim, that will be $13.365 (fractional cents are ok for now)
print("Hello,", username, "that will be", "$" + str(subtotal))
#Comment your code and use descriptive variable names.
