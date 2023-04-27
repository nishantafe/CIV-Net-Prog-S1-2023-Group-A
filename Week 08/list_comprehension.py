cars = ["Mercedes", "Volvo", "Ferrari", "Mazda"]
cars.append("Toyota")
print("Cars:", cars)
favourite_cars = []

for car in cars:
    if "r" in car:
        favourite_cars.append(car)
print("Favourite cars:", favourite_cars)

# List comprehension
# list = [APPENDING ZONE   LOOPING ZONE]
# list = [APPENDING ZONE   IF WITH ELSE ZONE    LOOPING ZONE]
# list = [APPENDING ZONE   LOOPING ZONE    IF WITHOUT ELSE ZONE]
best_cars = [car if "r" in car else "Bad Car" for car in cars]
print("Best cars:", best_cars)

grades = [22, 44, 66, 34, 12, 99]
# Condition to pass: grade should be greater or equals 50
# TODO: create a list of results "Pass" or "Fail" based on the grades list

# list = [APPENDING ZONE   IF WITH ELSE ZONE    LOOPING ZONE]
results = ["Pass" if grade >= 50 else "Fail" for grade in grades]
print("Results:", results)

# Get every player to play against all players in the other list
players_1 = ["John", "Sam", "David"]
players_2 = ["Rita", "Sara", "Lisa"]
for person in players_1:
    for another_person in players_2:
        print(person, "VS", another_person)

# All IPs against all ports
ips = ["192.168.0.1", "192.168.0.2", "192.168.0.3"]  # You can use range() to generate this
ports = ["80", "443", "110"]
for ip in ips:
    for port in ports:
        # scan(ip, port)
        print(ip, ":", port)
