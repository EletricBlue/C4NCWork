"""
Brock Griffith
Assignment: Fantastic Landscape
"""
import random

#create a tuple of place descriptions
places = ("You stand within the Grand Canyon, its walls towering above you on each side. A magical portal opens before you, do you walk through it?",
          "You stand among the trees of the Californian Redwood Forrest, their branches high above you sway in the wind. A portal opens before you, walk through it?",
          "You stand before Old Faithful in Yellowstone National Park, just as the geyser erupts, shooting hot steam into the air. The mist opens a portal, walk through?",
          "You emerge looking across Niagara Falls, as it dumps hundreds of thousands of gallons downstream. A portal opens behind you, care to walk through it?")
#Create a tuple of commands, walk and end
actions = ("walk", "end")

print("Welcome to Fantastic Landscape")
print("what would you like to do?")

#Code should loop until walk or end are entered
while True:
    choice = random.randrange(len(places))
    userIn = input("Type Here: ").lower()
    #if user inputs walk
    if userIn == actions[0]:
        #print a randomly selected description from the tuple
        print(places[choice])
    #if user inputs end, program ends
    elif userIn == actions[1]:
        break
    #if user inputs an unknown command, program complains and prints the valid commands
    else:
        print("I'm sorry, I do not know that command, valid commands are:", actions)
