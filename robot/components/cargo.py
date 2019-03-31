import ctre

from magicbot import feedback
from magicbot import feedback, tunable


class Cargo:

    current = tunable(0)
    smooth = tunable(0)
    alpha = tunable(0.92)
    inThreshold = tunable(11)
    cargo_intake_motor: ctre.WPI_TalonSRX

    def setup(self):
        self.speed = 0
        self.kMin = 1
        self.kMax = 4  #

    def shoot(self):
        self.speed = 1

    def intake(self):
        self.speed = -1

    def off(self):
        self.speed = 0

    def isBallIn(self):
        return self.smooth > self.inThreshold

    def execute(self):
        self.cargo_intake_motor.set(self.speed)
        self.current = self.cargo_intake_motor.getOutputCurrent()
        self.smooth = (self.alpha * self.smooth) + (1 - self.alpha) * self.current
