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
import uuid
import Feeder

def Client():
    id = str(uuid.uuid4())
    data_toPrint = "ClientThread: Client Thread Running ..."
    #print (data_toPrint)
    while True:
        Feeder.feeder(id,data_toPrint)
        data_toPrint = ""
        if Serial.MessageFromSerial != "":
            ClientSocket = socket(AF_INET,SOCK_DGRAM)
            if Server.RemoteIP != "":
                ClientSocket.sendto(Serial.MessageFromSerial.encode(),(Server.RemoteIP,10000))
                data_toPrint = Serial.MessageFromSerial.decode()
                # Remove last 3 chars (CR LF)
                data_toPrint = "CT: Sent to->[{}] Data->[{}]".format(Server.RemoteIP,data_toPrint[:-2])
                #print(data_toPrint)
            else:
                ClientSocket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
                ClientSocket.sendto(Serial.MessageFromSerial.encode(),('192.168.1.255',10000))
                data_toPrint = Serial.MessageFromSerial.decode()
                # Remove last 3 chars (CR LF)
                data_toPrint = "CT: Sent to->[192.168.1.255] Data->[{}]".format(data_toPrint[:-2])
                #print(data_toPrint)
            ClientSocket.close()
            Serial.MessageFromSerial = ""
            Server.RemoteIP = ""
