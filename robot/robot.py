#!/usr/bin/env python3

import wpilib
import ctre
import rev
from magicbot import MagicRobot
from networktables import NetworkTables

from components.flashdrive import Drivetrain
from components.elevator import Elevator
from components.elevatorcontrol import ElevatorControl
from components.arm import Arm
from components.hatch import Hatchintake
from components.cargo import Cargo
from components.shifter import Shifter

from components.flashlight import limelight


class MyRobot(MagicRobot):

    #
    # Define components here
    #
    shifter: Shifter
    elevatorControl: ElevatorControl
    drivetrain: Drivetrain
    elevator: Elevator
    arm: Arm
    hatch: Hatchintake
    cargo: Cargo
    flashlight: limelight

    def createObjects(self):
        """Initialize all wpilib motors & sensors"""
        self.joystickR = wpilib.Joystick(0)
        self.joystickL = wpilib.Joystick(1)
        self.armUp = False
        self.drive_l1 = ctre.WPI_TalonSRX(1)
        self.drive_l2 = ctre.VictorSPX(2)
        self.drive_l3 = ctre.VictorSPX(3)
        self.drive_r1 = ctre.WPI_TalonSRX(4)
        self.drive_r2 = ctre.VictorSPX(5)
        self.drive_r3 = ctre.VictorSPX(6)

        self.elevator_motor1 = ctre.WPI_TalonSRX(7)

        self.arm_motor = rev.CANSparkMax(9, rev.MotorType.kBrushless)
        self.cargo_intake_motor = ctre.WPI_TalonSRX(8)
        self.hatch_intake_motor = ctre.WPI_TalonSRX(9)
        self.testMotor = ctre.WPI_TalonSRX(12)

        self.shiftSolenoid1 = wpilib.DoubleSolenoid(0, 1)
        self.shiftSolenoid2 = wpilib.DoubleSolenoid(2, 3)

        self.gear = 1
        # self.driveMode = True

    def teleopPeriodic(self):
        """Place code here that does things as a result of operator
           actions"""
        # self.mode()
        self.drive()
        self.armButtons()  # LEFT BUTTONS: 2
        self.hatchButtons()  # LEFT BUTTONS: 6 and 4
        self.cargoButtons()  # LEFT BUTTONS: 3 and 5
        self.drive()  # RIGHT JOYSTICK
        self.elevatorButtons()  # LEFT BUTTONS: 1 AND 7 - 12
        self.shiftButtons()  # RIGHT BUTTONS: 1
        self.autoAlign()

    def autoAlign(self):
        if self.joystickR.getRawButton(2):
            self.flashlight.autoAlign()

    def drive(self):
        self.drivetrain.drive(
            -self.joystickR.getY() * 0.75, self.joystickR.getX() * 0.5
        )

    def cargoButtons(self):
        if self.joystickL.getRawButton(5):
            self.cargo.setSpeed(1)
        elif self.joystickL.getRawButton(3):
            self.cargo.setSpeed(-1)
        else:
            self.cargo.setSpeed(0)

    def elevatorButtons(self):
        if self.joystickL.getRawButton(1):
            self.elevatorControl.setLevel(0)
        elif self.joystickL.getRawButton(7):
            self.elevatorControl.setLevel(2)
        elif self.joystickL.getRawButton(9):
            self.elevatorControl.setLevel(4)
        elif self.joystickL.getRawButton(11):
            self.elevatorControl.setLevel(6)
        elif self.joystickL.getRawButton(8):
            self.elevatorControl.setLevel(1)
        elif self.joystickL.getRawButton(10):
            self.elevatorControl.setLevel(3)
        elif self.joystickL.getRawButton(12):
            self.elevatorControl.setLevel(5)

    def armButtons(self):
        if self.joystickL.getRawButtonReleased(2):
            self.armUp = not self.armUp
            if self.armUp:
                self.elevatorControl.setArmPos(100)
            else:
                self.elevatorControl.setArmPos(0)

    def hatchButtons(self):
        if self.joystickL.getRawButton(6):
            self.hatch.move(1)
        elif self.joystickL.getRawButton(4):
            self.hatch.move(-1)
        else:
            self.hatch.move(0)

    def shiftButtons(self):
        if self.joystickR.getRawButtonPressed(1):
            self.shifter.turnOn()
            if self.gear == 1:
                self.gear = 2
                self.shifter.upShift()
            else:
                self.gear = 1
                self.shifter.downShift()

        if self.joystickR.getRawButtonReleased(1):
            self.shifter.turnOff()


if __name__ == "__main__":
    wpilib.run(MyRobot)
