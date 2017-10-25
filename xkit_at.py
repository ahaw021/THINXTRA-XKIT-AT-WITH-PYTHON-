import serial
import argparse


from serial_ports_explorer import *
from WISOL_conversations import *


BAUD = 9600
COM_PORT = 'COM9'
MESSAGE = b'AAFF0011'


# setup a comms object that will do the talking to the Module
#summary of commands can be found here: https://pyserial.readthedocs.io/

comms = serial.Serial(COM_PORT,BAUD,timeout=5)

configure_macrochannel(comms)
message = b'009911118822AABBCCDDEEFF'
send_message(comms,message)
