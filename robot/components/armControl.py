import ctre
import wpilib
from components.arm import Arm


class ArmControl:
    def setup(self):
        # state machine
        self.state = 0

    def setPos(self):
        pass

    def execute(self):

        # aquire button input and assing state
        # state machine
        if self.state == 0:
            pass
        elif self.state == 1:
            pass
