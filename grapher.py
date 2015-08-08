#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rrdtool
import os

imgpath = os.path.dirname(os.path.realpath(__file__)) + '/public/'

def makegraphs():

    rrdpath = os.path.dirname(os.path.realpath(__file__)) + '/temperature.rrd'

    gmake1h(rrdpath)
    gmake2h(rrdpath)
    gmake1d(rrdpath)
    gmake7d(rrdpath)


# last hour
def gmake1h(rrd):
    rrdtool.graph(imgpath + 'temp1h.png',
            '--imgformat', 'PNG',
            '--width',  '720',
            '--height', '210',
            '--start', '-1h',
            '--vertical-label', 'Temperature (°C)',
            '--title', 'Temperature last 1 hour(s)',
            '-A',
            '--alt-y-grid',
            'DEF:temp=' + rrd + ':a:AVERAGE',
            'LINE2:temp#FFAAAA:Temperature',
            'GPRINT:temp:LAST:Last\: %2.2lf °C',
            'GPRINT:temp:MIN:Min\: %2.2lf °C',
            'GPRINT:temp:MAX:Max\: %2.2lf °C',
            'GPRINT:temp:AVERAGE:Avg\: %2.2lf °C',
            )


# last 2 hours
def gmake2h(rrd):
    rrdtool.graph(imgpath + 'temp2h.png',
            '--imgformat', 'PNG',
            '--width',  '720',
            '--height', '210',
            '--start', '-2h',
            '--vertical-label', 'Temperature (°C)',
            '--title', 'Temperature last 2 hour(s)',
            '-A',
            '--alt-y-grid',
            'DEF:temp=' + rrd + ':a:AVERAGE',
            'LINE2:temp#FFAAAA:Temperature',
            'GPRINT:temp:LAST:Last\: %2.2lf °C',
            'GPRINT:temp:MIN:Min\: %2.2lf °C',
            'GPRINT:temp:MAX:Max\: %2.2lf °C',
            'GPRINT:temp:AVERAGE:Avg\: %2.2lf °C',
            )

# last 1 day
def gmake1d(rrd):
    rrdtool.graph(imgpath + 'temp1d.png',
            '--imgformat', 'PNG',
            '--width',  '720',
            '--height', '210',
            '--start', '-1d',
            '--vertical-label', 'Temperature (°C)',
            '--title', 'Temperature last 1 day(s)',
            '-A',
            '--alt-y-grid',
            'DEF:temp=' + rrd + ':a:AVERAGE',
            'LINE2:temp#FFAAAA:Temperature',
            'GPRINT:temp:LAST:Last\: %2.2lf °C',
            'GPRINT:temp:MIN:Min\: %2.2lf °C',
            'GPRINT:temp:MAX:Max\: %2.2lf °C',
            'GPRINT:temp:AVERAGE:Avg\: %2.2lf °C',
            )


# last 7 days
def gmake7d(rrd):
    rrdtool.graph(imgpath + 'temp7d.png',
            '--imgformat', 'PNG',
            '--width',  '720',
            '--height', '210',
            '--start', '-7d',
            '--vertical-label', 'Temperature (°C)',
            '--title', 'Temperature last 7 day(s)',
            '-A',
            '--alt-y-grid',
            'DEF:temp=' + rrd + ':a:AVERAGE',
            'LINE2:temp#FFAAAA:Temperature',
            'GPRINT:temp:LAST:Last\: %2.2lf °C',
            'GPRINT:temp:MIN:Min\: %2.2lf °C',
            'GPRINT:temp:MAX:Max\: %2.2lf °C',
            'GPRINT:temp:AVERAGE:Avg\: %2.2lf °C',
            )


if __name__ == "__main__":
    makegraphs()
