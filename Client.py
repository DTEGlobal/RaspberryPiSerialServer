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

client = socket(AF_INET,SOCK_STREAM)
client.connect(('localhost',3000))
client.send("va1".encode())
respuesta = client.recv(512)
print (respuesta.decode())
client.close()