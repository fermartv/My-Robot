import unittest
import Controller
from random import randint
import sys

class TestController(unittest.TestCase):


	def test_get_register(self):
		'''Calculated values are equal to the ones given in spec'''
		print (sys.version)
		test_controller = Controller.Controller(debug = True)
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
		channel = randint(16, 100)
		test_controller = Controller.Controller(debug = True)
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.get_register(channel)
		self.assertEqual(cm.exception.code, None)	
			
	def test_get_register_wrong_channel_low(self):
		'''Invalid channel number '''
		channel = randint(-5, -1)
		test_controller = Controller.Controller(debug = True)
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.get_register(channel)
		self.assertEqual(cm.exception.code, None)	

			
	def test_set_value(self):
		'''Try some values in each channel'''
		test_controller = Controller.Controller(debug = True)
		result = [None]*2
		for channel in range (0, 16):
			for i in range(0, 10):
				value = randint(0, 4095)
				with self.subTest(value = value):
					written_values = test_controller.set_value(channel, value)
					result = [written_values[0]+256*written_values[1],written_values[2]+256*written_values[3]] #value = (Low byte) + (High byte)*256
					expected = [0,value]
					self.assertEqual(result,expected)
			test_controller.set_value(channel, 0)
	
	
	def test_set_value_wrong_value_high(self):
		'''Invalid PWM number number '''
		test_controller = Controller.Controller(debug = True)
		channel = randint(0, 15)
		value = randint(4096, 5000)
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.set_value(channel, value)
		self.assertEqual(cm.exception.code, None)	

	def test_set_value_wrong_value_low(self):
		'''Invalid PWM number number '''
		test_controller = Controller.Controller(debug = True)
		channel = randint(0, 15)
		value = randint(-500, -1)
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.set_value(channel, value)
		self.assertEqual(cm.exception.code, None)	
			
	def test_set_value_wrong_channel_high(self):
		'''Invalid channel number '''
		test_controller = Controller.Controller(debug = True)
		channel = randint(16, 100)
		value = randint(0, 4095)
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.set_value(channel, value)
		self.assertEqual(cm.exception.code, None)	
			
	def test_set_value_wrong_channel_low(self):
		'''Invalid channel number '''
		test_controller = Controller.Controller(debug = True)
		channel = randint(-5, -1)
		value = randint(0, 4095)
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.set_value(channel, value)
		self.assertEqual(cm.exception.code, None)			

			
if __name__ == '__main__':
	unittest.main()