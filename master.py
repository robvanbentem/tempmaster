#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import rrdtool
import SocketServer
import time

rrdpath = os.path.dirname(os.path.realpath(__file__)) + '/temperature.rrd'

class MasterTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            # collect and parse data
            self.data = self.request.recv(1024)

            ftemp = int(str(self.data).encode('hex'), 16) * 0.0625

            if 10 <= ftemp <= 40:
                stemp = "%f" % (ftemp)

                # update rrd
                rrdtool.update(rrdpath, 'N:' + stemp)

        except:
            print 'error..'



if __name__ == "__main__":
    HOST, PORT = "192.168.1.1", 4444
    server = SocketServer.TCPServer((HOST, PORT), MasterTCPHandler)
    server.serve_forever()

