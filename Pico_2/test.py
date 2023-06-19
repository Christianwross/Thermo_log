import serial.tools.list_ports

def get_ports():
    ports = serial.tools.list_ports.comports()
    return ports

# Get the list of ports
ports_found = get_ports()

if len(ports_found) > 0:
    # Print the list of found ports
    print("Found Ports:")
    for port in ports_found:
        print(port)
else:
    print("No ports found. Please ensure the device is connected.")

