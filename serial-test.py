import serial

port_number = "/dev/ttyUSB0"
port = serial.Serial(port_number, 38400)
print("Serial Port : {0}".format(port))

for i in range(0, 100):
    port.write("iSM\n")
    message = ""

    while True:
        tmpMsg = port.read()
        if tmpMsg == "\n": break
        else: message = message + tmpMsg
    print("{0} ==> Get Message : {1}".format(i, message))

port.close()
