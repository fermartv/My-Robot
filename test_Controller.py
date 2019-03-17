import unittest
import Controller

class TestController(unittest.TestCase):

	def test_get_register(self):
		channel0 = [6, 7, 8, 9]
		channel1 = [10, 11, 12, 13]
		channel15 = [66, 67, 68, 69]
	
		expected = [channel0, channel1, channel15]
		test_controller = Controller.Controller()
		result = [test_controller.get_register(0), test_controller.get_register(1), test_controller.get_register(15)]
		self.assertEqual(result, expected)
	
	
	def test_get_register_wrong(self):
		test_controller = Controller.Controller()
		with self.assertRaises(SystemExit) as cm:
			result = test_controller.get_register(100)
			self.assertEqual(cm.exception, None)
		
		
if __name__ == '__main__':
	unittest.main(exit = True)