#!/usr/bin/env python3

import rev
import wpilib

from robotpy_ext.common_drivers.distance_sensors import SharpIR2Y0A21


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.arm_motor = rev.CANSparkMax(9, rev.MotorType.kBrushless)
        self.stick = wpilib.Joystick(0)

        # self.thing = SharpIR2Y0A21(0)

        self.arm_motor.restoreFactoryDefaults()
        self.arm_pidController = self.arm_motor.getPIDController()
        self.arm_encoder = self.arm_motor.getEncoder()

        self.kP = 0.1
        self.kI = 0
        self.kD = 0
        self.kMaxOutput = 0.3
        self.kMinOutput = -0.2

        self.arm_pidController.setP(self.kP)
        self.arm_pidController.setI(self.kI)
        self.arm_pidController.setD(self.kD)
        self.arm_pidController.setOutputRange(self.kMinOutput, self.kMaxOutput)

        self.arm_encoder.setPosition(0.0)

    def disabledPeriodic(self):
        # wpilib.SmartDashboard.putNumber("thing", self.thing.getDistance())
        wpilib.SmartDashboard.putNumber("encoder", self.arm_encoder.getPosition())

    def teleopPeriodic(self):
        # self.arm_motor.set(self.stick.getY())
        wpilib.SmartDashboard.putNumber("encoder", self.arm_encoder.getPosition())
        # wpilib.SmartDashboard.putNumber("thing", self.thing.getDistance())

        if self.stick.getRawButton(12):
            self.arm_pidController.setReference(-3.0, rev.ControlType.kPosition)
        elif self.stick.getRawButton(11):
            self.arm_pidController.setReference(-9.0, rev.ControlType.kPosition)
        elif self.stick.getRawButton(10):
            self.arm_pidController.setReference(-1.0, rev.ControlType.kPosition)


if __name__ == "__main__":
    wpilib.run(MyRobot)
