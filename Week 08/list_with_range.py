for number in range(11, 50, 2):  # Start=0 | End | Steps=1
    # print(number)
    pass
# 255.255.255.255
# 0.0.0.0


# 10.56.17.11:80
# 10.56.17.12:80
# 10.56.17.13:80
# 10.56.17.14:80
""" Generate a list of all valid ip addresses that are formed of the
    subnet prefix and subsequent numbers skipping the first 10 and the even numbers.
    For example  10.56.17.11, 10.56.17.12, 10.56.17.13...
"""
# subnet_prefix = "10.56.17"
subnet_prefix = input("Enter a subnet prefix: ")
ips_list = [subnet_prefix + "." + str(num) for num in range(11, 50, 2)]
print(ips_list)

