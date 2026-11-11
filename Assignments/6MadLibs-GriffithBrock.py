"""
Brock Griffith
Assignment: Mad Libs
"""
import random
import time


#These three functions should have a list of the appropriate word type

#when the function is called, they randomly select a word from that list and return it

#Create noun() function
def noun(): #picks a random noun from a list
    nounlist = ["apples", "berries", "sandwich", "ham", "turkey", "beef", "Pepper Jack cheese", "American cheese",
                "Cheddar cheese", "bananas", "pineapple slices", "bacon", "chicken", "ribs", "avocado", "peppers"]
    select = nounlist[random.randrange(0, len(nounlist))]
    return select

#Create adjective() function
def adjective(): #picks a random adjective from a list
    adjlist = ["hot", "cold", "rusty", "dusty", "musty", "sandy", "foot-long", "six-inch", "twelve-foot", "rocky","wet",
               "soggy", "pressed-flat"]
    select = adjlist[random.randrange(0, len(adjlist))]
    return select

#create verb() function
def verb(): #picks a random verb from a list
    verblist = ["toast", "roast", "burn", "broil", "smoke", "grill", "chill", "blend", "torch", "scorch", "flambé",
                "sauté"]
    select = verblist[random.randrange(0, len(verblist))]
    return select

"""
print(noun()) 
print(adjective())
print(verb())
debug / testing
"""

#create a story that references the above functions multiple times
print("Hey I'm going to get lunch from Subway, do you want anything?")
time.sleep(3) #these are unnecessary, but it does make the story easier to read
print("Yeah gimme a", adjective(), "sandwich with", noun() + ",", noun() + ",", noun() + ",", "aaand", noun() + ".",
      "Oh! and make sure they", verb(), "and", verb(), "it, thanks man!")
time.sleep(4)
print("...What?")
