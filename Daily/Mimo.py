# 2/15/2023
# ---Mimo---

"""
Testing new system. 
Go through each section: Mimo, Sololearn, FreeCodeCamp as usual.
    a) Write out things that are new or unclear.
    b) Note material that is useful and store it.
    c) Use ChatGPT and practice recall (Read and write from memory)
    d) Make my own spin
"""

"""
Let's code a program to check if we have enough characters for a password. Here's a peek at
the final code.
"""
password_length = 8
input_password = 6

if input_password < password_length:
    print("Not enough characters")
else:
    print("Perfect password length!")


def is_new_record(current, new_value):
    return new_value > current

result = is_new_record(120, 154)
print(result)

"""
Test Corrections
"""

scores = [50, 70, 40]
for score in scores:
    bonus_points = 5
    print(f"new score: {score + bonus_points}")

"""
Let's use our knowledge of returning values to write a function that converts a set of
numbers to morse code.

We'll replace each number of the passed code parameter with its morse correspondent and
return the result.
"""

def convert_to_morse(code):
    code = code.replace("1", ".----")
    code = code.replace("2", "..---")
    code = code.replace("3", "...--")
    code = code.replace("4", "....-")
    code = code.replace("5", ".....")
    code = code.replace("6", "-....")
    code = code.replace("7", "--...")
    code = code.replace("8", "---..")
    code = code.replace("9", "----.")
    code = code.replace("0", "-----")
    return code
lock_code = "1 2 2 5 0"
print(f"Initial code: {lock_code}")

morse = convert_to_morse(lock_code)
print(f"Morse code: {morse}")

"""
Fare Split Calculator

Let's use our knowledge of using multiple parameters to create a function that splits a 
Doober fare between several users.

We'll divide the price by the number of passengers first. Then, we'll add a small feature
cost to each passenger's share.
"""

def split_fare(fare, passengers, feature_cost):
    share = fare/passengers
    print(f"Splitting the ${fare} fare between {passengers} passengers...")

    shared_cost = share + feature_cost
    print(f"Adding a ${feature_cost} feature cost...")
    return shared_cost

fare_cost = 36
passengers = 3
feature_cost = 0.5

shared_cost = split_fare(fare_cost, passengers, feature_cost)
print(f"Each pays: ${shared_cost}")

# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------
