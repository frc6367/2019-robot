import wpilib

class Ledstrip:

    blinkin: wpilib.Spark

    def setup(self):
        self.powerOut = 1
    
    def setMode(self, powerOut):
        self.powerOut = powerOut

    def execute(self):
        self.blinkin.setPosition(self.powerOut)
