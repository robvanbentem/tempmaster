#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rrdtool
import os

imgpath = os.path.dirname(os.path.realpath(__file__)) + '/public/'

def makegraphs():

    rrdpath = os.path.dirname(os.path.realpath(__file__)) + '/temperature.rrd'


    # define the graphs we want
    graphs = [
        ['1h', 'last 1 hour'],
        ['8h', 'last 8 hours'],
        ['1d', 'last 1 day'],
        ['7d', 'last 7 days'],
    ];

    for opts in graphs:
        gmake(rrdpath, opts[0], opts[1])


# make graph
def gmake(rrd, tspan, title):
    rrdtool.graph(imgpath + 'temp' + tspan +'.png',
            '--imgformat', 'PNG',
            '--width',  '720',
            '--height', '210',
            '--start', '-' + tspan,
            '--vertical-label', 'Temperature (°C)',
            '--title', 'Temperature ' + title,
            '-A',
            '--alt-y-grid',
            'DEF:tempa=' + rrd + ':a:AVERAGE',
            'DEF:tempb=' + rrd + ':a:MIN',
            'DEF:tempc=' + rrd + ':a:MAX',
            'LINE2:tempa#2C3E50:Avg',
            'LINE2:tempb#3498DB:Min',
            'LINE2:tempc#E74C3C:Max',
            'GPRINT:tempa:LAST:Last\: %2.2lf °C',
            'GPRINT:tempb:MIN:Min\: %2.2lf °C',
            'GPRINT:tempc:MAX:Max\: %2.2lf °C',
            'GPRINT:tempa:AVERAGE:Avg\: %2.2lf °C',
            )


if __name__ == "__main__":
    makegraphs()
