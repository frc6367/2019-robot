import ctre


class Cargo:

    cargo_intake_motor: ctre.WPI_TalonSRX

    def setup(self):
        self.speed = 0
        self.enabled = True

    def setSpeed(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0
        self.enabled = False

    def execute(self):
        if self.enabled:
            self.cargo_intake_motor.set(self.speed)
