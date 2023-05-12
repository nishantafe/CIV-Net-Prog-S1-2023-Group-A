import os

# Change or set the current working directory to the location of this file
os.chdir(os.path.dirname(__file__))


# TODO Create a function to read ports.txt into a list
# IF ports.txt exits
#     READ ports.txt
#     FOR a port in the file ports.txt
#         IF port is in the list (ports_list)
#             DISPLAY "Port already exits"
#         ELSE append the port into (ports_list)
#     CLOSE ports.txt
# ELSE DISPLAY "The file does not exit"

def read_ports_file_into_list(a_ports_file, a_ports_list):
    if os.path.isfile(a_ports_file):
        ports_file_in = open(a_ports_file, "r")
        for port in ports_file_in:
            if port in a_ports_list:
                print("This port already exists in the list")
            else:
                print(port.rstrip())
                a_ports_list.append(int(port.rstrip()))
        ports_file_in.close()
    else:
        print(f"The file {a_ports_file} does not exist")


PORTS_FILE = "../Parameters/ports.txt"
ports_list = []

read_ports_file_into_list(PORTS_FILE, ports_list)
print(ports_list)
