import serial.tools.list_ports

class Comports:
     # Code to be executed when the class is called
    def __init__(self):
        # Code to be executed when the class is called
        # Takes the list of ports and the Arduino connected port
        ports_found = self.get_ports()
        connect_port = self.findArduino(ports_found)

        # Loops through ports and if Arduino is found it connects
        if connect_port != 'None':
            self.ser = serial.Serial(connect_port, baudrate=9600, timeout=1)
            print('Connected to ' + connect_port)
        else:
            print('Connection Failed!')

        print("Done")  #End of Class Notification
        
    
    # Gets a list of ports 
    def get_ports(self):
        ports = serial.tools.list_ports.comports()
        return ports
    
    # Loops through ports until Arduino is found and returns 
    def findArduino(self, ports_found):
        comm_port = 'None'
        num_connections = len(ports_found)

        for i in range(0, num_connections):
            port = ports_found[i]
            str_port = str(port)

            if 'Arduino' in str_port:
                split_port = str_port.split(' ')
                comm_port = split_port[0]

        return comm_port

# Instantiate the Comports class, which will run the code in __init__()


# Additional methods or attributes can still be accessed and called on comports_obj
