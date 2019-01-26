#!/usr/bin/env python3

import wpilib
from magicbot import MagicRobot
import ctre

from components.flashdrive import Drivetrain
from components.elevator import Elevator
from components.elevatorcontrol import ElevatorControl
from components.arm import Arm
from components.hatch import Hatchintake
from components.cargo import Cargo


class MyRobot(MagicRobot):

    #
    # Define components here
    #
    elevatorControl: ElevatorControl
    drivetrain: Drivetrain
    elevator: Elevator
    arm: Arm
    hatch: Hatchintake
    cargo: Cargo

    def createObjects(self):
        """Initialize all wpilib motors & sensors"""
        self.joystick = wpilib.Joystick(0)

        self.drive_l1 = ctre.WPI_TalonSRX(1)
        self.drive_l2 = ctre.WPI_TalonSRX(2)
        self.drive_l3 = ctre.WPI_TalonSRX(3)
        self.drive_r1 = ctre.WPI_TalonSRX(4)
        self.drive_r2 = ctre.WPI_TalonSRX(5)
        self.drive_r3 = ctre.WPI_TalonSRX(6)

        self.elevator_motor1 = ctre.WPI_TalonSRX(7)
        self.elevator_motor2 = ctre.WPI_TalonSRX(8)

        self.arm_motor = ctre.WPI_TalonSRX(10)
        self.cargo_intake_motor = ctre.WPI_TalonSRX(11)
        self.hatch_intake_motor = ctre.WPI_TalonSRX(9)
        self.testMotor = ctre.WPI_TalonSRX(12)

        # self.driveMode = True

    def teleopPeriodic(self):
        """Place code here that does things as a result of operator
           actions"""
        # self.mode()
        self.drive()
        self.cargoButtons()
        self.elevatorButtons()

    # def mode(self):
    #     if self.joystick.getRawButtonReleased(2):
    #         self.driveMode = not self.driveMode

    #     if self.driveMode:
    #         self.drivingMode()
    #     else:
    #         self.manipulateMode()

    def drive(self):
        self.drivetrain.drive(
            -self.joystick.getY() * 0.75, self.joystick.getThrottle() * 0.5
        )

    def cargoButtons(self):
        if self.joystick.getRawButton(6):
            self.cargo.setSpeed(1)
        elif self.joystick.getRawButton(4):
            self.cargo.setSpeed(-1)
        else:
            self.cargo.setSpeed(0)

    def elevatorButtons(self):
        if self.joystick.getRawButton(2):
            self.elevatorControl.setLevel(0)
        elif self.joystick.getRawButton(7):
            self.elevatorControl.setLevel(2)
        elif self.joystick.getRawButton(9):
            self.elevatorControl.setLevel(4)
        elif self.joystick.getRawButton(11):
            self.elevatorControl.setLevel(6)
        elif self.joystick.getRawButton(8):
            self.elevatorControl.setLevel(1)
        elif self.joystick.getRawButton(10):
            self.elevatorControl.setLevel(3)
        elif self.joystick.getRawButton(12):
            self.elevatorControl.setLevel(5)

    # def manipulateMode(self):
    #     self.arm.move(self.joystick.getY())
    #     # HATCH INTAKE
    #     if self.joystick.getRawButton(5):
    #         self.hatchintake.move(1)
    #     elif self.joystick.getRawButton(3):
    #         self.hatchintake.move(-1)
    #     else:
    #         self.hatchintake.move(0)
    #     # CARGO INTAKE
    #     if self.joystick.getRawButton(6):
    #         self.cargo.setSpeed(1)
    #     elif self.joystick.getRawButton(4):
    #         self.cargo.setSpeed(-1)
    #     else:
    #         self.cargo.stop()


if __name__ == "__main__":
    wpilib.run(MyRobot)
