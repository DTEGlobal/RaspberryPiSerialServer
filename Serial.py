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
import uuid
import Feeder

MessageFromSerial = ""

def Rx():
    RxId = str(uuid.uuid4())
    data_toPrint = "RxST: Rx Thread Running ..."
    #print (data_toPrint)
    while True:
        global MessageFromSerial
        Feeder.feeder(RxId,data_toPrint)
        try:
            MessageFromSerial = port.readline()
            # Remove last 3 chars (CR LF)
            data_toPrint = "RxST: Rx Data->[{}]".format(MessageFromSerial[:-2])
            #print (data_toPrint)
        except serial.SerialException as e:
            data_toPrint = "RxST: Error->[{}]".format(e)
            #print (data_toPrint)
            port.flushInput()
        except serial.SerialTimeoutException:
            data_toPrint = ""

def Tx():
    TxId = str(uuid.uuid4())
    data_toPrint = "TxST: Tx Thread Running ..."
    #print (data_toPrint)
    while True:
        Feeder.feeder(TxId,data_toPrint)
        data_toPrint = ""
        if Server.MessageFromUDP != "":
            try:
                port.write(Server.MessageFromUDP)
                # Remove last 3 chars (CR LF)
                data_toPrint = "TxST: Tx Data->[{}]".format(Server.MessageFromUDP[:-2])
                #print (data_toPrint)
                Server.MessageFromUDP = ""
            except serial.SerialException as e:
                data_toPrint = "TxST: Error->[{}]".format(e)
                #print (data_toPrint)
                port.flushOutput()


def Serial():
    global port

    port = serial.Serial("/dev/ttyAMA0", baudrate=19200,timeout=1)

    SerialRxThread = threading.Thread(target=Rx)
    SerialRxThread.start()

    SerialTxThread = threading.Thread(target=Tx)
    SerialTxThread.start()

