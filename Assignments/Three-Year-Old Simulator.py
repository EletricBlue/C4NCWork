"""
                        Brock Griffith
            Assignment: Three-year-old Simulator
"""

#get initial response
userIn = input("Why is the sky blue? ").lower()

#loop immediately ends if user types "because!", else begins to run
while userIn != "because!":
    userIn = input("Why? ").lower()
    #runs forever until user enters "because!"

print("Oh ok.")