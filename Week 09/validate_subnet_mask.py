import ipaddress

my_ip = "10.56.17.7"


def validate_subnet_mask(my_ip_address):
    try:
        ipaddress.IPv4Network(my_ip_address)
        return True
    except ValueError:
        print("Invalid Subnet Mask")
        return False


new_ip_address = input("Enter an IP address: ")
is_valid = validate_subnet_mask(new_ip_address)
if is_valid:
    print("The IP address you entered is valid")
else:
    print("That is not a valid IP address")





