# MorseCodeWriter - Morse code visualisation on LED (RGB)
# Timing: https://en.wikipedia.org/wiki/Morse_code#Transmission

import RPi.GPIO as GPIO
import time

# LED setup
red = 18
green = 23
blue = 24

# Settings
selectedColor = red  # Selected color of LED
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
GPIO.setup(red,GPIO.OUT)  # All pins as output
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)

# Common anode setup
GPIO.output(red,GPIO.HIGH) # Common [anode = HIGH, catode = LOW]
GPIO.output(green,GPIO.HIGH)
GPIO.output(blue,GPIO.HIGH)

# Timing setup (international timing)
dotLength = timeUnit;  # For how long is LED visible [s]
dashLength = dotLength * 3
breakLength = dotLength
letterGap = dotLength * 3
wordGap = dotLength * 7

# Dot visualisation
def dot():
	GPIO.output(selectedColor,GPIO.LOW)
	time.sleep(dotLength)
	GPIO.output(selectedColor,GPIO.HIGH)
	time.sleep(breakLength)

# Dash visualisation
def dash():
	GPIO.output(selectedColor,GPIO.LOW)
	time.sleep(dashLength)
	GPIO.output(selectedColor,GPIO.HIGH)
	time.sleep(breakLength)

# Main loop
try:
	while True:
		input = raw_input('What would you like to send? ')
		for letter in input:
			time.sleep(letterGap)

			# Space between words
			if letter == ' ':
				time.sleep(wordGap)
				continue;

			# Character visualisation
			for symbol in CODE[letter.upper()]:
				if symbol == '.':  # Dot
					dot()
				elif symbol == '-':  # Dash
					dash()

# BPIO safe exit
except KeyboardInterrupt:
	GPIO.cleanup()