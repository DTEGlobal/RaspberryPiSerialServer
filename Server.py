__author__ = 'Cesar'
#-------------------------------------------------------------------------------
# Name:        PruebaSerial1
# Purpose:
#
# Author:      Cesar
#
# Created:     21/06/2013
# Copyright:   (c) Cesar 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=1.0)
while True:
    port.write("00S?1\r\n")
    print(port.readline())
    port.write("00MB\r\n")
    print(port.readline())
    port.write("00E\r\n")
    print(port.readline())

    print('test GitHub')
