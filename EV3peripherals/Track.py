from BrickPi import *


class Track:
    '''

    '''

    def __init__(self, port):
        self.port = port
        BrickPi.MotorEnable[port] = 1

    def setSpeed(self, speed=200):
        self.speed = speed
        BrickPi.MotorSpeed[self.port] = speed