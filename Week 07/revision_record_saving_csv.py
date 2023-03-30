FILE = "sheet.csv"

enter_new_record = input("Would you like to enter a new record? [y/n]: ")
ask_again = True
while ask_again:
    if enter_new_record == "y":
        name = input("Enter a name to save: ")
        phone = input("Enter a phone number to save: ")
        file_out = open(FILE, "a")
        file_out.write(name + "," + phone + "\n")
        file_out.close()
        enter_new_record = input("Would you like to enter a new record? [y/n]: ")
    else:
        print("File saved. Goodbye!")
        ask_again = False

