import serial
import time

#play arround with listing ports at a later stage
# docs for listing ports: https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.list_ports

BAUD = 9600
COM_PORT = 'COM3'
MESSAGE = b'001100AAEE'

#AT Commands Dictionary

CARRIDGE_RETURN = b'\r'
TEST_COMMAND = b'AT'+ CARRIDGE_RETURN
CHECK_MICROCHANNEL = b'AT$GI?' + CARRIDGE_RETURN
CONFIGURE_MICROCHANNEL = b'AT$RC' + CARRIDGE_RETURN
DEVICE_ID = b'AT$I=10' + CARRIDGE_RETURN
SEND_MESSAGE = b'AT$SF='

# setup a comms object that will do the talking to the Module
#summary of commands can be found here: https://pyserial.readthedocs.io/

comms = serial.Serial(COM_PORT,BAUD,timeout=5)

# helper function - print the result of sending a serial commands
# note: we sleep for 1 second so the buffer can be filled up
# note: no parsing of results currently

def readSerialResult():
    time.sleep(1)
    response_length = comms.in_waiting
    print("The response is " + str(response_length) + " bytes")
    response = comms.read(response_length)
    print("--Response--")
    print(response)
    print("---")

# run an AT command to test module is responding
#then get device ID

print("Testing AT Comms by sending AT Command")
comms.write(TEST_COMMAND)
readSerialResult()

print("Get Device ID")
comms.write(DEVICE_ID)
readSerialResult()

# check if AT$RC needs to be called page 6 of WISOL Manual
# link: https://github.com/Thinxtra/Xkit-Sample/blob/master/Document/Wisol_Comands_and_Schematics/WISOL_WSSFM10R_AT%20command_SFM10R_Rev.00_1.pdf
# note: this is how the flow should work - run command below if x or y are below 0 or 6 then call AT$RC command

print()
print("Check if AT$RC Needs to be Called --- NOTE: We call this anyway but good practise it to check")
comms.write(CHECK_MICROCHANNEL)
readSerialResult()

print()
print("Call the AT$RC AT Command")
comms.write(CONFIGURE_MICROCHANNEL)
readSerialResult()

#send message and wait 5 seconds for message to be sent before reading result

print()
print("Send the Message")
comms.write(SEND_MESSAGE+MESSAGE+CARRIDGE_RETURN)
time.sleep(5)
readSerialResult()
