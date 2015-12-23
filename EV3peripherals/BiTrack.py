import time
from BrickPi import *

class BiTrack:
    '''

    '''

    def __init__(self, leftTrack, rightTrack):
        self.leftTrack = leftTrack
        self.rightTrack = rightTrack

    def setSpeed(self, speed=None):
        self.leftTrack.setSpeed(speed)
        self.rightTrack.setSpeed(speed)

    def turn(self, angle):
        diffLeft, diffRight, duration = self._getTurnParams(angle)
        startT = time.time()
	while True:
            result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors
            if not result:
		print ",",
	        self.leftTrack.setSpeed(self.leftTrack.speed + diffLeft)
                self.rightTrack.setSpeed(self.rightTrack.speed + diffRight)
 	    if (time.time() - startT) > duration:
                break
            time.sleep(.1)
        self.leftTrack.setSpeed(self.leftTrack.speed - diffLeft)
        self.rightTrack.setSpeed(self.rightTrack.speed - diffRight)

    def _getTurnParams(self, angle):
        diffLeft = 200
        diffRight = -200
        duration = 0.5
        return diffLeft, diffRight, duration
