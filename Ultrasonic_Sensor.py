#Sources:
# - https://pimylifeup.com/raspberry-pi-distance-sensor/



import RPi.GPIO as GPIO
import time
import os

class Ultrasonic_Sensor(object):

	def __init__(self, channel, settle_time = 0.005):
		self.channel = channel
		self.settle_time = settle_time
		GPIO.setmode(GPIO.BCM)

	def get_distance(self):
		

		pulse_start_time = time.time()


		GPIO.setup(self.channel, GPIO.OUT)    
		GPIO.output(self.channel, GPIO.LOW)
		time.sleep(self.settle_time)

		GPIO.output(self.channel, GPIO.HIGH)
		time.sleep(0.00001)

		GPIO.output(self.channel, GPIO.LOW)

		GPIO.setup(self.channel, GPIO.IN)

		while GPIO.input(self.channel)==0:
			pulse_start_time = time.time()
		while GPIO.input(self.channel)==1:
			pulse_end_time = time.time()

		pulse_duration = pulse_end_time - pulse_start_time
		distance = round(pulse_duration * 17150, 2)
		#print "Distance:",distance,"cm"

		GPIO.setup(self.channel, GPIO.OUT)
		GPIO.output(self.channel, GPIO.LOW)

		return distance












def test_optimal_settle_time():
	settle_time = 0
	real_distance = 0
	f = open('Pruebas Picar/My robot/Doc/Ultrasonic_sensor_measurements_settle_time_0cm.txt', 'w')
	f.write('Settle time (s),Measured Distance (cm), Error to real distance = ' + str(real_distance) +' cm\n')
	
	while settle_time < 0.3:
		for i in range(0,3):
		# print(settle_time)
			US = Ultrasonic_Sensor(20, settle_time = settle_time)
			distance = US.get_distance()
			error = real_distance - distance
			write = str(settle_time) + ',' + str(distance) +',' +  str(error) + "\n"
			f.write(write)
			print('settle time: ', round(settle_time,4), ' Distance: ', distance, ' Error:', error)
		settle_time += 0.001


def test_distance_accuracy():
	settle_time = 0.005
	real_distance = 0
	f = open('Pruebas Picar/My robot/Doc/Ultrasonic_sensor_measurements_0cm.txt', 'w')
	f.write('Settle time (s),Measured Distance (cm), Error to real distance = ' + str(real_distance) +' cm\n')
	US = Ultrasonic_Sensor(20, settle_time = settle_time)
	for i in range (0, 100):
		distance = US.get_distance()
		error = real_distance - distance
		write = str(settle_time) + ',' + str(distance) +',' +  str(error) + "\n"
		f.write(write)
		print('settle time: ', round(settle_time,4), ' Distance: ', distance, ' Error:', error)



def test_angle_impact():

	settle_time = 0.005
	real_distance = 100
	f = open('Pruebas Picar/My robot/Doc/Ultrasonic_sensor_measurements_angle_67.5aaaa.txt', 'w')
	f.write('Settle time (s),Measured Distance (cm), Error to real distance = ' + str(real_distance) +' cm\n')
	US = Ultrasonic_Sensor(20, settle_time = settle_time)
	for i in range (0, 100):
		print(i)
		distance = US.get_distance()
		error = real_distance - distance
		write = str(settle_time) + ',' + str(distance) +',' +  str(error) + "\n"
		f.write(write)
		print('settle time: ', round(settle_time,4), ' Distance: ', distance, ' Error:', error)



if __name__ == '__main__':

	test_angle_impact()



