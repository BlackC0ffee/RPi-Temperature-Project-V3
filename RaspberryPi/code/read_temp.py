#!/usr/bin/python
# Copyright (c) 2018-2019 Stijn D'haese

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import datetime
import Adafruit_DHT
from influxdb import client as influxdb

humidity, temperature = Adafruit_DHT.read_retry(22, 2)
now = datetime.datetime.now().strftime("%d-%m-%Y,%H:%M")

#Safe data to InfluxDB
influxHost = 'localhost'
influxUser = 'admin'
infile = open('/home/pi/code/secretstring', 'r')
influxPasswd = infile.readline()
infile.close()
influxdbName = 'temperature'

#print('{0}'.format(influxPasswd))

#return influxDB friendly time 2017-02-26T13:33:49.00279827Z (not really required, but meh)
current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

influx_metric = [{
    'measurement': 'TemperatureSensor',
    'time': current_time,
    'fields': {
        'temperature': temperature,
        'humidity': humidity
    }
}]
    

try:
    db = influxdb.InfluxDBClient(influxHost, 8086, influxUser, influxPasswd, influxdbName)
    db.write_points(influx_metric)
finally:
    db.close()