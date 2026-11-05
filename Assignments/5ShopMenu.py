"""
Brock Griffith
Assignment: Shop Menu
"""

#put three items in a shop LIST, with prices
goodOutCheck = True
items = [("apple", 2), ("magic pendant", 50), ("shiny dagger", 45)]
while True:

    #Display list neatly (unpack it)
    print("Here's what I have: ")
    for i in items:
        print(i[0].title(), "for $" + str(i[1]))
    #ask what the user what to buy
    userIn = input("what do you want? ").lower()

    #check if item is in list
    for x in items:
        #if in list,
        if userIn == x[0]:
            #display ITEM with PRICE
            print("Here's your", x[0].title() + ". That will be $" + str(x[1]))
            goodOutCheck = True
            break
        else:
            goodOutCheck = False
#if not in list,
    if goodOutCheck == False:
        #program complains
        print("\nI don't have that! Get lost.\n")
        break
