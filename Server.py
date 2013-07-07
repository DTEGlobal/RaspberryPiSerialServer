__author__ = 'Cesar'
#-------------------------------------------------------------------------------
# Name:        Server
# Purpose:
#
# Author:      Cesar
#
# Created:     21/06/2013
# Copyright:   (c) Cesar 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# import serial
#
# port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=1.0)
# while True:
#     port.write("00S?1\r\n")
#     print(port.readline())
#     port.write("00MB\r\n")
#     print(port.readline())
#     port.write("00E\r\n")
#     print(port.readline())
#
#     print('test GitHub')

import threading

from socketserver import TCPServer
from TCPSerialServer import *


SerialServer = TCPServer(('localhost',3000),SerialClientHandler)
DiagnosticServer = TCPServer(('localhost',3001),DiagnosticHandler)
FindServer = TCPServer(('localhost',3002),FindHandler)

# Main Serial Server
def StartSerialServer ():
    print("Serial Server Running on: %s" % (SerialServer.server_address,))
    SerialServer.serve_forever()

# Returns the status of the serial server for diagnostic purposes
def StartDiagnosticServer ():
    print("Diagnostic Server Running on: %s" % (DiagnosticServer.server_address,))
    DiagnosticServer.serve_forever()

# Returns server IP address to a "Find Server" client request
def StartFindServer ():
    print("Find Server Running on: %s" % (FindServer.server_address,))
    FindServer.serve_forever()

SSSt = threading.Thread(target=StartSerialServer)
SSSt.start()

SDSt = threading.Thread(target=StartDiagnosticServer)
SDSt.start()

SFSt = threading.Thread(target=StartFindServer)
SFSt.start()
