#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rrdtool
import os

imgpath = os.path.dirname(os.path.realpath(__file__)) + '/public/'

def makegraphs():

    rrdpath = os.path.dirname(os.path.realpath(__file__)) + '/'


    # define the graphs we want
    graphs = [
        ['1h', '60', 'past 1 hour', '1', []],
        ['8h', '600', 'past 8 hours', '1', []],
        ['1d', '900', 'past day', '1', []],
        ['7d', '4500', 'past week', '1', []],
        ['1m', '9000', 'past month', '1', []],
        ['3m', '21000', 'past 3 months', '1', []],
    ]

    for opts in graphs:
        gmake(rrdpath, tspan=opts[0], step=opts[1], title=opts[2], extra=opts[4], lw=opts[3])


# make graph
def gmake(rrd, tspan, step='300', title='', extra=[], lw='1'):
    rrdtool.graph(imgpath + 'temp' + tspan +'.png',
            '--imgformat', 'PNG',
            '--width',  '540',
            '--height', '180',
            '--start', '-' + tspan,
            '--vertical-label', 'Temperature (°C)',
            '--title', 'Temperature ' + title,
            '-A',
            '--alt-y-grid',
            '-S', step,
            '-E',
            'DEF:bavg=' + rrd + 'poc2.rrd:a:AVERAGE',
            'DEF:bmin=' + rrd + 'poc2.rrd:a:MIN',
            'DEF:bmax=' + rrd + 'poc2.rrd:a:MAX',
            'DEF:eta=' + rrd + 'esp.rrd:temp:AVERAGE',
            'DEF:etn=' + rrd + 'esp.rrd:temp:MIN',
            'DEF:etx=' + rrd + 'esp.rrd:temp:MAX',
            'DEF:eha=' + rrd + 'esp.rrd:hum:AVERAGE',
            'DEF:ehn=' + rrd + 'esp.rrd:hum:MIN',
            'DEF:ehx=' + rrd + 'esp.rrd:hum:MAX',
            'LINE' + lw +':bavg#2980B9:Bedroom   ',
            'GPRINT:bmin:LAST:Current\: %2.2lf °C',
            'GPRINT:bmin:MIN:Min\: %2.2lf °C',
            'GPRINT:bmax:MAX:Max\: %2.2lf °C',
            'GPRINT:bavg:AVERAGE:Avg\: %2.2lf °C\l',
            'LINE' + lw +':eta#FF80B9:ESP8266   ',
            'GPRINT:etn:LAST:Current\: %2.2lf °C',
            'GPRINT:etn:MIN:Min\: %2.2lf °C',
            'GPRINT:etx:MAX:Max\: %2.2lf °C',
            'GPRINT:eta:AVERAGE:Avg\: %2.2lf °C\l',
#            'LINE1:amax#E74C3C',
#            'LINE1:amin#E74C3C',
#            'LINE1:bmax#2980B9',
#            'LINE1:bmin#2980B9',

            extra,
            )


if __name__ == "__main__":
    makegraphs()
