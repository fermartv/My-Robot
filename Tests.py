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

debug_Controller = True
debug_Rear_Wheel = True
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

		
def test_controller(min_value, max_value, start_channel, end_channel):
	
	print 'Changing values from ', min_value, ' to ', max_value, ' for channels ', start_channel, ' to ', end_channel
	
	wheel = Controller(debug = debug_Controller)
	try:
		for channel in range(start_channel, end_channel+1):
			for i in range(min_value,max_value+1):
				wheel.set_value(channel, i)
			wheel.set_value(channel, 0)	
			
	except KeyboardInterrupt:
		print 'Setting the value back to 0 to exit'
		wheel.set_value(channel, 0)
		print 'Test interrupted by user'	
					
					
if __name__ == '__main__':

	print 'Testing file ', debug_info	
	print 'Testing Wheel class'
	test_wheel()
	
	print 'Testing Controller class'
	min_value = 0 #Values from 0 to 4095
	max_value = 4095 #Values from 0 to 4095
	
	start_channel = 0 #Values from 0 to 15
	end_channel = 1 #Values from 0 to 15
	test_controller(min_value, max_value, start_channel, end_channel)
