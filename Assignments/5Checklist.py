"""
Brock Griffith
Assignment: Checklist
"""
#create task list
tasks = ["do laundry", "feed self", "write 5 pages of play", "read textbook"]
goodInput = False

#displays a list of tasks when program starts
print("Here's the To Do list for today: ")
print(tasks)
print("When you have completed a task, type it in below.")

while True:

    #asks user to type things in when completed
    userIn = input("What task have you done? ").lower()


    for x in tasks:
        #if input is in list, delete item
        #print("checking")
        if x == userIn:
            i = tasks.index(x)
            #print("popping:", x, "index:", i)
            tasks.pop(i)
            goodInput = True
            break

    if goodInput == False:
        print("I don't see", userIn, "on the list")

    #check if list is empty here
    if len(tasks) < 1:                      #the sign of distrust
        #if list is empty, say so and break
        print("You have completed ALL tasks, congrats!")
        break

    #then show remaining tasks
    print("Here's the To Do list for today: ")
    print(tasks)