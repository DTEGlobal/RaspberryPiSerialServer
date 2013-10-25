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
import time

def watchdog():
    os.system("sudo python /home/pi/watchdog/main.py")


ServerThread = threading.Thread(target=watchdog)
ServerThread.daemon = True
ServerThread.start()

time.sleep(.5)

ServerThread = threading.Thread(target=Server)
ServerThread.daemon = True
ServerThread.start()

ClientThread = threading.Thread(target=Client)
ClientThread.daemon = True
ClientThread.start()

SerialThread = threading.Thread(target=Serial)
SerialThread.daemon = True
SerialThread.start()


while True:
    a=0 #Do nothing