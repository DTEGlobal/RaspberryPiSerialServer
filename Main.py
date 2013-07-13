__author__ = 'Cesar'

#-------------------------------------------------------------------------------
# Name:        Server
# Purpose:
#
# Author:      Cesar
#
# Created:     07/08/2013
# Copyright:   (c) Cesar 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import threading
from Server import Server
from Client import Client
from Serial import Serial
import os

ServerThread = threading.Thread(target=Server)
ServerThread.daemon = True
ServerThread.start()

ClientThread = threading.Thread(target=Client)
ClientThread.daemon = True
ClientThread.start()

SerialThread = threading.Thread(target=Serial)
SerialThread.daemon = True
SerialThread.start()

os.system("sudo python3 /home/pi/SerialServer/Watchdog.py")

while True:
    a=0 #Do nothing