import wpilib
import ctre
from components.elevator import Elevator
from components.arm import Arm
import math

from magicbot import tunable


class ElevatorControl:

    elevator: Elevator
    arm: Arm

    # cimcoder is 80 per rev
    # gearbox is 12:1
    #
    kEncoderPerInch = 960 / (1.75 * math.pi)
    kGroundOffset = 19

    low = tunable(10)
    middle = tunable(26)
    top = tunable(35)

    def setup(self):
        self.state = 0
        self.armState = 0

    def on_enable(self):
        self.elevator.set_target(0 * self.kEncoderPerInch)

    def elevator_position_cargo_ground(self):
        # ground is always 0
        self.elevator.set_target(0 * self.kEncoderPerInch)
        self.arm.setBottom()

    # Cargo is a bit higher than Hatch level
    def elevator_position_cargo1(self):
        self.elevator.set_target(self.low * self.kEncoderPerInch)
        self.arm.setMiddle()

    def elevator_position_cargo2(self):
        self.elevator.set_target(self.middle * self.kEncoderPerInch)
        self.arm.setMiddle()

    def elevator_position_cargo3(self):
        self.elevator.set_target(self.top * self.kEncoderPerInch)
        self.arm.setMiddleTop()

    def elevator_position_hatch1(self):
        self.elevator.set_target(self.low * self.kEncoderPerInch)
        self.arm.setTop()

    def elevator_position_hatch2(self):
        self.elevator.set_target(self.middle * self.kEncoderPerInch)
        self.arm.setTop()

    def elevator_position_hatch3(self):
        self.elevator.set_target(self.top * self.kEncoderPerInch)
        self.arm.setTop()

    def arm_position_down(self):
        # self.arm.setPos(1)
        pass

    def arm_position_up(self):
        # self.arm.setPos(1)
        pass

    def setArmPos(self, pos):
        # self.armState = pos
        pass

    def setLevel(self, state):
        # self.armState = state
        pass

    def execute(self):
        # acquire button input and assign state.
        # state machine based on button input
        # if self.state == 1:  # first hatch
        #     self.elevator_position_hatch1()
        # elif self.state == 2:  # first cargo
        #     self.elevator_position_cargo1()
        # elif self.state == 3:  # second hatch
        #     self.elevator_position_hatch2()
        # elif self.state == 4:  # second cargo
        #     self.elevator_position_cargo2()
        # elif self.state == 5:  # third hatch
        #     self.elevator_position_hatch3()
        # elif self.state == 6:  # third cargo
        #     self.elevator_position_cargo3()
        # elif self.state == 0:  # ground
        #     self.elevator_position_ground()
        # if self.armState == 0:
        #     self.arm_position_down()
        # elif self.armState == 1:
        #     self.arm_position_up()
        pass

