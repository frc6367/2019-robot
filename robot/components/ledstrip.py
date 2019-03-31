import wpilib
from magicbot import tunable


class Ledstrip:

    blinkin: wpilib.Spark

    powerOut = tunable(0)

    def setMode(self, powerOut):
        self.powerOut = powerOut

    def execute(self):
        self.blinkin.set(self.powerOut)
