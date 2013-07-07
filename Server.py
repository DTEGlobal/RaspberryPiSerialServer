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
from TCPSerialServer import SerialClientHandler
from TCPSerialServer import DiagnosticHandler


SerialServer = TCPServer(('localhost',3000),SerialClientHandler)
DiagnosticServer = TCPServer(('localhost',3001),DiagnosticHandler)

# Main Serial Server
def StartSerialServer ():
    SerialServer.serve_forever()

# Returns the status of the serial server for diagnostic purposes
def StartDiagnosticServer ():
    print("Serial Server Running on: %s" % (SerialServer.server_address,))
    DiagnosticServer.serve_forever()

SSSt = threading.Thread(target=StartSerialServer)
SSSt.start()

SDSt = threading.Thread(target=StartDiagnosticServer)
SDSt.start()
