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

    print ("RxST: Rx Thread Running ...")
    while True:
        global MessageFromSerial
        try:
            MessageFromSerial = port.readline()
            # Remove last 3 chars (CR LF)
            data_toPrint = MessageFromSerial[:-2]
            print ("RxST: Rx Data->[{}]".format(data_toPrint))
        except serial.SerialException as e:
            print ("RxST: Error->[{}]".format(e))
            port.flushInput()


def Tx():

    print ("TxST: Tx Thread Running ...")
    while True:
        if Server.MessageFromUDP != "":
            try:
                port.write(Server.MessageFromUDP)
                # Remove last 3 chars (CR LF)
                data_toPrint = Server.MessageFromUDP[:-2]
                print ("TxST: Tx Data->[{}]".format(data_toPrint))
                Server.MessageFromUDP = ""
            except serial.SerialException as e:
                print ("TxST: Error->[{}]".format(e))
                port.flushOutput()

def Serial():
    global port

    port = serial.Serial("/dev/ttyAMA0", baudrate=19200)

    SerialRxThread = threading.Thread(target=Rx)
    SerialRxThread.start()

    SerialTxThread = threading.Thread(target=Tx)
    SerialTxThread.start()
