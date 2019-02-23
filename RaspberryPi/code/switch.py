#Demo Code
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

screen = False

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
    if screen == False:
		print('screen turned on')
		screen = True
	elif screen == True:
		print('Screen is turned off')
		screen = False
        time.sleep(0.2)
