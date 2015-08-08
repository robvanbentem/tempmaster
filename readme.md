### Simple temperature logger

Create a tcp server and wait for temperature logger to connect.

This script expects values from a ds18b20 sensor. The reported value is multiplied by 0.0625 (12bit acuracy on the sensor) and stored in a rrd db.

Graphs with multiple timeframes will be created.


#### RRD database

Use this command to create a rrd:

`rrdtool create temperature.rrd 
    --start now --step 60 
    DS:a:GAUGE:120:-50:50 
    RRA:AVERAGE:0.5:1:12 
    RRA:AVERAGE:0.5:1:288 
    RRA:AVERAGE:0.5:12:168 
    RRA:AVERAGE:0.5:12:720 
    RRA:AVERAGE:0.5:288:365`
