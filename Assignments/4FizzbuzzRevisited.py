"""
Brock Griffith
Assignment: fizzbuzz Revisited
"""

#create number variable / sentry variable
num = 1
#start while loop to run 100 times
while num <= 100:
    #if number divides by 15
    if num % 15 == 0:
        #fizz
        print("fizzbuzz")
    #if number divides by 5
    elif num % 5 == 0:
        #buzz
        print("buzz")
    #if number divides by 3
    elif num % 3 == 0:
        #fizzbuzz
        print("fizz")
    else:
        print(num)

    #increment number variable
    num += 1