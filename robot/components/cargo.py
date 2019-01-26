import ctre


class Cargo:

    cargo_intake_motor: ctre.WPI_TalonSRX

    def setup(self):
        self.speed = 0

    def setSpeed(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def execute(self):
        self.cargo_intake_motor.set(self.speed)
