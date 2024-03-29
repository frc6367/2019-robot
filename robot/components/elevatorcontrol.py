import wpilib
import ctre
from components.cargo import Cargo
from components.elevator import Elevator
from components.arm import Arm
from components.hatch import Hatchintake
import math
from magicbot import StateMachine, default_state, timed_state, state

from magicbot import tunable


class ElevatorControl(StateMachine):

    cargo: Cargo
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

    touchButtonCargoBottom = tunable(False)
    touchButtonCargoMiddle = tunable(False)
    touchButtonCargoTop = tunable(False)
    touchButtonHatchBottom = tunable(False)
    touchButtonHatchMiddle = tunable(False)
    touchButtonHatchTop = tunable(False)
    touchButtonIntake = tunable(False)
    touchButtonCargoHab = tunable(False)

    def setup(self):
        self.state = 0
        self.armState = 0

        self.armPos = None
        self.elevatorTarget = None

    def on_enable(self):
        self.elevator.set_target(0 * self.kEncoderPerInch)

    def elevator_position_cargo_ground(self):
        # ground is always 0
        self._start_control(0, self.arm.setBottom, self.hatch.unlock, False)
        self.touchButtonIntake = False

    def isPositionCargoGround(self):
        return self.elevatorTarget == 0 and self.armPos == self.arm.setBottom

    # Cargo is a bit higher than Hatch level
    def elevator_position_cargo1(self):
        self._start_control(self.low, self.arm.setMiddle, self.hatch.unlock, False)
        self.touchButtonCargoBottom = False

    def elevator_position_cargo2(self):
        self._start_control(self.middle, self.arm.setMiddle, self.hatch.unlock, False)
        self.touchButtonCargoMiddle = False

    def elevator_position_cargo3(self):
        self._start_control(self.top, self.arm.setMiddleTop, self.hatch.unlock, False)
        self.touchButtonCargoTop = False

    def elevator_position_hatch1(self):
        self._start_control(self.bottom, self.arm.setTop, self.hatch.lock, False)
        self.touchButtonHatchBottom = False

    def elevator_position_hatch2(self):
        self._start_control(self.middle, self.arm.setTop, self.hatch.lock, True)
        self.touchButtonHatchMiddle = False

    def elevator_position_hatch3(self):
        self._start_control(self.top, self.arm.setTop, self.hatch.lock, False)
        self.touchButtonHatchTop = False

    def elevator_position_cargoBay(self):
        self._start_control(self.middle, self.arm.setBottom, self.hatch.unlock, True)
        self.touchButtonCargoHab = False

    def _start_control(self, elevatorTarget, armPos, hatchState, delay):
        # Only begin control IFF it wasn't asked for
        elevatorTarget = elevatorTarget * self.kEncoderPerInch
        if self.armPos == armPos and self.elevatorTarget == elevatorTarget:
            return

        hatchState()
        self.armPos = armPos
        self.elevatorTarget = elevatorTarget

        if not delay:
            self.elevator.set_target(self.elevatorTarget)
            armPos()

        # IF GOING DOWN
        elif self.elevator.target1 > elevatorTarget:
            self.engage("moveArmFirst", True)
        # Otherwise going up
        else:
            self.engage("moveElevatorFirst", True)

    @timed_state(duration=0.25, must_finish=True, next_state="moveElevatorSecond")
    def moveArmFirst(self):
        self.armPos()

    @state(must_finish=True)
    def moveElevatorSecond(self):
        self.elevator.set_target(self.elevatorTarget)

    @timed_state(duration=0.25, must_finish=True, next_state="moveArmSecond")
    def moveElevatorFirst(self):
        # Assume intake only happens when going up
        self.cargo.intake()
        self.elevator.set_target(self.elevatorTarget)

    @state(must_finish=True)
    def moveArmSecond(self):
        self.armPos()

    @state(first=True)
    def ignored(self):
        pass
