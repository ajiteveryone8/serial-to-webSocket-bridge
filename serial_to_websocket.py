import serial
import time


serialPort = serial.Serial(
    port="COM7", baudrate=230400, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)

serialPort.write(b"d")




serialString = ""  # Used to hold data coming over UART
while 1:
    # Read data out of the buffer until a carraige return / new line is found
    serialString = serialPort.readline()

    # Print the contents of the serial data
    try:
        print(serialString.decode("Ascii"))
    except:
        pass