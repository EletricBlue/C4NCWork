"""
                            Brock Griffith
                                C4NC
            Python Ch 5: Shared References and DICTIONARIES
"""

### For final project: Logic Diagram due first

"""
SHARED REFERENCES
x = 6
this is not stored this way in storage/memory
"x" POINTS to a hexadecimal (base 16) code
meaning you can change the data and not the variable pointer (in theory)
TYPICALLY this is not a problem

However, observe:

player1_items = ["torch", "wineskin", "club"]
player2_items = player1_items
print("Player 1 has: ",player1_items)
print("Player 2 has: ",player2_items)
print("Player 1 trades a torch for a lantern.")
player1_items[0] = "lantern"
print("Player 1 now has: ",player1_items)
print("Player 2 now has: ",player2_items)
"""


"""
Instead, make a copy:
player1_items = ["torch", "wineskin", "club"]
player2_items = player1_items[:] #<- this makes a copy of the entire player1_items list
print("Player 1 has: ",player1_items)
print("Player 2 has: ",player2_items)
print("Player 1 trades a torch for a lantern.")
player1_items[0] = "lantern"
print("Player 1 now has: ",player1_items)
print("Player 2 now has: ",player2_items)
"""

"""
DICTIONARIES
dictionaries resembles lists and tuples, but are NOT SEQUENCES
they cannot be used in for loops
They use key-value pairs

declared like this:
item_dictionary = {"banana":"A yellow fruit", "apple":"It's crunchy", "kale":"It's crunchy"}

{"Key":"Value"}

a value is searched by its key, like looking up a definition; you look for the word first THEN the definition

keys are IMMUTABLE

getting values:
dictionaryName[keyValue]
item_dictionary = {"banana":"A yellow fruit",
"apple":"It's crunchy", "kale":"It's crunchy"}
print(item_dictionary["banana"])
"""

### PROGRAMMING CHALLENGE: Dictionary (SAVE FOR LATER)###

#make a dict. of three places you've been, the place names are the keys, short desc. are values
places = {"Grand Canyon":"It's a canyon.", "Redwood Forrest":"It's a forrest of really tall trees",
          "Glacier Natl. Park":"It's a park with a glacier in it"}
#prompt the user to ask about on of three places, give the place names in the prompt
userIn = input("What place do you want to know about: Grand Canyon, Redwood Forrest, or Glacier Natl. Park? ")
#collect the input from user, ignore errors

#print the value

print(places[userIn])
#This code is prone to errors

"""
TESTING FOR A KEY
you can check by using an if/else statement with an in operator:
item_dictionary = {"banana":"A yellow fruit",
"apple":"It's crunchy", "kale":"It's crunchy"}
check = input("What do you want to know about? ")
if check in item_dictionary:
print(item_dictionary[check])
else:
print("I can't help you with that.")

this^ isn't the BEST way to do this, but this is:

dictionary_name.get(key, default)

.keys() returns all keys
.values() returns all values
.items() returns all keys AND values

JUST USE .GET() !
"""

### PROGRAMMING CHALLENGE: Dictionary 2
places = {"Grand Canyon":"It's a canyon.", "Redwood Forrest":"It's a forrest of really tall trees",
          "Glacier Natl. Park":"It's a park with a glacier in it"}
#start loop
while True:
    #show places user can enter with .keys()
    print("I know info about these places:", list(places.keys()))
    #check user entry with .get()
    userIn = input("What place do you want to know about? ")
    if userIn == "end":
        break
    print(places.get(userIn, "I don't know about that place"))
    print("enter another place or type 'end'")
    #make the loop endable by typing end

"""
MODIFYING THE DICTIONARY
keys are IMMUTABLE, but values are MUTABLE
dictionary_name[key] = value
IF THAT KEY DOES NOT EXIST: the key and value will be added

item_dictionary = {"banana":"A yellow fruit",
"apple":"It's crunchy", "kale":"It's crunchy"}
print(item_dictionary.items())
item_dictionary["kale"] = "It's healthy"
print(item_dictionary.items())

you can also DELETE entries with the del operator
del dictionary[key]
if key does not exist, it will give an error

item_dictionary = {"banana":"A yellow fruit",
"apple":"It's crunchy", "kale":"It's crunchy"}
print(item_dictionary.items())
if "banana" in item_dictionary:
del item_dictionary["banana"]
else:
print("Yes! We have no bananas")
print(item_dictionary.items())

you cannot guarantee that the order you make a dictionary will be the order python will stor it
"""