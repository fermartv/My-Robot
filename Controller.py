
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


	def set_duty_cycle(self, channel, duty_cycle):
		'''Write the given duty_cycle to a specific channel for the 12-bit PWM'''
		
		if 0 <= duty_cycle <= 4095:
			duty_cycle = int(duty_cycle)
		
			reg = self.get_register(channel)

			self.bus.write_byte_data(self.address, reg[0], 0 & 0xFF) #Low byte 
			self.bus.write_byte_data(self.address, reg[1], 0 >> 8) #High byte
			self.bus.write_byte_data(self.address, reg[2], duty_cycle & 0xFF) #Low byte 
			self.bus.write_byte_data(self.address, reg[3], duty_cycle >> 8) #High byte
			
			written_values = [None]*4
			
			for i in range(0, 4):
				written_values[i] = self.bus.read_byte_data(self.address, reg[i])
			
			if self.debug:
				print (debug_info, 'Channel: ', channel)
				for i in range (0, 4):
					print (debug_info, 'Value ', written_values[i], 'written to register ', reg[i])
					
			return written_values
		
		else:
			print ('PWM duty cycle must be a number between 0 and 4095')
			print ('Stopping all channels')
			for channel in range(0, 15):
				self.set_duty_cycle(channel, 0)
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
				self.set_duty_cycle(channel, 0)
			sys.exit()
			
				

		
		
def test_controller():
	min_duty_cycle = 0 #Values from 0 to 4095
	max_duty_cycle = 300 #Values from 0 to 4095
	
	start_channel = 15 #Values from 0 to 15
	end_channel = 16 #Values from 0 to 15
	
	print ('Changing duty cycle from ', min_duty_cycle, ' to ', max_duty_cycle, ' for channels ', start_channel, ' to ', end_channel)
	
	wheel = Controller(debug = debug)
	try:
		for channel in range(start_channel, end_channel+1):
			for i in range(min_duty_cycle,max_duty_cycle+1):
				wheel.set_duty_cycle(channel, i)
			wheel.set_duty_cycle(channel, 0)	
			
	except KeyboardInterrupt:
		print ('Setting the duty cycle back to 0 to exit')
		wheel.set_duty_cycle(channel, 0)
		print ('Test interrupted by user')


if __name__ == '__main__':
	debug = True
	print ('Testing file ', debug_info)
	print ('Testing Controller class')
	test_controller()
	
	
