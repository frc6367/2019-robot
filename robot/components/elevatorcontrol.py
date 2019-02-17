import wpilib
import ctre
from components.elevator import Elevator
from components.arm import Arm


class ElevatorControl:

    elevator: Elevator
    arm: Arm

    def setup(self):
        self.state = 0
        self.armState = 0

    def elevator_position_ground(self):
        # ground is always 0
        self.elevator.set_target(0)

    # Cargo is a bit higher than Hatch level
    def elevator_position_cargo1(self):
        self.elevator.set_target(2000)

    def elevator_position_cargo2(self):
        self.elevator.set_target(5500)

    def elevator_position_cargo3(self):
        self.elevator.set_target(8000)
        self.arm_position_up()

    def elevator_position_hatch1(self):
        self.elevator.set_target(1500)

    def elevator_position_hatch2(self):
        self.elevator.set_target(5000)

    def elevator_position_hatch3(self):
        self.elevator.set_target(7500)

    def arm_position_down(self):
        self.arm.setPos(1)

    def arm_position_up(self):
        self.arm.setPos(1)

    def setArmPos(self, pos):
        self.armState = pos

    def setLevel(self, state):
        self.armState = state

    def execute(self):
        # acquire button input and assign state.
        # state machine based on button input
        if self.state == 1:  # first hatch
            self.elevator_position_hatch1()
        elif self.state == 2:  # first cargo
            self.elevator_position_cargo1()
        elif self.state == 3:  # second hatch
            self.elevator_position_hatch2()
        elif self.state == 4:  # second cargo
            self.elevator_position_cargo2()
        elif self.state == 5:  # third hatch
            self.elevator_position_hatch3()
        elif self.state == 6:  # third cargo
            self.elevator_position_cargo3()
        elif self.state == 0:  # ground
            self.elevator_position_ground()
        if self.armState == 0:
            self.arm_position_down()
        elif self.armState == 1:
            self.arm_position_up()

