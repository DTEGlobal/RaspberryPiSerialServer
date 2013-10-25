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
import Feeder
import uuid
RemoteIP = ""
MessageFromUDP = ""



# Returns server IP address to a "Find Server" client request
def Server ():
    global MessageFromUDP,RemoteIP

    id = str(uuid.uuid4())
    s = socket(AF_INET,SOCK_DGRAM)
    s.setblocking(False)
    s.bind(('',10000))
    # Find LocalIp from OS.
    ifconfig = os.popen("ifconfig").read()
    # Match LocalIp with Regular Expression
    IpMatch = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}',ifconfig)
    # Assign Result
    localaddress = IpMatch.group()
    diagnosticMsg = "ST: Server Running on->[{}]:[{}]".format(localaddress,'10000')
    #print(diagnosticMsg)
    while True:
        Feeder.feeder(id,diagnosticMsg)
        try:
            data,address=s.recvfrom(256)
            data_toPrint = data.decode()
            # Remove last 3 chars (CR LF)
            data_toPrint = data_toPrint[:-2]
            RemoteIP,port = address
            # Find LocalIp from OS.
            ifconfig = os.popen("ifconfig").read()
            # Match LocalIp with Regular Expression
            IpMatch = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}',ifconfig)
            # Assign Result
            localaddress = IpMatch.group()
            if localaddress != RemoteIP:
                diagnosticMsg = "ST: Cx Received: Address->[{}] Port->[{}] Data->[{}]"\
                    .format(RemoteIP,port,data_toPrint)
                #print (diagnosticMsg)
                MessageFromUDP = data.decode()
            else:
                diagnosticMsg = "ST: Cx Received: Address->[Mine!]: Echo do nothing!"
                #print (diagnosticMsg)
        except error:
            diagnosticMsg = ""

