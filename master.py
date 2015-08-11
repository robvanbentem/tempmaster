#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import rrdtool
import time
import cherrypy


class Master(object):

    def __init__(self, rrdpath):
        self.rrdpath = rrdpath

    def handle(self, device, attribute, value):

        try:
            ftemp = int(value) * 0.0625

            if 10 <= ftemp <= 40:
                stemp = "%f" % (ftemp)

                cherrypy.log("%s reported %s:%s" %(device, attribute, stemp))

                # update rrd
                rrdtool.update(self.rrdpath, '-t', str(attribute), 'N:%s' % stemp)

                return "ACK"

        except:
            cherrypy.log("error! [%s]" % sys.exc_info()[0])
            return "NACK"
