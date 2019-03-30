import ctre

from magicbot import feedback


class Cargo:

    cargo_intake_motor: ctre.WPI_VictorSPX

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

    def execute(self):
        self.cargo_intake_motor.set(self.speed)
