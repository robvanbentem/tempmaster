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
            '--width',  '720',
            '--height', '240',
            '--start', '-' + tspan,
            '--vertical-label', 'Temperature (°C)',
            '--title', 'Temperature ' + title,
            '--alt-y-grid',
            '-S', step,
            '-E',
            '-A',
            'DEF:bavg=' + rrd + 'poc2.rrd:a:AVERAGE',
            'DEF:bmin=' + rrd + 'poc2.rrd:a:MIN',
            'DEF:bmax=' + rrd + 'poc2.rrd:a:MAX',
            'DEF:tavg=' + rrd + 'esp.rrd:temp:AVERAGE',
            'DEF:tmin=' + rrd + 'esp.rrd:temp:MIN',
            'DEF:tmax=' + rrd + 'esp.rrd:temp:MAX',
            'DEF:havg=' + rrd + 'esp.rrd:hum:AVERAGE',
            'DEF:hmin=' + rrd + 'esp.rrd:hum:MIN',
            'DEF:hmax=' + rrd + 'esp.rrd:hum:MAX',
            'CDEF:hline=havg,2,/',
            'LINE' + lw +':bavg#FEAC00:DS18B20    ',
            'GPRINT:bavg:LAST:Current\: %2.2lf °C',
            'GPRINT:bmin:MIN:Min\: %2.2lf °C',
            'GPRINT:bmax:MAX:Max\: %2.2lf °C',
            'GPRINT:bavg:AVERAGE:Avg\: %2.2lf °C\l',
            'LINE' + lw +':tavg#F25C05:DHT22 Temp.',
            'GPRINT:tavg:LAST:Current\: %2.2lf °C',
            'GPRINT:tmin:MIN:Min\: %2.2lf °C',
            'GPRINT:tmax:MAX:Max\: %2.2lf °C',
            'GPRINT:tavg:AVERAGE:Avg\: %2.2lf °C\l',
            '--right-axis-label', 'Humidity (RH %)',
            '--right-axis', '2:0',
            'LINE' + lw +':hline#3A50FE:DHT22 Hum. ',
            'GPRINT:havg:LAST:Current\: %2.2lf  %%',
            'GPRINT:hmin:MIN:Min\: %2.2lf  %%',
            'GPRINT:hmax:MAX:Max\: %2.2lf  %%',
            'GPRINT:havg:AVERAGE:Avg\: %2.2lf  %%\l',
#            'LINE1:amax#E74C3C',
#            'LINE1:amin#E74C3C',
#            'LINE1:bmax#2980B9',
#            'LINE1:bmin#2980B9',

            extra,
            )


if __name__ == "__main__":
    makegraphs()
