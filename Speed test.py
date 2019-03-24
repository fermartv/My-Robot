from Wheel import Rear_Wheel
from Front_Wheels import Front_Wheels
import time


def speed_test():
    speed = 20  #Values from 0 to 100
    wait = 35
    debug = False

    left_PCAchannel = 5  #Values from 0 to 15
    left_pin = 17 #Left wheel = 17; right wheel = 27
    right_PCAchannel = 4  #Values from 0 to 15
    right_pin = 27 #Left wheel = 17; right wheel = 27
    front_PCAchannel = 0

    front_wheels = Front_Wheels(front_PCAchannel, offset = -4, debug = debug)
    left_wheel = Rear_Wheel(left_PCAchannel, left_pin, debug = debug)
    right_wheel = Rear_Wheel(right_PCAchannel, right_pin, debug = debug)

    print('Starting in 3 seconds')
    time.sleep(3)


    front_wheels.turn_straight()
    left_wheel.forward(speed)
    right_wheel.forward(speed)
    print('Moving forward for ', wait, ' seconds')
    time.sleep(wait)

    left_wheel.stop()
    right_wheel.stop()
    time.sleep(0.5)

    left_wheel.backwards(100)
    right_wheel.backwards(100)
    print('Moving backward for ', wait, ' seconds')
    time.sleep(2.5)

    left_wheel.stop()
    right_wheel.stop()
    print('Stopping')

def circle_test():
    speed = 30  #Values from 0 to 100
    debug = False

    left_PCAchannel = 5  #Values from 0 to 15
    left_pin = 17 #Left wheel = 17; right wheel = 27
    right_PCAchannel = 4  #Values from 0 to 15
    right_pin = 27 #Left wheel = 17; right wheel = 27
    front_PCAchannel = 0

    front_wheels = Front_Wheels(front_PCAchannel, offset = 0, debug = True)
    left_wheel = Rear_Wheel(left_PCAchannel, left_pin, debug = debug)
    right_wheel = Rear_Wheel(right_PCAchannel, right_pin, debug = debug)

    try:
        while True:
            front_wheels.turn_left()
            left_wheel.forward(speed)
            right_wheel.forward(speed)
            time.sleep(10)

    except KeyboardInterrupt:
        print ('Stopping wheels')
        left_wheel.stop()
        right_wheel.stop()
        front_wheels.turn_straight()
        print ('Test interrupted by user')


if __name__ == '__main__':

    circle_test()