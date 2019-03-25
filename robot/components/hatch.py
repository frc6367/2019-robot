import ctre
from magicbot import StateMachine, default_state, timed_state
from components.arm import Arm

class Hatchintake(StateMachine):

    hatch_intake_motor: ctre.WPI_TalonSRX

    arm: Arm

    def unlock(self):
        self.engage("do_unlock", True)

    def lock(self):
        if self.arm.isArmTargetTop():
            self.engage("do_lock", True)

    def halfLock(self):
        if self.arm.isArmTargetTop():
            self.engage("do_half_lock_start", True)

    @timed_state(duration=2.0, must_finish=True)
    def do_unlock(self):
        self.hatch_intake_motor.set(1)

    @timed_state(duration=2.0, must_finish=True, first=True)
    def do_lock(self):
        self.hatch_intake_motor.set(-1)

    @timed_state(duration = .60, must_finish = True)
    def do_half_lock_end(self):
        self.hatch_intake_motor.set(1)
    @timed_state(duration=2.0, must_finish=True, next_state = do_half_lock_end)
    def do_half_lock_start(self):
        self.hatch_intake_motor.set(-1)
    @default_state()
    def stop(self):
        self.hatch_intake_motor.set(0)

