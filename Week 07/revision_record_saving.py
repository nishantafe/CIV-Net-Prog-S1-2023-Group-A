FILE = "phonebook.txt"
name = input("Enter a name to save: ")
phone = input("Enter a phone number to save: ")
file_out = open(FILE, "a")
file_out.write(name + " " + phone + "\n")
file_out.close()
