import wpilib


class Shifter:

    shiftSolenoid1: wpilib.DoubleSolenoid
    shiftSolenoid2: wpilib.DoubleSolenoid

    def setup(self):
        self.gear = False
        self.on = False

    def upShift(self):
        self.gear = True

    def downShift(self):
        self.gear = False

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def execute(self):
        if self.gear and self.on:
            self.shiftSolenoid1.set(wpilib.DoubleSolenoid.Value.kForward)
            self.shiftSolenoid2.set(wpilib.DoubleSolenoid.Value.kForward)
        elif not self.gear and self.on:
            self.shiftSolenoid1.set(wpilib.DoubleSolenoid.Value.kReverse)
            self.shiftSolenoid2.set(wpilib.DoubleSolenoid.Value.kReverse)
        else:
            self.shiftSolenoid1.set(wpilib.DoubleSolenoid.Value.kOff)
            self.shiftSolenoid2.set(wpilib.DoubleSolenoid.Value.kOff)
