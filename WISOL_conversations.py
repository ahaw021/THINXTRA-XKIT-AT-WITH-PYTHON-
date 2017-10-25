from WISOL_AT_DICTIONARY import *
import time

# helper function - print the result of sending a serial commands
# note: we sleep for 1 second so the buffer can be filled up
# note: no parsing of results currently

def readSerialResult(comms):
    time.sleep(1)
    response_length = comms.in_waiting

    response = comms.read(response_length)
    print("--Response--")
    print("The response is " + str(response_length) + " bytes")
    print(response.decode())
    print("---")

def test_at_command(comms):
# run an AT command to test module is responding
#then get device ID
    print("Testing AT Comms by sending AT Command")
    comms.write(TEST_COMMAND)
    readSerialResult(comms)


def device_id(comms):
    print("Get Device ID")
    comms.write(DEVICE_ID)
    readSerialResult(comms)

def check_macrochanel(comms):
# check if AT$RC needs to be called page 6 of WISOL Manual
# link: https://github.com/Thinxtra/Xkit-Sample/blob/master/Document/Wisol_Comands_and_Schematics/WISOL_WSSFM10R_AT%20command_SFM10R_Rev.00_1.pdf
# note: this is how the flow should work - run command below if x or y are below 0 or 6 then call AT$RC command
    print("Check if AT$RC Needs to be Called --- NOTE: We call this anyway but good practise it to check")
    comms.write(CHECK_MACROCHANNEL)
    readSerialResult(comms)

def configure_macrochannel(comms):
    print("Call the AT$RC AT Command")
    comms.write(CONFIGURE_MACROCHANNEL)
    readSerialResult(comms)

def send_message(comms,message):
    #send message and wait 5 seconds for message to be sent before reading result
    print("Send the Message")
    comms.write(SEND_MESSAGE+message+CARRIDGE_RETURN)
    time.sleep(5)
    readSerialResult(comms)
