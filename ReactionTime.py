
### This program controls the state of the virtual assistant ROLL-E's animations at Villanova University
###
### Author: Noah Schwanke 		Created: 12/3/17

import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO! This is probably because you need superuser privileges.")

##############################################################################################################################
## GPIO setup

## Set numbering mode

GPIO.setmode(GPIO.BCM)

## Set pin numbers

pin1 = 26
pin2 = 19
pin3 = 13
pin4 = 6

## Set channels

#GPIO.setup(pin1, GPIO.IN)
#GPIO.setup(pin2, GPIO.IN)
#GPIO.setup(pin3, GPIO.IN)
#GPIO.setup(pin4, GPIO.IN)

## set default inputs to 0 -- should this be done in this script? Probably handled by david?

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


defaultState = [GPIO.input(pin2),GPIO.input(pin3),GPIO.input(pin4)]  

# print defaultState ## This should be all 0's

print(defaultState)

##############################################################################################################################
## LED Matrix config

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 2
options.parallel = 1
options.gpio_slowdown = 2
options.hardware_mapping = 'regular'


matrix = RGBMatrix(options = options)

##############################################################################################################################
## Importing images

sleep1 = Image.open("ROLLESleep1.png")
sleep2 = Image.open("ROLLESleep2.png")

closedmouth = Image.open("ROLLE.png")
blink = Image.open("ROLLEEyesClosed.png")

# openmouth = Image.open("ROLLEMouthOpen.png")
talking1 = Image.open("ROLLETalk1.png")
talking2 = Image.open("ROLLETalk2.png")

thinking1 = Image.open("ROLLEThinking1.png")
thinking2 = Image.open("ROLLEThinking2.png")

happy = Image.open("ROLLEHappy.png")
sad = Image.open("ROLLESad.png")
mad = Image.open("ROLLEMad.png")
nationer1 = Image.open("ROLLEVEyes1.png")
nationer2 = Image.open("ROLLEVEyes2.png")
#############################################################################################################################
## Setting states as lists

awake = [False, False, True]
thinking = [False, True, False]
talking = [False, True, True]
villanova = [True, False, False]

##############################################################################################################################
## Functions and event trigger handler
def playTalking():
        #GPIO.add_event_detect(pin1, GPIO.BOTH, callback=my_callback)
        while (1):
                matrix.SetImage(talking1.convert('RGB'))

                time.sleep(.5)

                matrix.Clear()

                matrix.SetImage(talking2.convert('RGB'))

                time.sleep(.5)

                matrix.Clear()

def playNationer():
        #GPIO.add_event_detect(pin1, GPIO.BOTH, callback=my_callback)
        while (1):
                matrix.SetImage(nationer1.convert('RGB'))

                time.sleep(1)

                matrix.Clear()

                matrix.SetImage(nationer2.convert('RGB'))

                time.sleep(1)

                matrix.Clear()

def playAwake():
        #GPIO.add_event_detect(pin1, GPIO.BOTH, callback=my_callback)
        while (1):
                matrix.SetImage(closedmouth.convert('RGB'))

                time.sleep(3)

                matrix.Clear()

                matrix.SetImage(blink.convert('RGB'))

                time.sleep(.3)

                matrix.Clear()

def playThinking():
        #GPIO.add_event_detect(pin1, GPIO.BOTH, callback=my_callback)
        while (1):
                matrix.SetImage(thinking1.convert('RGB'))

                time.sleep(.5)

                matrix.Clear()

                matrix.SetImage(thinking2.convert('RGB'))

                time.sleep(.5)

                matrix.Clear()


def callback(pin1):
	time.sleep(.01) #small pause to allow for all signals to be received
	currentState = [GPIO.input(pin2),GPIO.input(pin3),GPIO.input(pin4)]

	## Check to see if current state = awake
	if ((currentState[0] == awake[0]) and (currentState[1] == awake[1]) and (currentState[2] == awake[2])):
		playAwake()

	## Check to see if current state = thinking
	if ((currentState[0] == thinking[0]) and (currentState[1] == thinking[1]) and (currentState[2] == thinking[2])):
		playThinking()

	## Check to see if current state = talking
	if ((currentState[0] == talking[0]) and (currentState[1] == talking[1]) and (currentState[2] == talking[2])):
		playTalking()

	## Check to see if current state = nationer
	if ((currentState[0] == villanova[0]) and (currentState[1] == villanova[1]) and (currentState[2] == villanova[2])):
		playNationer()

##############################################################################################################################
## Finite State Machine 

## GPIO.wait_for_edge(##, GPIO.RISING) 
## GPIO.input(pin1):

print("\n\nEntering infinite loop..")

# Begin infinite loop of ROLL-E Animations
#while (1):
GPIO.add_event_detect(26, GPIO.FALLING, callback=callback)
	

	#print "Display Sponsor proc#" + str(disp.pid)
