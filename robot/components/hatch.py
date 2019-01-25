import ctre


class Hatchintake:

    hatch_intake_motor: ctre.WPI_TalonSRX

    def setup(self):
        self.speed = 0

    def move(self, speed):
        self.speed = speed

    def execute(self):
        self.hatch_intake_motor.set(self.speed)

