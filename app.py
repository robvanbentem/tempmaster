#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cherrypy
import time
from master import Master


class MasterApp(object):

    def __init__(self):
        rrdpath = os.path.dirname(os.path.realpath(__file__)) + '/' + cherrypy.config['app']['rrd']
        self.master = Master(rrdpath)

    @cherrypy.expose
    def log(self, d, a, v):
        return self.master.handle(d, a, v)
        
    
cherrypy.config.update("app.conf")

if __name__ == "__main__":
    cherrypy.config.update('server.conf')
    app = cherrypy.tree.mount(MasterApp(), '/', config='app.conf')
    cherrypy.server.start()
    cherrypy.engine.start()
