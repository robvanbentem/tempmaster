#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import rrdtool
import time
import cherrypy


class Master(object):

    def __init__(self, rrdpath):
        self.rrdpath = rrdpath

    def esp(self, temp, hum):

        try:
            cherrypy.log("temp: %s; hum: %s" %(temp, hum))
            rrdtool.update(self.rrdpath + 'esp.rrd', 'N:' + str(temp) + ':' + str(hum))
            return "ACK"

        except:
            cherrypy.log("error! [%s]" % sys.exc_info()[0])
            return "NACK"


    def pic(self, device, attribute, value):

        try:
            ftemp = int(value) * 0.0625

            if 10 <= ftemp <= 40:
                stemp = "%f" % (ftemp)

                cherrypy.log("%s %s: %s" %(device, attribute, stemp))

                # update rrd
                rrdtool.update(self.rrdpath + str(device) + '.rrd', '-t', str(attribute), 'N:' + stemp)

                return "ACK"

        except:
            cherrypy.log("error! [%s]" % sys.exc_info()[0])
            return "NACK"
