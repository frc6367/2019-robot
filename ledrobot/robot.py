import wpilib
import random
import rev
from robotpy_ext.common_drivers.distance_sensors import SharpIR2Y0A21
from magicbot import MagicRobot, tunable

class CargoAutomaion:
    sensor: SharpIR2Y0A21

    def setup(self):
        self.kMin = 1
        self.kMax = 4

    def toInches(self, cm):
        return cm * 0.393701

    def inRange(self):
        dist = self.toInches(self.sensor.getDistance())
        if dist <= self.kMax and dist >= self.kMin:
            return True
        
    def execute(self):
        pass

class Ledstrip:

    blinkin: wpilib.Spark

    powerOut = tunable(0)

    def setup(self):
        # self.blinkin.setBounds(2000,1500,1500,1500,1000)
        pass
    
    def setMode(self, powerOut):
        self.powerOut = powerOut

    def execute(self):
        self.blinkin.set(self.powerOut)

class MyRobot(MagicRobot):

    ledstrip: Ledstrip
    cargoauto: CargoAutomaion
    def createObjects(self):
        self.blinkin = wpilib.Spark(1)
        self.stick = wpilib.Joystick(0)
        self.sensor = SharpIR2Y0A21(1)

    def teleopPeriodic(self):
        self.cargoButtons()
        if self.stick.getRawButtonReleased(1):
            self.ledstrip.setMode((random.random() * 2) - 1)
    
    def cargoButtons(self):
        if self.cargoauto.inRange():
            self.ledstrip.setMode((random.random() * 2) - 1)

if __name__ == "__main__":
    wpilib.run(MyRobot)
