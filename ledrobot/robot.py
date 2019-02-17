import wpilib
import random
import rev
from magicbot import MagicRobot, tunable

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

    def createObjects(self):
        self.blinkin = wpilib.Spark(1)
        self.stick = wpilib.Joystick(0)
        self.sensor = wpilib.AnalogInput(1)

    def teleopPeriodic(self):
        if self.stick.getRawButtonReleased(1):
            self.ledstrip.setMode((random.random() * 2) - 1)

if __name__ == "__main__":
    wpilib.run(MyRobot)
