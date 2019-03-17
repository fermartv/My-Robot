''' 
To do:
	Test incremento / decremento de velocidades de las dos ruedas
	Test valor de velocidad incorrecto
	Test de canales o pines incorrectos

'''

from Controller import Controller
from Wheel import Rear_Wheel
import time
import os
import RPi.GPIO as GPIO

debug_Controller = False
debug_Rear_Wheel = False
debug_info = os.path.basename(__file__)

def test_wheel():
	
	speed = 100  #Values from 0 to 100
	wait = 1
	
	left_PCAchannel = 5  #Values from 0 to 15
	left_pin = 17 #Left wheel = 17; right wheel = 27
	right_PCAchannel = 4  #Values from 0 to 15
	right_pin = 27 #Left wheel = 17; right wheel = 27
	
	try:
		left_wheel = Rear_Wheel(left_PCAchannel, left_pin, debug = debug_Rear_Wheel)
		right_wheel = Rear_Wheel(right_PCAchannel, right_pin, debug = debug_Rear_Wheel)
		
		left_wheel.forward(speed)
		time.sleep(wait)
		left_wheel.backwards(speed)
		time.sleep(wait)
		left_wheel.stop()
		
		right_wheel.forward(speed)
		time.sleep(wait)
		right_wheel.backwards(speed)
		time.sleep(wait)
		right_wheel.stop()

		GPIO.cleanup()
		
	except KeyboardInterrupt:
		print 'Stopping wheels'
		left_wheel.stop()
		right_wheel.stop()
		GPIO.cleanup()
		print 'Test interrupted by user'
					
					
					
					
if __name__ == '__main__':

	print 'Testing file ', debug_info	
	print 'Testing Wheel class'
	test_wheel()
