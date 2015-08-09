#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rrdtool
import os

imgpath = os.path.dirname(os.path.realpath(__file__)) + '/public/'

def makegraphs():

    rrdpath = os.path.dirname(os.path.realpath(__file__)) + '/temperature.rrd'


    # define the graphs we want
    graphs = [
        ['1h', '120', 'last 1 hour', []],
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
            'DEF:avg=' + rrd + ':a:AVERAGE',
            'DEF:min=' + rrd + ':a:MIN',
            'DEF:max=' + rrd + ':a:MAX',
            'LINE2:avg#2C3E50:DS18B20 Sensor',
            'GPRINT:avg:LAST:Current\: %2.2lf °C',
            'GPRINT:min:MIN:Min\: %2.2lf °C',
            'GPRINT:max:MAX:Max\: %2.2lf °C',
            'GPRINT:avg:AVERAGE:Avg\: %2.2lf °C\l',
            extra,
            )


if __name__ == "__main__":
    makegraphs()
