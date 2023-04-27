import ipaddress

my_ip = "10.56.17.22"


# 0.0.0.0
# 255.255.255.255
def validate_ip_address(my_ip_address):
    try:
        ipaddress.IPv4Address(my_ip_address)
        return True
    except ipaddress.AddressValueError:
        # print("Invalid IP address")
        return False


new_ip_address = input("Enter an IP address: ")
is_valid = validate_ip_address(new_ip_address)
if is_valid:
    print("The IP address you entered is valid")
else:
    print("That is not a valid IP address")
