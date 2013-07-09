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

# Send "Find Server" request via UDP
client = socket(AF_INET,SOCK_DGRAM)
client.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
client.sendto("Find Server".encode(),('255.255.255.255',10000))
address,port = client.recvfrom(256)
print ("Remote IP: {}".format(address.decode()))
client.close()
