"""
LBYL
Look before you leap

EAFP
Easier to ask for forgiveness than permission
"""
try:
    print(name)
except NameError:
    print("Sorry, the variable 'name' does not have a value yet.")

try:
    number = input("Enter a number: ")
    number = int(number)  # can cause a ValueError if the user enters a letter.

    print("You entered", number)
except ValueError:
    print("Invalid number.")
