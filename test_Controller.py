import unittest
import Controller
import random
import sys

class TestController(unittest.TestCase):
	debug = False

	def test_get_register(self):
		'''Calculated values are equal to the ones given in spec'''
		print (sys.version)
		test_controller = Controller.Controller(debug = self.debug)
		channel0 = [6, 7, 8, 9]
		channel1 = [10, 11, 12, 13]		
		channel2 = [14, 15, 16, 17]
		channel3 = [18, 19, 20, 21]
		channel4 = [22, 23, 24, 25]
		channel5 = [26, 27, 28, 29]
		channel6 = [30, 31, 32, 33]
		channel7 = [34, 35, 36, 37]
		channel8 = [38, 39, 40, 41]
		channel9 = [42, 43, 44, 45]
		channel10 = [46, 47, 48, 49]
		channel11 = [50, 51, 52, 53]
		channel12 = [54, 55, 56, 57]
		channel13 = [58, 59, 60, 61]
		channel14 = [62, 63, 64, 65]
		channel15 = [66, 67, 68, 69]
		
		expected_array = [channel0, channel1, channel2, channel3, channel4, channel5, channel6, channel7, \
			channel8, channel9, channel10, channel11, channel12, channel13, channel14, channel15]

		for channel in range(0, 16):
			expected = expected_array[channel]
			with self.subTest(channel = channel):
				result = test_controller.get_register(channel)
				self.assertEqual(result, expected)

	
	def test_get_register_wrong_channel_high(self):
		'''Invalid channel number '''
		channel = random.randint(16, 100)
		test_controller = Controller.Controller(debug = self.debug)
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.get_register(channel)
		self.assertEqual(cm.exception.code, None)	
			
	def test_get_register_wrong_channel_low(self):
		'''Invalid channel number '''
		channel = random.randint(-5, -1)
		test_controller = Controller.Controller(debug = self.debug)
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.get_register(channel)
		self.assertEqual(cm.exception.code, None)	

			
	def test_set_duty_cycle(self):
		'''Try some duty_cycles in each channel'''
		test_controller = Controller.Controller(debug = self.debug)
		result = [None]*2
		for channel in range (0, 16):
			for i in range(0, 10): #Test 10 different values for each channel
				duty_cycle = random.randint(0, 4095)
				with self.subTest(duty_cycle = duty_cycle):
					written_values = test_controller.set_duty_cycle(channel, duty_cycle)
					result = [written_values[0]+256*written_values[1],written_values[2]+256*written_values[3]] #duty_cycle = (Low byte) + (High byte)*256
					expected = [0,duty_cycle]
					self.assertEqual(result,expected)
			test_controller.set_duty_cycle(channel, 0)
	
	
	def test_set_duty_cycle_wrong_value_high(self):
		'''Invalid PWM number number '''
		test_controller = Controller.Controller(debug = self.debug)
		channel = random.randint(0, 15)
		duty_cycle = random.randint(4096, 5000)
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.set_duty_cycle(channel, duty_cycle)
		self.assertEqual(cm.exception.code, None)	

	def test_set_duty_cycle_wrong_value_low(self):
		'''Invalid PWM number number '''
		test_controller = Controller.Controller(debug = self.debug)
		channel = random.randint(0, 15)
		duty_cycle = random.randint(-500, -1)
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.set_duty_cycle(channel, duty_cycle)
		self.assertEqual(cm.exception.code, None)	
			
	def test_set_duty_cycle_wrong_channel_high(self):
		'''Invalid channel number '''
		test_controller = Controller.Controller(debug = self.debug)
		channel = random.randint(16, 100)
		duty_cycle = random.randint(0, 4095)
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.set_duty_cycle(channel, duty_cycle)
		self.assertEqual(cm.exception.code, None)	
			
	def test_set_duty_cycle_wrong_channel_low(self):
		'''Invalid channel number '''
		test_controller = Controller.Controller(debug = self.debug)
		channel = random.randint(-5, -1)
		duty_cycle = random.randint(0, 4095)
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.set_duty_cycle(channel, duty_cycle)
		self.assertEqual(cm.exception.code, None)

	def test_set_duty_cycle_float_value(self):
		'''Pass a float as Duty cycle 12-bits instead of an integer'''
		test_controller = Controller.Controller(debug = self.debug)
		channel = 15
		duty_cycle = random.uniform(1,2)
		written_values = test_controller.set_duty_cycle(channel, duty_cycle)
		result = [written_values[0]+256*written_values[1],written_values[2]+256*written_values[3]] #duty_cycle = (Low byte) + (High byte)*256
		expected = [0,int(duty_cycle)]
		self.assertEqual(result,expected)
		test_controller.set_duty_cycle(channel, 0)	

			
if __name__ == '__main__':
	unittest.main()