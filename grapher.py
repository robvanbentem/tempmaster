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
            'DEF:aavg=' + rrd + 'poc1.rrd:a:AVERAGE',
            'DEF:amin=' + rrd + 'poc1.rrd:a:MIN',
            'DEF:amax=' + rrd + 'poc1.rrd:a:MAX',
            'DEF:bavg=' + rrd + 'poc2.rrd:a:AVERAGE',
            'DEF:bmin=' + rrd + 'poc2.rrd:a:MIN',
            'DEF:bmax=' + rrd + 'poc2.rrd:a:MAX',
            'LINE' + lw + ':aavg#E74C3C:Livingroom',
            'GPRINT:amin:LAST:Current\: %2.2lf °C',
            'GPRINT:amin:MIN:Min\: %2.2lf °C',
            'GPRINT:amax:MAX:Max\: %2.2lf °C',
            'GPRINT:aavg:AVERAGE:Avg\: %2.2lf °C\l',
            'LINE' + lw +':bavg#2980B9:Bedroom   ',
            'GPRINT:bmin:LAST:Current\: %2.2lf °C',
            'GPRINT:bmin:MIN:Min\: %2.2lf °C',
            'GPRINT:bmax:MAX:Max\: %2.2lf °C',
            'GPRINT:bavg:AVERAGE:Avg\: %2.2lf °C\l',
#            'LINE1:amax#E74C3C',
#            'LINE1:amin#E74C3C',
#            'LINE1:bmax#2980B9',
#            'LINE1:bmin#2980B9',

            extra,
            )


if __name__ == "__main__":
    makegraphs()
