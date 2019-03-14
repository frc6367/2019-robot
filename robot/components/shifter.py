import wpilib


class Shifter:

    shiftSolenoid1: wpilib.DoubleSolenoid
    shiftSolenoid2: wpilib.DoubleSolenoid

    def setup(self):
        self.gear = False
        self.on = False

        self.lastSolValue = wpilib.DoubleSolenoid.Value.kOff

    def upShift(self):
        self.gear = True

    def downShift(self):
        self.gear = False

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def execute(self):
        # apparently solenoids are really slow, only set them when the
        # value changes!

        if self.gear and self.on:
            solValue = wpilib.DoubleSolenoid.Value.kForward
        elif not self.gear and self.on:
            solValue = wpilib.DoubleSolenoid.Value.kReverse
        else:
            solValue = wpilib.DoubleSolenoid.Value.kOff

        if solValue != self.lastSolValue:
            self.lastSolValue = solValue
            self.shiftSolenoid1.set(solValue)
            self.shiftSolenoid2.set(solValue)
