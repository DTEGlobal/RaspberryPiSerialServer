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

from socket import *

RemoteIP = ""
MessageFromUDP = ""

# Returns server IP address to a "Find Server" client request
def Server ():
    global MessageFromUDP,RemoteIP

    print ("ServerThread: Server Thread Running ...")
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(('',10000))
    #TODO esto apesta!!
    localaddress = s.getsockname()
    print("ServerThread: Server Running on -> {}:{}".format(localaddress,10000))
    while True:
        data,address=s.recvfrom(256)
        RemoteIP,port = address
        print ("ServerThread: Connection Received: Address -> {} Port -> {} Data -> {}"\
                .format(RemoteIP,port,data.decode()))
        MessageFromUDP = data.decode()

