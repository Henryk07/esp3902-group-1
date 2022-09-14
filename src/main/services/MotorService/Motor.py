class Motor:
    '''
    Constructor of Motor class
    Is executed when Motor() is called
    '''
    def __init__(self) -> None:
        pass
        
    '''
    Method to tilt the motor for a certain angle
    @params angle The angle of which the motor should tilt (positive for up, negative for down)
    '''
    def tilt(angle: float) -> None:
        pass

    '''
    Method to rotate the motor for a certain angle
    @params angle The angle of which the motor should rotate (positive for right, negative for left)
    '''
    def rotate(angle: float) -> None:
        pass

'''
To test, create a Motor object, and then call the methods

motor = Motor()

# To tilt
motor.tilt(10)

# To rotate
motor.rotate(10)
'''