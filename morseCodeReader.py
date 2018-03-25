# MorseCodeReader - Reading morse code with phototransistor from LED (RGB)
# Timing: https://en.wikipedia.org/wiki/Morse_code#Transmission

import RPi.GPIO as GPIO
import time

# Phototransistor setup
pin = 18

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
dotLength = timeUnit;  # For how long is LED visible [s]
dashLength = dotLength * 3
breakLength = dotLength
letterGap = dotLength * 3
wordGap = dotLength * 7

# Main loop
try:
	while True:
		;

# BPIO safe exit
except KeyboardInterrupt:
	GPIO.cleanup()