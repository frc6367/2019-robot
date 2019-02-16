import wpilib
import rev

class Arm:

    arm_motor: rev.CANSparkMax

    def setup(self):
        self.target = 0

        self.arm_motor.restoreFactoryDefaults()
        self.arm_pidController = self.arm_motor.getPIDController()
        self.arm_encoder = self.arm_motor.getEncoder()

        self.kP = 0.1
        self.kI = 0
        self.kD = 0
        self.kMaxOutput = 1
        self.kMinOutput = 0

        self.arm_pidController.setP(self.kP)
        self.arm_pidController.setI(self.kI)
        self.arm_pidController.setD(self.kD)
        self.arm_pidController.setOutputRange(self.kMinOutput, self.kMaxOutput)

    def setPos(self, pos):
        # Sets the position of the Arm
        self.target = pos

    ## STOP
    def stop(self):
        pass

    def execute(self):
        # Sends outputs to the motors

        self.arm_pidController.setReference(self.target, rev.ControlType.kPosition)

    # def move(self, speed):
    #     self.arm_motor.set(speed)

