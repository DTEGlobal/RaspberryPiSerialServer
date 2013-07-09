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

from socketserver import TCPServer, UDPServer
from TCPSerialServer import *
import socket


SerialServer = TCPServer(('',3000),SerialClientHandler)
DiagnosticServer = TCPServer(('',3001),DiagnosticHandler)

# Main Serial Server
def StartSerialServer ():
    ip, port = SerialServer.server_address
    print("Serial Server Running on: {}:{}".format(socket.gethostbyname(socket.gethostname()),port))
    SerialServer.serve_forever()

# Returns the status of the serial server for diagnostic purposes
def StartDiagnosticServer ():
    ip, port = DiagnosticServer.server_address
    print("Diagnostic Server Running on: {}:{}".format(socket.gethostbyname(socket.gethostname()),port))
    DiagnosticServer.serve_forever()

# Returns server IP address to a "Find Server" client request
def StartFindServer ():
    s = socket.socket(AF_INET,SOCK_DGRAM)
    s.bind(('',10000))
    localaddress = socket.gethostbyname(socket.gethostname())
    print("Find Server Running on: {}:{}".format(localaddress,10000))
    while True:
        data,address=s.recvfrom(256)
        addr,port = address
        print ("Connection Received: Data = {} Address = {} Port = {}".format(data.decode(),addr,port))
        if data.decode() == "Find Server":
            s.sendto(localaddress.encode(),address)
        else:
            s.sendto("Error".encode(),address)


SSSt = threading.Thread(target=StartSerialServer)
SSSt.start()

SDSt = threading.Thread(target=StartDiagnosticServer)
SDSt.start()

SFSt = threading.Thread(target=StartFindServer)
SFSt.start()
