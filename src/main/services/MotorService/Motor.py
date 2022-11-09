import Jetson.GPIO as GPIO
import time
from datetime import datetime, timedelta
'''
add a function to only allow the motor get input with one sec
'''
class Motor:
    '''
    Constructor of Motor class
    Is executed when Motor() is called
    '''
    def __init__(self) -> None:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.output_pin_rotate = 32
        self.output_pin_tilt = 33
        self.rotate_angle = 0.0
        self.tilt_angle = 0.0
        
        # Reset the angular orientation of the motor
        self.tilt(0.0)
        self.rotate(0.0)        

    '''
    Method to tilt the motor to a certain angle
    @params angle The angle of which the motor should tilt to
    '''
    def tilt(self, angle: float) -> None:
        self.__execute(angle, self.output_pin_tilt) 
        self.tilt_angle = angle

    '''
    Method to rotate the motor to a certain angle
    @params angle The angle of which the motor should rotate to
    '''
    def rotate(self, angle: float) -> None:
        self.__execute(angle, self.output_pin_rotate) 
        self.rotate_angle = angle

    def __execute(self, angle: float, port_number: int) -> None:
        GPIO.setup(port_number, GPIO.OUT, initial=GPIO.HIGH)
        period = 20 # ms

        mode = 0
        GPIO.output(port_number, GPIO.LOW)

        MIN_DUTY, MAX_DUTY = 2.5, 12.5 # Percentage range

        test_time = 0.25
        up_time = period * (angle / 180 * (MAX_DUTY-MIN_DUTY) + MIN_DUTY) / 100 # ms
        down_time = period - up_time # ms

        next_time = datetime.now() + timedelta(seconds = down_time/1000)
        end_time = datetime.now() + timedelta(seconds = test_time)
        while datetime.now() <= end_time:
                if datetime.now() >= next_time:
                       if mode == 0: 
                                mode = 1
                                GPIO.output(port_number, GPIO.HIGH)
                                next_time += timedelta(seconds = up_time/1000)
                       else:
                                mode = 0
                                GPIO.output(port_number, GPIO.LOW)
                                next_time += timedelta(seconds = down_time/1000)
        

'''
To test, create a Motor object, and then call the methods

motor = Motor()

# To tilt
motor.tilt(10)

# To rotate
motor.rotate(10)
'''
