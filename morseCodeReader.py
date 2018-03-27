# MorseCodeReader - Reading morse code with phototransistor from LED (RGB)
# Timing: https://en.wikipedia.org/wiki/Morse_code#Transmission

import RPi.GPIO as GPIO
import time

# Phototransistor setup
pin = 25

# Settings
timeUnit = 0.1  # Duration of one time unit [s]
precision = 0.02  # Deviation of received time

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
pauseTime = time.time()  # Pause between transmittings
transmitionTime = time.time()  # Transmission time [s]
lastState = False  # Last transmitting status (ON, OFF)

# Variables for dot dash conversion
dotDashString = ''
dot = '.'
dash = '-'

# Get transmission time
def getTransmissionTime():

	# Usage of global variables
	global timeStart, timeStop, lastState
	global transmitionTime, pauseTime

	# Check for transmitting status changed
	currentState = GPIO.input(pin)  # Read current status
	if currentState != lastState:  # Status changed

		# Transmitting begin
		if currentState == True:
			pauseTime = time.time() - timeStop
			timeStart = time.time()
			timeStop = 0
			print 'Pause time: ', pauseTime, ' s'

		# Transmitting end
		else:
			timeStop = time.time()
			pauseTime = 0
			transmitionTime = timeStop - timeStart

		lastState = currentState  # Refresh last status
		time.sleep(0.01)  # Wait for signal stabilization
		return False if timeStop == 0 else True  # Ternary
	return False

# Convert time to dot and dash
def timeToDotDash():

	# Usage of global variables
	global transmitionTime, dotDashString

	# Dot
	if transmitionTime > dotLength - precision and transmitionTime < dotLength + precision:
		dotDashString += dot

	# Dash
	elif transmitionTime > dashLength - precision and transmitionTime < dashLength + precision:
		dotDashString += dash

	else: print 'Not recognized'

# Check for end of word
def checkWordGap():

	# Usage of global variables
	global dotDashString

	# Recognize regular end of letter between letters
	if pauseTime > letterGap - precision and pauseTime < letterGap + precision:
		return True  # End of letter

	# Recognize end of letter on end of word
	if (time.time() - timeStop) > (letterGap - precision) and (time.time() - timeStop) < (letterGap + precision):
		return True  # End of letter

	return False

# Convert dots and dashes to letter
def decodeLetter():

	# Usage of global variables
	global dotDashString

	for letter, code in CODE.iteritems():
		if code == dotDashString:
			print letter
			dotDashString = ''

# Main loop
try:
	while True:

		# Try to decode one letter
		if checkLetterGap():
			decodeLetter()  # Convert dots and dashes to letter

		# Check for incomming data
		newTime = getTransmissionTime()  # Get transmission time

		# If new incomming data
		if newTime:
			timeToDotDash()  # Convert time to dot and dash

# BPIO safe exit
except KeyboardInterrupt:
	GPIO.cleanup()
