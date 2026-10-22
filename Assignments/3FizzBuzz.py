"""
                            Brock Griffith
                                C4NC
                    Assignment: Intro to Fizzbuzz
"""

#ask the user for a number from 1 to 100
userNum = int(input("give me a number between 1 and 100 "))

#If the number is divisable by 15, print FizzBuzz
if userNum % 15 == 0:
    print("FizzBuzz")
#if the number is divisable by 5, print Buzz
elif userNum % 5 == 0:
    print("Buzz")
#if the number is divisable by 3, print Fizz
elif userNum % 3 == 0:
    print("Fizz")
#reprint the number if not divisable by 15, 5, or 3
else:
    print(userNum)
