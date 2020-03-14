#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 16

def rc_time (pin_to_circuit):
	count = 0

	#Output on the pin for 
	GPIO.setup(pin_to_circuit, GPIO.OUT)
	GPIO.output(pin_to_circuit, GPIO.LOW)
	time.sleep(0.1)

	#Change the pin back to input
	GPIO.setup(pin_to_circuit, GPIO.IN)
  
	#Count until the pin goes high
	while (GPIO.input(pin_to_circuit) == GPIO.LOW):
		count += 1
		
	return count

print(rc_time(pin_to_circuit))
GPIO.cleanup()