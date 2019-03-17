''' 
To do:
	- Debug.
	- 


'''

from Controller import Controller
import time
import os
import RPi.GPIO as GPIO



debug_info = os.path.basename(__file__)

class Rear_Wheel(object):
	'''Create a wheel object controlled by the Controller PCA9685'''
	
	controller_address = 0x40
	
	def __init__(self, PCAchannel, pin, debug = False):
		self.debug = debug
		self.controller = Controller(self.controller_address, debug)
		self.PCAchannel = PCAchannel
		self.pin = pin
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin, GPIO.OUT)
		
	def speed_converter(self, speed):
		'''Converts speed from 0-100 to 0-4095'''
		if 0 <= speed <= 100:
			value = 40.95*speed
		else:
			value = 0
			print 'Speed values must be between 0 and 100'
			
			if self.debug:
				print debug_info, 'Exiting program due to invalid speed value'
			GPIO.cleanup()
			exit()
			
		value = int(value)
		if self.debug:
			print debug_info, 'Speed ', speed, 'converted to ', value
		
		return value		

		
		
	def forward(self, speed):
		'''Sets the movement of the wheel forwards to a given speed'''
		GPIO.output(self.pin, False)
		value = self.speed_converter(speed)
		self.controller.set_value(self.PCAchannel, value)
		if self.debug:
			print debug_info, 'Wheel connected to pin', self.pin, 'in the Raspberry Pi GPIO and channel', self.PCAchannel,'in the PCA9685 is moving forwards at speed', speed
		
	def backwards(self, speed):
		'''Sets the movement of the wheel backwards to a given speed'''
		GPIO.output(self.pin, True)
		value = self.speed_converter(speed)
		self.controller.set_value(self.PCAchannel, value)
		if self.debug:
			print debug_info, 'Wheel connected to pin', self.pin, 'in the Raspberry Pi GPIO and channel', self.PCAchannel,'in the PCA9685 is moving backwards at speed', speed
		
	def stop(self):	
		'''Stops the wheel'''	
		self.controller.set_value(self.PCAchannel, 0)		
		if self.debug:
			print debug_info, 'Wheel connected to pin', self.pin, 'in the Raspberry Pi GPIO and channel', self.PCAchannel,'in the PCA9685 has stopped'
		
		



def test_wheel():
	
	speed = 100  #Values from 0 to 100
	wait = 0.5
	
	left_PCAchannel = 5  #Values from 0 to 15
	left_pin = 17 #Left wheel = 17; right wheel = 27
	right_PCAchannel = 4  #Values from 0 to 15
	right_pin = 27 #Left wheel = 17; right wheel = 27
	
	try:
		left_wheel = Rear_Wheel(left_PCAchannel, left_pin, debug = debug)
		right_wheel = Rear_Wheel(right_PCAchannel, right_pin, debug = debug)
		
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

	debug = True
	print 'Testing file ', debug_info	
	print 'Testing Wheel class'
	test_wheel()
	
