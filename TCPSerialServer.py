__author__ = 'Cesar'
#-------------------------------------------------------------------------------
# Name:        SerialServerHandler
# Purpose:     Handle requests form SerialClients and Diagnostic Request.
#
# Author:      Cesar
#
# Created:     07/07/2013
# Copyright:   (c) Cesar 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# TODO check if import for Python 2 is needed
from socketserver import StreamRequestHandler

# Handles Serial Clients requests
class SerialClientHandler (StreamRequestHandler):
    def handle(self):
        response = "Serial Clients Handler"+"\r\n"
        self.wfile.write(response.encode())

# Handles Serial Clients requests
class DiagnosticHandler (StreamRequestHandler):
    def handle(self):
        response = "Diagnostic Handler"+"\r\n"
        self.wfile.write(response.encode())


