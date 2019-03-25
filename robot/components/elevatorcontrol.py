import wpilib
import ctre
from components.elevator import Elevator
from components.arm import Arm
from components.hatch import Hatchintake
import math

from magicbot import tunable


class ElevatorControl:

    elevator: Elevator
    arm: Arm
    hatch: Hatchintake

    # cimcoder is 80 per rev
    # gearbox is 12:1
    #
    kEncoderPerInch = 960 / (1.75 * math.pi)
    kGroundOffset = 19

    bottom = tunable(5)
    low = tunable(8.5)
    middle = tunable(24)
    top = tunable(36.5)

    def setup(self):
        self.state = 0
        self.armState = 0

    def on_enable(self):
        self.elevator.set_target(0 * self.kEncoderPerInch)
 
    def elevator_position_cargo_ground(self):
        # ground is always 0
        self.elevator.set_target(0 * self.kEncoderPerInch)
        self.arm.setBottom()
        self.hatch.unlock()

    # Cargo is a bit higher than Hatch level
    def elevator_position_cargo1(self):
        self.elevator.set_target(self.low * self.kEncoderPerInch)
        self.arm.setMiddle()
        self.hatch.unlock()

    def elevator_position_cargo2(self):
        self.elevator.set_target(self.middle * self.kEncoderPerInch)
        self.arm.setMiddle()
        self.hatch.unlock()

    def elevator_position_cargo3(self):
        self.elevator.set_target(self.top * self.kEncoderPerInch)
        self.arm.setMiddleTop()
        self.hatch.unlock()

    def elevator_position_hatch1(self):
        self.elevator.set_target(self.bottom * self.kEncoderPerInch)
        self.arm.setTop()
        self.hatch.lock()

    def elevator_position_hatch2(self):
        self.elevator.set_target(self.middle * self.kEncoderPerInch)
        self.arm.setTop()
        self.hatch.lock()

    def elevator_position_hatch3(self):
        self.elevator.set_target(self.top * self.kEncoderPerInch)
        self.arm.setTop()
        self.hatch.lock()

    def elevator_position_cargoBay(self):
        self.elevator.set_target(self.middle * self.kEncoderPerInch)
        self.arm.setBottom()
        self.hatch.unlock()

    def execute(self):
        pass

