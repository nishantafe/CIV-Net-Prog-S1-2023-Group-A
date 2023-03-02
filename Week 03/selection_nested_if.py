# result = 50
result = int(input("Enter your result: "))
if result >= 50:
    # the result is 50 or above
    if result == 50:
        print("Well done")
    else:
        print("Excellent work!")
else:
    # the result is 49 or lower
    print("Unfortunately you didn't pass", result, "isn't high enough")
