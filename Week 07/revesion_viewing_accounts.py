FILE = "phonebook.txt"
phonebook_dictionary = {}


def read_file_into_dictionary(file_name, dictionary_name):
    phonebook_file_in = open(file_name, "r")
    for line in phonebook_file_in:
        name, phone = line.split(" ")
        dictionary_name[name] = phone.rstrip()


read_file_into_dictionary(FILE, phonebook_dictionary)

print(f"{'Name':10s} Phone\n{'':-<21s}")
for each_name, each_phone in phonebook_dictionary.items():
    print(f"{each_name:10s} {each_phone}")
