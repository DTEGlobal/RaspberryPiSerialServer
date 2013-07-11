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
import os, re

RemoteIP = ""
MessageFromUDP = ""

# Returns server IP address to a "Find Server" client request
def Server ():
    global MessageFromUDP,RemoteIP

    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(('',10000))
    # Find LocalIp from OS.
    ifconfig = os.popen("ifconfig").read()
    # Match LocalIp with Regular Expresion
    IpMatch = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}',ifconfig)
    # Assign Result
    localaddress = IpMatch.group()
    print("ServerThread: Server Running on -> [{}]:[{}]".format(localaddress,'10000'))
    while True:
        data,address=s.recvfrom(256)
        data_toPrint = data.decode()
        # Remove last 3 chars (CR LF)
        data_toPrint = data_toPrint[:-2]
        RemoteIP,port = address
        if localaddress != RemoteIP:
            print ("ServerThread: Cx Received: Address -> [{}] Port -> [{}] Data -> [{}]"\
                .format(RemoteIP,port,data_toPrint))
            MessageFromUDP = data.decode()
        else:
            print ("ServerThread: Cx Received: Address -> [Mine!]: Echo do nothing!")


