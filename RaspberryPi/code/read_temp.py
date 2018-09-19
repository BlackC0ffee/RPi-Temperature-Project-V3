#!/usr/bin/python
# Copyright (c) 2018 Stijn D'haese

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


# import serial
#import time
import datetime
import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(22, 2)
now = datetime.datetime.now().strftime("%d-%m-%Y,%H:%M")

f = open("/home/pi/log/temperatureData.csv", "a")
f.write('{},{:0.1f},{:0.1f}'.format(now, temperature, humidity))
f.write("\n")
f.close()



#f.write({

#ser = serial.Serial('/dev/ttyACM0', 9600)
#time.sleep(3) #timeout of 3 seconds 
#ser.write("1") #trigger the arduino to send temp 
#data = ser.readline() #read the data 
#dt = datetime.datetime.now() 
#f = open("/home/pi/log/temperatureData.csv", "a")
#f.write(dt.strftime("%d-%m-%Y,%H:%M") + "," + data) # KISS, we just add the data at the end. :)
#f.close();
