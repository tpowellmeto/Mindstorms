
import time
from BrickPi import *
import EV3peripherals as ev3

class LabbyBot:

    def __init__(self, **kwargs):
        BrickPiSetup()
        self.leftTrack = ev3.Track(kwargs['leftTrackPort'])
        self.rightTrack = ev3.Track(kwargs['rightTrackPort'])
        self.biTrack = ev3.BiTrack(self.leftTrack, self.rightTrack)
        self.irSensor = ev3.IRSensor(kwargs['irSensorPort'])
        BrickPiSetupSensors()

    def bringToLife(self):
        while True:
            result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors
            if not result:
                '''
                maybe move the logic later on
                '''
                if not self.edgeDetected():
                    self.biTrack.setSpeed(200)
                else:
                    self.biTrack.setSpeed(0)
            time.sleep(.1)


    def edgeDetected(self, limit=100):
        return self.irSensor.getValue() >= limit


if __name__=='__main__':
    myRobot = LabbyBot(leftTrackPort='PORT_D',rightTrackPort='PORT_A',irSensorPort='PORT_1')
    myRobot.bringToLife()