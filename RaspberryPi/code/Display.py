import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio
from gaugette.fonts import arial_16
import time
import sys
import subprocess
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
screen = False

def On():
    RESET_PIN = 15
    DC_PIN = 16

    spi_bus = 0
    spi_device = 0
    gpio = gaugette.gpio.GPIO()
    spi = gaugette.spi.SPI(spi_bus, spi_device)

    led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=32, cols=128)

    #Stupid hack to get last line of file and to remove the line-end
    filename = '/home/pi/log/temperatureData.csv'
    line = subprocess.check_output(['tail', '-1', filename]).replace('\n', '')

    text = line.split(',')

    #Lets draw
    led.begin()
    led.clear_display()
    led.display()
    font = arial_16
    textSize = led.draw_text3(0,0,text[2] + ' \177C', font)
    textSize = led.draw_text2(0,16,'Log date: ' + text[0], 1)
    textSize = led.draw_text2(0,24,'Log hour: ' + text[1], 1)
    led.display()

def Off():
    import gaugette.platform
    import gaugette.gpio
    from gaugette.fonts import arial_16
    from gaugette.fonts import arial_32
    import time
    import sys
    import subprocess
    RESET_PIN = 15
    DC_PIN = 16

    spi_bus = 0
    spi_device = 0
    gpio = gaugette.gpio.GPIO()
    spi = gaugette.spi.SPI(spi_bus, spi_device)

    led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=32, cols=128)
    led.clear_display()
    led.display()

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        
        if screen == False:
                On()
                screen = True
        elif screen == True:
                Off()
                screen = False
        time.sleep(0.2)
