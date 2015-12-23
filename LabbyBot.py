
import time
from BrickPi import *
from EV3peripherals.Track import Track
from EV3peripherals.BiTrack import BiTrack
from EV3peripherals.InfraredSensor import IRSensor

class LabbyBot:
    speed = 300
    def __init__(self, **kwargs):
        BrickPiSetup()
        self.leftTrack = Track(kwargs['leftTrackPort'])
        self.rightTrack = Track(kwargs['rightTrackPort'])
        self.biTrack = BiTrack(self.leftTrack, self.rightTrack)
        self.irSensor = IRSensor(kwargs['irSensorPort'])
        BrickPiSetupSensors()

    def bringToLife(self):
        while True:
            result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors
            if not result:
                '''
                maybe move the logic later on
                '''
		print ".",
                if not self.edgeDetected():
                    self.biTrack.setSpeed(self.speed)
                else:
                    self.biTrack.setSpeed(0)
		    self.biTrack.turn(90)
                    self.biTrack.setSpeed(self.speed)
            time.sleep(.1)


    def edgeDetected(self, limit=15, nSamples=10):
	samples = []
        for i in range(nSamples):
            BrickPiUpdateValues()
            samples.append(self.irSensor.getValue() >= limit)
	return all(samples)


if __name__=='__main__':
    myRobot = LabbyBot(leftTrackPort=PORT_D, rightTrackPort=PORT_A, irSensorPort=PORT_1)
    myRobot.bringToLife()
