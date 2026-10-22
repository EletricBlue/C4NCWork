import random

#declare user balance
userBalance = 500

#start game while loop
while True:
    #rollSum = random.randint(1, 6)
    print("You have", userBalance, "dollars")
        #get a bet from user
    userBet = int(input("What do you bet? "))
    #check if user bet too much money
    if userBet > userBalance:
        print("You can't bet more than you have!")
    else:
        #roll two six sided dice, random(1,6)
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        rollSum = roll1 + roll2
        print(roll1, roll2, rollSum)
            #compare sum to 7 or 11, user wins
        if rollSum == 7 or rollSum == 11:
            print("player wins")
            userBalance += userBet
            #if sum == 2, 3, or 12, user loses
        elif rollSum == 2 or rollSum == 3 or rollSum == 12:
            print("player loses")
            userBalance -= userBet
            #else save sum as point total
        else:
            points = rollSum
            print("you have", points, "points")
            #in loop roll 2 more dice
            while True:
                rollOff1 = random.randint(1, 6)
                rollOff2 = random.randint(1, 6)
                rollOffSum = rollOff1 + rollOff2
                print("rolloff total:",rollOffSum)
                #if sum == point total, win
                if rollOffSum == points:
                    print("player wins")
                    userBalance += userBet
                    break
                #if sum == 7, lose
                elif rollOffSum == 7:
                    print("player loses")
                    userBalance -= userBet
                    break

                #keep rolling dice until outcome

        #Check if the user is out of money
        if userBalance == 0:
            print("You have no more money!, that means you can't play...")
            break
        #ask user if they want to keep going or quit
        userIn = input("Would you like to stop? y/n ")
        if userIn == "y":
            #if quit then break
            print("you quit with", userBalance, "dollars")
            break
