import ctre


class Arm:

    arm_motor: ctre.WPI_TalonSRX

    def setup(self):
        # Position starts at 0
        self.pos = 0

    def setPos(self, pos):
        # Sets the position of the Arm
        self.pos = pos

    def execute(self):
        # Sends outputs to the motors
        self.arm_motor.set()

    # def move(self, speed):
    #     self.arm_motor.set(speed)
