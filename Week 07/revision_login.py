FILE = "phonebook.txt"
phonebook_dictionary = {}


def read_file_into_dictionary(file_name, dictionary_name):
    phonebook_file_in = open(file_name, "r")
    for line in phonebook_file_in:
        name, phone = line.split(" ")
        dictionary_name[name] = phone.rstrip()


read_file_into_dictionary(FILE, phonebook_dictionary)

entered_name = input("Enter your username: ")
entered_phone = input("Enter your password: ")
if entered_name in phonebook_dictionary and entered_phone == phonebook_dictionary[entered_name]:
    print("Valid record.")
else:
    print("Invalid record.")
