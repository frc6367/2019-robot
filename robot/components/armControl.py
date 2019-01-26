import ctre
import wpilib
from components.arm import Arm


class ArmControl:

    arm: Arm

    def setup(self):
        # state machine
        self.state = 0

    def downPosition(self):
        self.arm.setPos(0)
    def upPosition(self):
        self.arm.setPos(.25)

    def setPos(self, pos):
        self.state = pos

    def execute(self):

        # aquire button input and passing state
        # state machine
        if self.state == 0:
            self.downPosition
        elif self.state == 1:
            self.upPosition
