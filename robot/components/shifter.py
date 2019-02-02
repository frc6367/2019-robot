import wpilib


class Shifter:

    shiftSolenoid1: wpilib.Solenoid
    shiftSolenoid2: wpilib.Solenoid

    def setup(self):
        self.gear = 0
        self.shiftSolenoid2.follow(self.shiftSolenoid1)

    def upShift(self):
        self.gear = 1

    def downShift(self):
        self.gear = 0

    def execute(self):
        self.shiftSolenoid1.set(self.gear)
