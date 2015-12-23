import time

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
        self.leftTrack.setSpeed(self.leftTrack.speed + diffLeft)
        self.rightTrack.setSpeed(self.rightTrack.speed + diffRight)
        time.sleep(duration)
        self.leftTrack.setSpeed(self.leftTrack.speed - diffLeft)
        self.rightTrack.setSpeed(self.rightTrack.speed - diffRight)

    def _getTurnParams(self, angle):
        diffLeft = -10
        diffRight = -10
        duration = 1
        return diffLeft, diffRight, duration
