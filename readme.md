### Simple temperature logger

Create a tcp server and wait for temperature logger to connect.

This script expects values from a ds18b20 sensor. The reported value is multiplied by 0.0625 (12bit acuracy on the sensor) and stored in a rrd db.

Graphs with multiple timeframes will be created.


#### RRD database

Use this command to create a rrd:

    rrdtool create temperature.rrd \
        --start now --step 1m \
        DS:a:GAUGE:120:0:50 \
        RRA:AVERAGE:0.5:1m:1440 \
        RRA:MIN:0.5:1m:1440 \
        RRA:MAX:0.5:1m:1440 \
        RRA:AVERAGE:0.5:5m:2016 \
        RRA:MIN:0.5:5m:2016 \
        RRA:MAX:0.5:5m:2016 \
        RRA:AVERAGE:0.5:30m:1440 \
        RRA:MIN:0.5:30m:1440 \
        RRA:MAX:0.5:30m:1440 \
        RRA:AVERAGE:0.5:4h:2190 \
        RRA:MIN:0.5:4h:2190 \
        RRA:MAX:0.5:4h:2190
