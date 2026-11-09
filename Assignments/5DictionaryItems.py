"""
Brock Griffith
Assignment: Dictionary Items
"""

#variables

roomDesc = "You are in a plain room, in the center is a table with three items."
itemDict = {
            "Fruits":"A bowl of apples is on the table",
            "Sword":"A sword inside a scabbard lies on the table",
            "Potion":"A vial of blue and gold liquid that glitters in the light"
            }

#in a loop:
while True:

    #Program describes a room and lists the items in it

    print(roomDesc)
    print("On the table there are these items:")
    

    #Program asks what the user wants to inspect

    userIn = input("What item would you like to inspect?")

        #check if the input exists in the library before displaying

    #user can type end to quit program