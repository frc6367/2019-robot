import wpilib


class Shifter:

    shiftSolenoid1: wpilib.Solenoid
    shiftSolenoid2: wpilib.Solenoid

    def setup(self):
        self.gear = False

    def upShift(self):
        self.gear = True

    def downShift(self):
        self.gear = False

    def execute(self):
        self.shiftSolenoid1.set(self.gear)
        self.shiftSolenoid2.set(self.gear)
