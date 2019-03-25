import wpilib
import rev

from magicbot import feedback, tunable


class Arm:

    arm_motor: rev.CANSparkMax

    top = tunable(0)
    middle = tunable(-8.8)
    bottom = tunable(-15.0)
    middle_top = tunable(-7.0)

    def setup(self):
        self.target = None
        self.arm_motor.setIdleMode(rev.IdleMode.kBrake)
        self.arm_motor.restoreFactoryDefaults()
        self.arm_pidController = self.arm_motor.getPIDController()
        self.arm_encoder = self.arm_motor.getEncoder()

        self.kP = 0.2
        self.kI = 0
        self.kD = 0.01
        self.kMaxOutput = 0.3
        self.kMinOutput = -0.2

        self.arm_pidController.setP(self.kP)
        self.arm_pidController.setI(self.kI)
        self.arm_pidController.setD(self.kD)
        self.arm_pidController.setOutputRange(self.kMinOutput, self.kMaxOutput)

        self.arm_encoder.setPosition(0.0)

    @feedback
    def encoder(self):
        return self.arm_encoder.getPosition()

    def setTop(self):
        self.target = self.top

    def setMiddle(self):
        self.target = self.middle

    def setMiddleTop(self):
        self.target = self.middle_top

    def setBottom(self):
        self.target = self.bottom

    def isArmTargetTop(self):
        return self.target == self.top

    ## STOP
    def stop(self):
        self.target = None

    def execute(self):
        # Sends outputs to the motors
        if self.target is None:
            self.arm_motor.set(0)
        else:
            self.arm_pidController.setReference(self.target, rev.ControlType.kPosition)

