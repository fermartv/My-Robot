
import smbus
import time
import math
import os
import RPi.GPIO as GPIO
import sys


debug_info = os.path.basename(__file__)


class Controller(object):
	def __init__(self, address = 0x40, debug = False):
		'''Create a Controller objet to control each device connected to the PCA9685 PWM Driver'''
		
		self.address = address
		self.bus = smbus.SMBus(1)
		self.debug = debug
		if self.debug:
			print (debug_info, 'Debug set on')
		else:
			print (debug_info, 'Debug set off')


	def set_value(self, channel, value):
		'''Write the given value to a specific channel for the 12-bit PWM'''
		
		if 0 <= value <= 4095:
		
			reg = self.get_register(channel)

			self.bus.write_byte_data(self.address, reg[0], 0 & 0xFF) #Low byte 
			self.bus.write_byte_data(self.address, reg[1], 0 >> 8) #High byte
			self.bus.write_byte_data(self.address, reg[2], value & 0xFF) #Low byte 
			self.bus.write_byte_data(self.address, reg[3], value >> 8) #High byte
			
			written_values = [None]*4
			
			for i in range(0, 4):
				written_values[i] = self.bus.read_byte_data(self.address, reg[i])
			
			if self.debug:
				print (debug_info, 'Channel: ', channel)
				for i in range (0, 4):
					print (debug_info, 'Value ', written_values[i], 'written to register ', reg[i])
					
			return written_values
		
		else:
			print ('PWM value must be a number between 0 and 4095')
			print ('Stopping all channels')
			for channel in range(0, 15):
				self.set_value(channel, 0)
			sys.exit()
		
	def get_register(self, channel):
		'''Get the register according to the given values in the PCA9685 spec'''
		reg = [None]*4
		if 0 <= channel <= 15:
			for i in range(0,4):			
				reg[i] = 6+i+4*channel		
			return reg
		else:
			print ('Channel must be a value between 0 and 15')
			print ('Stopping all channels')
			for channel in range(0, 15):
				self.set_value(channel, 0)
			sys.exit()
			
				

		
		
def test_controller():
	min_value = 0 #Values from 0 to 4095
	max_value = 300 #Values from 0 to 4095
	
	start_channel = 15 #Values from 0 to 15
	end_channel = 16 #Values from 0 to 15
	
	print ('Changing values from ', min_value, ' to ', max_value, ' for channels ', start_channel, ' to ', end_channel)
	
	wheel = Controller(debug = debug)
	try:
		for channel in range(start_channel, end_channel+1):
			for i in range(min_value,max_value+1):
				wheel.set_value(channel, i)
			wheel.set_value(channel, 0)	
			
	except KeyboardInterrupt:
		print ('Setting the value back to 0 to exit')
		wheel.set_value(channel, 0)
		print ('Test interrupted by user')


if __name__ == '__main__':
	debug = True
	print ('Testing file ', debug_info)
	print ('Testing Controller class')
	test_controller()
	
	
