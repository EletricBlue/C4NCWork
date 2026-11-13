"""
                            Brock Griffith
                                C4NC
                Python Ch 6: Functions Pt. 2: More Parameters
"""

"""
Multiple Parameters:

send the right type of data
send them in the right order
name parameters helpfully AND differently to what you're using in the rest of your file

def sums(num1, num2, num3):
    answer = (num1+num2+num3)
    return(answer)

print(sums(firstNum, secondNum, thirdNum))"""

### PROGRAMMING CHALLENGE: More Functions 1 ###
"""
def addOrMult(str1, str2, decider): #takes two numbers and adds or multiplies depending on the string
    if decider.lower() == "multiply":
        return str1 * str2
    elif decider.lower() == "add":
        return str1 + str2
    else:
        return "ERROR: bad string!"


print(addOrMult(5, 5, "multiply"))
"""

"""
optional parameters; or how to give default values

def greeting(message = "Hello.":
    print("you say, \'" + message + "\' to him.")
    
if you have an optional parameter, the following parameters MUST be optional, too
"""

### PROGRAMMING CHALLENGE: More Functions 2 ###
"""
def greeting(name, years = "who knows how many"):
    print("Hello", name + ", you are", years, "years old today!")

greeting("Brian", "41")

greeting("Brian")
"""

"""
You can return multiple values by doing: return "abc", 100, [0, 1, 2]
the order must match to the number of variables you are creating!
"""

"""
Code Reuse: if you write the exact same code MORE THAN ONCE, make a function
"""