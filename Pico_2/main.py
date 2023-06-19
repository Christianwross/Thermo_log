
import time
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from connect import Comports


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




def animate(i, dataList, ser):
    ser.write(b'g')                                     # Transmit the char 'g' to receive the Arduino data point
    arduinoData_string = ser.readline().decode('ascii') # Decode receive Arduino data as a formatted string
    #print(i)                                           # 'i' is a incrementing variable based upon frames = x argument

    try:
        arduinoData_float = float(arduinoData_string)   # Convert to float
        dataList.append(arduinoData_float)              # Add to the list holding the fixed number of points to animate

    except:                                             # Pass if data point is bad                               
        pass

    #dataList = dataList[-50:]                           # Fix the list size so that the animation plot 'window' is x number of points
    
    ax.clear()                                          # Clear last data frame
    ax.plot(dataList)                                   # Plot new data frame
    
    #ax.set_ylim([0, 1200])                              # Set Y axis limit of plot
    ax.set_title("Thermocouple Temperature")                        # Set title of figure
    ax.set_ylabel("Temperature (C)")                              # Set title of y axis 

comports_obj = Comports()
class_variables = vars(comports_obj)
ser = comports_obj.ser

dataList = []                                           # Create empty list variable for later use
                                                        
fig = plt.figure()                                      # Create Matplotlib plots fig is the 'higher level' plot window
ax = fig.add_subplot(111)                               # Add subplot to main fig window


                                                        # Matplotlib Animation Fuction that takes takes care of real time plot.
                                                        # Note that 'fargs' parameter is where we pass in our dataList and Serial object. 
ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(dataList, ser), interval=100) 

plt.show()                                              # Keep Matplotlib plot persistent on screen until it is closed
ser.close()                                             # Close Serial connection when plot is closed
