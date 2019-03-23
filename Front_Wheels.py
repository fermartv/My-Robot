
from Controller import Controller
import time
import os





debug_info = os.path.basename(__file__)

class Front_Wheels(object):
	'''Create a front_wheels object controlled by the Controller PCA9685'''
	controller_address = 0x40
	min_pulse_width = 600 #microseconds
	max_pulse_width = 2400 #microseconds
	frequency = 60 #Hz
	turning_angle = 45

	min_duty_cycle = min_pulse_width / 1000000 * frequency
	max_duty_cycle = max_pulse_width / 1000000 * frequency
	
	def __init__(self, PCAchannel, offset = 0, debug = False):
		self.debug = debug
		self.controller = Controller(self.controller_address)
		self.PCAchannel = PCAchannel
		self.offset = offset
		
	def angle_converter(self, angle):
		if -90 <= angle <= 90:
			duty_cycle = (self.max_duty_cycle-self.min_duty_cycle)/180*angle+self.max_duty_cycle-(self.max_duty_cycle-self.min_duty_cycle)/2
			duty_cycle = int(duty_cycle*4096)
			if self.debug:
				print (debug_info, 'Angle ', angle, 'converted to ', duty_cycle)
			return duty_cycle
		else:
			duty_cycle = 0
			print ('Angle values must be between -90 and 90')
			if self.debug:
				print (debug_info, 'Exiting program due to invalid angle value')
			exit()

	def turn(self, angle):
		angle += self.offset
		duty_cycle = self.angle_converter(angle)
		self.controller.set_duty_cycle(self.PCAchannel, duty_cycle)

		if self.debug:
			print (debug_info, 'Servo connected to pin', self.PCAchannel,'in the PCA9685 is turned', angle, ' degrees')



	def turn_left(self):
		self.turn(-self.turning_angle)
		if self.debug:
			print (debug_info, 'Turning left ', self.turning_angle, 'degrees')

	def turn_right(self):
		self.turn(self.turning_angle)
		if self.debug:
			print (debug_info, 'Turning right ', self.turning_angle, 'degrees')

	def turn_straight(self):
		self.turn(0)
		if self.debug:
			print (debug_info, 'Turning straight ', 0, 'degrees')





					
if __name__ == '__main__':
	debug = True
	PCAchannel = 0

	front_wheels = Front_Wheels(PCAchannel, debug = debug)

	try:
		front_wheels.turn_straight()
		print('Turning straight')
		
		# for i in range(-90,90,5):
		# 	front_wheels.turn(i)
		# 	print('Turning to ', i)
		# 	time.sleep(0.1)

	
		while True:

			front_wheels.turn_left()
			time.sleep(1)
			print('Turning left')

			front_wheels.turn_straight()
			time.sleep(1)
			print('Turning straight')

			front_wheels.turn_right()
			time.sleep(1)
			print('Turning right')

			front_wheels.turn_straight()
			time.sleep(1)
			print('Turning straight')

	except KeyboardInterrupt:
		print (' Test interrupted by user')
		front_wheels.turn_straight()
		print ('Going back to straight wheels')




