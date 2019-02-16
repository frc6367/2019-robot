import ctre


class Elevator:

    motor1: ctre.WPI_TalonSRX
    motor2: ctre.WPI_TalonSRX

    def setup(self):

        # pid constants
        self.kSlotIdx = 0
        self.kPIDLoopIdx = 0
        self.kTimeoutMs = 10
        self.target1 = 0

        self.motor2.follow(self.motor1)
        # setup information for motion magic

        self.loops = 0
        self.timesInMotionMagic = 0

        # first choose the sensor
        self.motor1.configSelectedFeedbackSensor(
            ctre.WPI_TalonSRX.FeedbackDevice.CTRE_MagEncoder_Relative,
            self.kPIDLoopIdx,
            self.kTimeoutMs,
        )
        self.motor1.setSensorPhase(True)
        self.motor1.setInverted(False)

        # Set relevant frame periods to be at least as fast as periodic rate
        self.motor1.setStatusFramePeriod(
            ctre.WPI_TalonSRX.StatusFrameEnhanced.Status_13_Base_PIDF0,
            10,
            self.kTimeoutMs,
        )
        self.motor1.setStatusFramePeriod(
            ctre.WPI_TalonSRX.StatusFrameEnhanced.Status_10_MotionMagic,
            10,
            self.kTimeoutMs,
        )

        # set the peak and nominal outputs
        self.motor1.configNominalOutputForward(0, self.kTimeoutMs)
        self.motor1.configNominalOutputReverse(0, self.kTimeoutMs)
        self.motor1.configPeakOutputForward(1, self.kTimeoutMs)
        self.motor1.configPeakOutputReverse(-1, self.kTimeoutMs)

        # set closed loop gains in slot0 - see documentation */
        self.motor1.selectProfileSlot(self.kSlotIdx, self.kPIDLoopIdx)
        self.motor1.config_kF(0, 0.2, self.kTimeoutMs)
        self.motor1.config_kP(0, 0.2, self.kTimeoutMs)
        self.motor1.config_kI(0, 0, self.kTimeoutMs)
        self.motor1.config_kD(0, 0, self.kTimeoutMs)
        # set acceleration and vcruise velocity - see documentation
        self.motor1.configMotionCruiseVelocity(15000, self.kTimeoutMs)
        self.motor1.configMotionAcceleration(6000, self.kTimeoutMs)
        # zero the sensor
        self.motor1.setSelectedSensorPosition(0, self.kPIDLoopIdx, self.kTimeoutMs)

    ## Set a target position
    def set_target(self, pos):
        self.target1 = pos

    ## STOP
    def stop(self):
        pass

    ## Incremental up and down
    def execute(self):
        self.motor1.set(ctre.WPI_TalonSRX.ControlMode.MotionMagic, self.target1)

