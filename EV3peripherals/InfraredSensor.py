from BrickPi import *

class IRSensor:

    def __init__(self, port):
        self.port = port
        BrickPi.SensorType[port] = TYPE_SENSOR_EV3_INFRARED_M0

    def getValue(self):
        return BrickPi.Sensor[self.port]