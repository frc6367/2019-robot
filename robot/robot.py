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
from components.armControl import ArmControl
from components.shifter import Shifter


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
    ArmControl: ArmControl

    def createObjects(self):
        """Initialize all wpilib motors & sensors"""
        self.joystick = wpilib.Joystick(0)
        self.armUp = False
        self.drive_l1 = ctre.WPI_TalonSRX(1)
        self.drive_l2 = ctre.VictorSPX(2)
        self.drive_l3 = ctre.VictorSPX(3)
        self.drive_r1 = ctre.WPI_TalonSRX(4)
        self.drive_r2 = ctre.VictorSPX(5)
        self.drive_r3 = ctre.VictorSPX(6)

        self.elevator_motor1 = ctre.WPI_TalonSRX(7)
        self.elevator_motor2 = ctre.WPI_TalonSRX(8)

        self.arm_motor = ctre.WPI_TalonSRX(10)
        self.cargo_intake_motor = ctre.WPI_TalonSRX(11)
        self.hatch_intake_motor = ctre.WPI_TalonSRX(9)
        self.testMotor = ctre.WPI_TalonSRX(12)

        self.shiftSolenoid1 = wpilib.Solenoid(0)
        self.shiftSolenoid2 = wpilib.Solenoid(1)

        self.inMode1 = True
        # self.driveMode = True

    def teleopPeriodic(self):
        """Place code here that does things as a result of operator
           actions"""
        # self.mode()
        if self.joystick.getRawButtonReleased(1):
            self.inMode1 = not self.inMode1

        if self.inMode1 == True:
            self.mode1()
        else:
            self.mode2()

    def mode1(self):
        pass
        self.drive()
        self.armButtons()  # BUTTONS: 2
        self.hatchButtons()  # BUTTONS: 6 and 4
        self.cargoButtons()  # BUTTONS: 3 and 5

    def mode2(self):
        self.drive()
        self.elevatorButtons()  # BUTTONS: 7,9,5,8,10,6
        # self.shiftButtons()  # BUTTONS: 3 and 4

    def drive(self):
        self.drivetrain.drive(
            -self.joystick.getY() * 0.75, self.joystick.getThrottle() * 0.5
        )

    def cargoButtons(self):
        if self.joystick.getRawButton(5):
            self.cargo.setSpeed(1)
        elif self.joystick.getRawButton(3):
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
        elif self.joystick.getRawButton(5):
            self.elevatorControl.setLevel(6)
        elif self.joystick.getRawButton(8):
            self.elevatorControl.setLevel(1)
        elif self.joystick.getRawButton(10):
            self.elevatorControl.setLevel(3)
        elif self.joystick.getRawButton(6):
            self.elevatorControl.setLevel(5)

    def armButtons(self):
        if self.joystick.getRawButtonReleased(2):
            self.armUp = not self.armUp
            if self.armUp:
                self.ArmControl.setPos(1)
            else:
                self.ArmControl.setPos(0)

    def hatchButtons(self):
        if self.joystick.getRawButton(6):
            self.hatch.move(1)
        elif self.joystick.getRawButton(4):
            self.hatch.move(-1)
        else:
            self.hatch.move(0)

    def shiftButtons(self):
        if self.joystick.getRawButton(3):
            self.shifter.downShift()
        elif self.joystick.getRawButton(4):
            self.shifter.upShift()


if __name__ == "__main__":
    wpilib.run(MyRobot)
