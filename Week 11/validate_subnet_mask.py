import ipaddress


def validate_subnet_mask(an_ip_address, a_subnet_mask):
    """Validate the subnet mask"""
    ip_range = an_ip_address + "/" + a_subnet_mask  # Example "192.168.0.0/255.255.255.0"
    try:
        ipaddress.IPv4Network(ip_range)
        return True
    except ValueError:
        print("Invalid subnet mask")
        return False


subnet_prefix = "10.56.17"  # make sure to validate the ipaddress (see Week 08)

valid_subnet_mask = False
while not valid_subnet_mask:
    subnet_mask = "255.255.255.0"
    # subnet_mask = input("Enter a subnet mask (Eg. 255.255.255.0): ")
    sample_ip = subnet_prefix + ".0"
    valid_subnet_mask = validate_subnet_mask(sample_ip, subnet_mask)

# validate_subnet_mask("10.56.17.0", "255.255.255.192")
