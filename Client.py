__author__ = 'Cesar'

#-------------------------------------------------------------------------------
# Name:        Client
# Purpose:
#
# Author:      Cesar
#
# Created:     07/07/2013
# Copyright:   (c) Cesar 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from socket import *
import Serial, Server

def Client():

    print ("ClientThread: Client Thread Running ...")

    while True:
        if Serial.MessageFromSerial != "":
            ClientSocket = socket(AF_INET,SOCK_DGRAM)
            if Server.RemoteIP != "":
                ClientSocket.sendto(Serial.MessageFromSerial.encode(),(Server.RemoteIP,10000))
                data_toPrint = Serial.MessageFromSerial.decode()
                # Remove last 3 chars (CR LF)
                data_toPrint = data_toPrint[:-2]
                print("CT: Sent to->[{}] Data->[{}]".format(Server.RemoteIP,data_toPrint))
            else:
                ClientSocket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
                ClientSocket.sendto(Serial.MessageFromSerial.encode(),('255.255.255.255',10000))
                data_toPrint = Serial.MessageFromSerial.decode()
                # Remove last 3 chars (CR LF)
                data_toPrint = data_toPrint[:-2]
                print("CT: Sent to->[255.255.255.255] Data->[{}]".format(data_toPrint))
            ClientSocket.close()
            Serial.MessageFromSerial = ""
            Server.RemoteIP = ""
