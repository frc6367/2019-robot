import ctre


class Cargo:

    cargo_intake_motor: ctre.WPI_TalonSRX
    self.joy = wpilib.Joystick(0)

    self.loops = 0
    self.timesInMotionMagic = 0

    # first choose the sensor
    self.cargo_intake_motor.configSelectedFeedbackSensor(
        WPI_TalonSRX.FeedbackDevice.CTRE_MagEncoder_Relative,
        self.kPIDLoopIdx,
        self.kTimeoutMs,
    )
    self.cargo_intake_motor.setSensorPhase(True)
    self.cargo_intake_motor.setInverted(False)

    # Set relevant frame periods to be at least as fast as periodic rate
    self.cargo_intake_motor.setStatusFramePeriod(
        WPI_TalonSRX.StatusFrameEnhanced.Status_13_Base_PIDF0, 10, self.kTimeoutMs
    )
    self.cargo_intake_motor.setStatusFramePeriod(
        WPI_TalonSRX.StatusFrameEnhanced.Status_10_MotionMagic, 10, self.kTimeoutMs
    )

    # set the peak and nominal outputs
    self.cargo_intake_motor.configNominalOutputForward(0, self.kTimeoutMs)
    self.cargo_intake_motor.configNominalOutputReverse(0, self.kTimeoutMs)
    self.cargo_intake_motor.configPeakOutputForward(1, self.kTimeoutMs)
    self.cargo_intake_motor.configPeakOutputReverse(-1, self.kTimeoutMs)

    # set closed loop gains in slot0 - see documentation */
    self.cargo_intake_motor.selectProfileSlot(self.kSlotIdx, self.kPIDLoopIdx)
    self.cargo_intake_motor.config_kF(0, 0.2, self.kTimeoutMs)
    self.cargo_intake_motor.config_kP(0, 0.2, self.kTimeoutMs)
    self.cargo_intake_motor.config_kI(0, 0, self.kTimeoutMs)
    self.cargo_intake_motor.config_kD(0, 0, self.kTimeoutMs)
    # set acceleration and vcruise velocity - see documentation
    self.cargo_intake_motor.configMotionCruiseVelocity(15000, self.kTimeoutMs)
    self.cargo_intake_motor.configMotionAcceleration(6000, self.kTimeoutMs)
    # zero the sensor
    self.cargo_intake_motor.setSelectedSensorPosition(
        0, self.kPIDLoopIdx, self.kTimeoutMs
    )

    def setup(self):
        self.speed = 0

    def setSpeed(self, speed):
        self.speed = speed

    def execute(self):
        self.cargo_intake_motor.set()
