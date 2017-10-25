# THINXTRA-XKIT-AT-WITH-PYTHON-
A python example of using AT commands with Thinxtra

A write up of some of the engineering can be found here: https://www.linkedin.com/pulse/integrating-thinxtra-xkit-python-via-commands-andrei-hawke/

We utilise the PySerial library so we need to install this first. Documentation: https://pyserial.readthedocs.io

> pip install pyserial

### Constants to change:

COM_PORT: this will change from operating system to operating system
MESSAGE: make sure that it's a byte array

### Architecture

I have reworked the original codebase to break up functionality into a AT Dictionary (specific to Wisol) and conversations class (specific to Wisol)

Hopefully this will allow us to add other SigFox modules at a later date and create conversation objects for those modules

### Examples

##### Send MESSAGE

> comms = serial.Serial(COM_PORT,BAUD,timeout=5)
> configure_macrochannel(comms)
> message = b'0001100AAA'
> send_message(comms,message)


##### Get Device ID

> comms = serial.Serial(COM_PORT,BAUD,timeout=5)
> device_id(comms)

##### Check Macrochannel

> comms = serial.Serial(COM_PORT,BAUD,timeout=5)
> check_macrochanel(comms)
