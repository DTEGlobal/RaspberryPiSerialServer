__author__ = 'Cesar'

#-------------------------------------------------------------------------------
# Name:        Serial
# Purpose:
#
# Author:      Cesar
#
# Created:     07/08/2013
# Copyright:   (c) Cesar 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import serial
import threading
import Server

MessageFromSerial = ""

def Rx():

    print ("RxSerialThread: Rx Thread Running ...")
    while True:
        global RxBusy, MessageFromSerial
        MessageFromSerial = port.readline()
        print ("RxSerialThread: Rx -> {}".format(MessageFromSerial))

def Tx():

    print ("TxSerialThread: Tx Thread Running ...")
    while True:
        if Server.MessageFromUDP != "":
             port.write(Server.MessageFromUDP+"\r\n")
             Server.MessageFromUDP = ""


def Serial():
    global port

    port = serial.Serial("/dev/ttyAMA0", baudrate=19200)

    SerialRxThread = threading.Thread(target=Rx)
    SerialRxThread.start()

    SerialTxThread = threading.Thread(target=Tx)
    SerialTxThread.start()
