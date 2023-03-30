"""
Login [l]
Register [r]
    Generated password [y]
        Digits? [y/n]
        Symbols? [y/n]
        Length of the password (default = 10) [50]
    Custom password [n]
View Accounts [v]
Exit [e]
"""
MENU = "l) Login, r) Register"
print(MENU)
user_choice = input("Choose [l/r]: ")

if user_choice == "l":
    print("Login")
elif user_choice == "r":
    print("Register")
    generated_password_choice = input("Would you like a generated password? [y/n]: ")
    if generated_password_choice == "y":
        print("Generating a password")
    else:
        print("Enter your custom password")
else:
    print("Invalid choice.")
