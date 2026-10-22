"""
                            Brock Griffith
                                C4NC
                        Python Ch 5: Lists
"""

"""
Lists are very similar to tuples
A list is another kind of sequence
it is MUTABLE
format: 
    list_name = [item1, item2, item3]

works with len() and the in operator
you can print lists like tuples, you should not do this (shows poor quality)
    it will print the [] or the ()
slicing works too, so list[1:3] works

you can concatenate lists: 
chest = [sheild, gems]
inventory = [sword]
inventory += chest
"""


### PROGRAMMING CHALLENGE: Concatenating Lists
"""
inventory = ["Sword", "Shield"]
chest = ["gem", "scroll"]
#show the user the contents of treasure chest (list)
print("You open the chest and there is a", chest[0], "and a", chest[1])
#show the user what they are carrying (inventory list)
print("This is your inventory:", inventory[0], inventory[1])
#asks if the user would like to get the items from the chest
userIn = input("Would you like to take the items from the chest? y/n ").lower()
#if user types y or yes, the treasure list is concat'd onto the inventory list
if userIn == "y" or userIn == "yes":
    inventory += chest
    #display full list after
    print("You have grabbed the items in the chest, this is your inventory now:", inventory[0], inventory[1], inventory[2], inventory[3]) #this method sucks but i don't really care rn; also its better than printing the list raw
else:
    print("You have decided not to take the chest.")
"""

"""
You can assign new elements by an index
but you can also slice
    when you slice, you HAVE to give it a list

you can delete elements of a list by using the "del" command 

more methods:
append() adds to end of list
sort() sorts elements smallest first
reverse()
count(value) returns number of times value occurs
index(value) returns first position where value occurs
insert(i, value) inserts value at position i
pop(i) returns value at position i and removes the value from the list
remove(value) removes the first occurrence of value from the list


method format: list.append(banana)
"""

###PROGRAMMING CHALLENGE: List Methods

#make two lists, ground and inventory
inv = ["sword", "shield"]
ground = ["potion", "orb"]
choice = ""
#The Program should display items on the ground and in inventory
print("Inventory: ", inv)
print("Ground: ", ground)
#ask if user wants to drop or pick up something
while choice != "end":
    userIn = input("would you like to \"pick up\" or \"drop?\" ").lower()
    if userIn == "pick up":
        var = user == input("what would you like to pick up? ")
#if pick up, append specified item to inventory
        if user in ground:

            print(inv)
        else:
            print("bad")
#if drop, append item to ground
#if item does not exist, complain


"""Why use tuples at all if list can do everything?
tuples are faster
tuples are immutable, so python will yell at you if you are trying to change it
sometimes tuples are needed
"""