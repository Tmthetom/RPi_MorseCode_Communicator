# MorseCodeReader - Reading morse code with phototransistor from LED (RGB)
# Timing: https://en.wikipedia.org/wiki/Morse_code#Transmission

import RPi.GPIO as GPIO
import time

# Phototransistor setup
pin = 25

# Settings
timeUnit = 0.1  # Duration of one time unit [s]

# Morse code dictionary
CODE = {"'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

# Board setup
GPIO.setwarnings(False)  # When another doesnt safe exit
GPIO.setmode(GPIO.BCM)  # Refeting pins by Broadcom SOC channel model
GPIO.setup(pin,GPIO.IN)  # All pins as output

# Timing setup (international timing)
dotLength = timeUnit  # For how long is LED visible [s]
dashLength = dotLength * 3
breakLength = dotLength
letterGap = dotLength * 3
wordGap = dotLength * 7

# Variables for time counting
timeStart = time.time()  # Transmitting begin time [s]
timeStop = time.time()  # Transmitting end time [s]
lastState = False  # Last transmitting status (ON, OFF)

# Get transmission time
def getTransmissionTime():
	
	# Usage of global variables
	global timeStart, timeStop, lastState

	# Check for transmitting status changed
	currentState = GPIO.input(pin)  # Read current status
	if (currentState != lastState):  # Status changed

		# Transmitting begin
		if (currentState == True):
			timeStart = time.time()
			timeStop = 0
			print 'Transmitting started'

		# Transmitting end
		else:
			timeStop = time.time()
			print 'Time: ', timeStop - timeStart, ' s'

		lastState = currentState;  # Refresh last status
		time.sleep(0.01)  # Wait for signal stabilization
		return timeStop

# Converting time to dot and dash
def convertTimeToMorseLanguage():
	
		if (timeStop == 0) return;  # No new time

# Decode morse code to letters
def decodeMorseCode():

	# Usage of global variables
	global timeStop
	if (timeStop == 0) return;  # No new time

# Main loop
try:
	while True:
		getTransmissionTime()
		decodeMorseCode()

# BPIO safe exit
except KeyboardInterrupt:
	GPIO.cleanup()