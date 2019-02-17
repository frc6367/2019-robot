import ctre
from magicbot import StateMachine, default_state, timed_state


class Hatchintake(StateMachine):

    hatch_intake_motor: ctre.WPI_TalonSRX

    def unlock(self):
        self.engage("do_unlock", True)

    def lock(self):
        self.engage("do_lock", True)

    @timed_state(duration=2.0, must_finish=True)
    def do_unlock(self):
        self.hatch_intake_motor.set(1)

    @timed_state(duration=2.0, must_finish=True, first=True)
    def do_lock(self):
        self.hatch_intake_motor.set(-1)

    @default_state()
    def stop(self):
        self.hatch_intake_motor.set(0)

