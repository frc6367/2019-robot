import ctre


class Arm:

    arm_motor: ctre.WPI_TalonSRX

    def setup(self):
        self.speed = 0

    def move(self, speed):
        self.speed = speed

    def execute(self):
        self.arm_motor.set(self.speed)

    # def move(self, speed):
    #     self.arm_motor.set(speed)
