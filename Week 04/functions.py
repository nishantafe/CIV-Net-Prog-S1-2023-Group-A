def greet():
    print("Hello")


def get_name_and_greet():
    name = input("Enter your name: ")
    print("Hello", name)


def verify_age():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You're an adult")
    else:
        print("You're a minor")


# Using a parameter and return
def is_successful(result):
    if result >= 50:
        return True
    else:
        return False


def assess_result():
    my_result = int(input("Enter your result: "))
    if is_successful(my_result):
        print("You have been successful")
    else:
        print("Sorry you haven't been successful")


def multiplier(num1, num2):
    return num1 * num2


def convert_usd_to_aud(amount):
    conversion_rate = 0.63  # Local variable to the function only
    return round(amount * conversion_rate, 2)


my_amount = 10  # Global variable, can be used anywhere even in functions

print("USD", convert_usd_to_aud(my_amount))
# print(conversion_rate) # This will return a NameError because it's a local variable

# greet()
# get_name_and_greet()
# verify_age()
# print(is_successful(10))
# assess_result()
# print(multiplier(1,2))
