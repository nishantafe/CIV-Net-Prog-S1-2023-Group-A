import string
import random

letters = string.ascii_letters  # Alphabet letters (upper & lower case)
digits = string.digits  # All numbers from 0-9
symbols = string.punctuation  # All the special characters/symbols

secret_word = ""
character_combo = letters
use_digits = input("Would you like to include digits? [y/n]: ").lower()
if use_digits == "y":
    character_combo += digits

secret_word_length = input("Enter the length (press enter for 10): ")
if secret_word_length == "":
    secret_word_length = 10
else:
    secret_word_length = int(secret_word_length)

for character in range(secret_word_length):
    secret_word += random.choice(character_combo)
print(secret_word)
