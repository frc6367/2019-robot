#!/usr/bin/env python3

import wpilib
from magicbot import MagicRobot
import ctre

from components.drivetrain import Drivetrain
from components.elevator import Elevator


class MyRobot(MagicRobot):

    #
    # Define components here
    #

    drivetrain: Drivetrain
    elevator: Elevator

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

        self.hatch_intake_motor = ctre.WPI_TalonSRX(9)

    def teleopPeriodic(self):
        """Place code here that does things as a result of operator
           actions"""
        self.drivetrain.drive(self.joystick.getY(), -self.joystick.getX())


if __name__ == "__main__":
    wpilib.run(MyRobot)
