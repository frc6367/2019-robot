import ctre


class Arm:

    arm_motor: ctre.WPI_TalonSRX

    def setup(self):
        # Position starts at 0
        self.pos = 0

        # pid constants 
        self.kSlotIdx = 0
        self.kPIDLoopIdx = 0
        self.kTimeoutMs = 10
        self.target = 0

        self.arm_motor = ctre.WPI_TalonSRX(10)
        self.loops = 0
        self.timesInMotionMagic = 0

        # first choose the sensor
        self.arm_motor.configSelectedFeedbackSensor(
         ctre.WPI_TalonSRX.FeedbackDevice.CTRE_MagEncoder_Relative,
            self.kPIDLoopIdx,
            self.kTimeoutMs,
        )

        self.arm_motor.setSensorPhase(True)
        self.arm_motor.setInverted(False)


        # Set relevant frame periods to be at least as fast as periodic rate
        self.arm_motor.setStatusFramePeriod(
            ctre.WPI_TalonSRX.StatusFrameEnhanced.Status_13_Base_PIDF0,
            10,
            self.kTimeoutMs,
        )

        self.arm_motor.setStatusFramePeriod(
            ctre.WPI_TalonSRX.StatusFrameEnhanced.Status_10_MotionMagic,
            10,
            self.kTimeoutMs,
        )

 # set the peak and nominal outputs
        self.arm_motor.configNominalOutputForward(0, self.kTimeoutMs)
        self.arm_motor.configNominalOutputReverse(0, self.kTimeoutMs)
        self.arm_motor.configPeakOutputForward(1, self.kTimeoutMs)
        self.arm_motor.configPeakOutputReverse(-1, self.kTimeoutMs)

             # set closed loop gains in slot0 - see documentation */
        self.arm_motor.selectProfileSlot(self.kSlotIdx, self.kPIDLoopIdx)
        self.arm_motor.config_kF(0, 0.2, self.kTimeoutMs)
        self.arm_motor.config_kP(0, 0.2, self.kTimeoutMs)
        self.arm_motor.config_kI(0, 0, self.kTimeoutMs)
        self.arm_motor.config_kD(0, 0, self.kTimeoutMs)
        # set acceleration and vcruise velocity - see documentation
        self.arm_motor.configMotionCruiseVelocity(15000, self.kTimeoutMs)
        self.arm_motor.configMotionAcceleration(6000, self.kTimeoutMs)
        # zero the sensor
        self.arm_motor.setSelectedSensorPosition(0, self.kPIDLoopIdx, self.kTimeoutMs)


    def setPos(self, pos):
        # Sets the position of the Arm
        self.pos = pos

    ## STOP
    def stop(self):
        pass

    def execute(self):
        # Sends outputs to the motors
        self.arm_motor.set(ctre.WPI_TalonSRX.ControlMode.MotionMagic, self.target)