import serial
import os

def print_ports():
    if os.name == 'nt':  # sys.platform == 'win32':
        from serial.tools.list_ports_windows import comports
    elif os.name == 'posix':
        from serial.tools.list_ports_posix import comports
    #~ elif os.name == 'java':
    else:
        raise ImportError("Sorry: no implementation for your platform ('{}') available".format(os.name))

    serial_ports = comports()

    for n, (port, desc, hwid) in enumerate(serial_ports, 1):
        print("PORT NAME: {} \t\t  DESCRIPTION: {} \t\t  HWID: {} ".format(port,desc,hwid))
