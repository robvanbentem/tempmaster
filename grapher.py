#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rrdtool
import os

imgpath = os.path.dirname(os.path.realpath(__file__)) + '/public/'

def makegraphs():

    rrdpath = os.path.dirname(os.path.realpath(__file__)) + '/'


    # define the graphs we want
    graphs = [
        ['1h', '1', 'last 1 hour', []],
        ['8h', '600', 'last 8 hours', []],
        ['1d', '1800', 'last 1 day', []],
        ['7d', '3600', 'last 7 days', []]
    ]

    for opts in graphs:
        gmake(rrdpath, tspan=opts[0], step=opts[1], title=opts[2], extra=opts[3])


# make graph
def gmake(rrd, tspan, step='300', title='', extra=[]):
    rrdtool.graph(imgpath + 'temp' + tspan +'.png',
            '--imgformat', 'PNG',
            '--width',  '720',
            '--height', '210',
            '--start', '-' + tspan,
            '--vertical-label', 'Temperature (°C)',
            '--title', 'Temperature ' + title,
            '-A',
            '-S', step,
            '--alt-y-grid',
            'DEF:aavg=' + rrd + 'poc1.rrd:a:AVERAGE',
            'DEF:amin=' + rrd + 'poc1.rrd:a:MIN',
            'DEF:amax=' + rrd + 'poc1.rrd:a:MAX',
            'DEF:bavg=' + rrd + 'poc2.rrd:a:AVERAGE',
            'DEF:bmin=' + rrd + 'poc2.rrd:a:MIN',
            'DEF:bmax=' + rrd + 'poc2.rrd:a:MAX',
            'LINE2:aavg#E74C3C:Livingroom',
            'GPRINT:aavg:LAST:Current\: %2.2lf °C',
            'GPRINT:amin:MIN:Min\: %2.2lf °C',
            'GPRINT:amax:MAX:Max\: %2.2lf °C',
            'GPRINT:aavg:AVERAGE:Avg\: %2.2lf °C\l',
            'LINE2:bavg#2980B9:Bathroom  ',
            'GPRINT:bavg:LAST:Current\: %2.2lf °C',
            'GPRINT:bmin:MIN:Min\: %2.2lf °C',
            'GPRINT:bmax:MAX:Max\: %2.2lf °C',
            'GPRINT:bavg:AVERAGE:Avg\: %2.2lf °C\l',

            extra,
            )


if __name__ == "__main__":
    makegraphs()
