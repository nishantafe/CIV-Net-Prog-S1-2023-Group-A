my_dictionary = {"John": "0412312314", "Sara": "0421321332", "Jonathan": "0402948472"}

# Get the keys of a dictionary
keys = my_dictionary.keys()
print("Keys:", keys)

# Get the values of a dictionary
values = my_dictionary.values()
print("Values:", values)

# Get the items (pairs) of a dictionary
items = my_dictionary.items()
print("Items:", items)

# Get the value of a specific key in the dictionary
the_one = my_dictionary["John"]
print(the_one)

# Add a new item (pair) to the dictionary
my_dictionary["Joe"] = "0438495584"
print(my_dictionary)

# Use a for loop with .items() to neatly display keys and values in a dictionary
for one_key, one_value in my_dictionary.items():
    print(one_key, one_value)

# Challenge: Get John's phone number
print("John's phone number is:", my_dictionary["John"])
