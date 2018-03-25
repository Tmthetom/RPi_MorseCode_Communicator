import RPi.GPIO as GPIO
import time

# Main loop
try:
	while True:

# BPIO safe exit
except KeyboardInterrupt:
	GPIO.cleanup()