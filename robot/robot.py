#!/usr/bin/env python3

import wpilib
import ctre
import rev
from magicbot import tunable
from magicbot import MagicRobot
from networktables import NetworkTables


from robotpy_ext.common_drivers.distance_sensors import SharpIR2Y0A21
from components.flashdrive import Drivetrain
from components.elevator import Elevator
from components.elevatorcontrol import ElevatorControl

from components.arm import Arm
from components.hatch import Hatchintake
from components.cargo import Cargo
from components.shifter import Shifter
from components.ledstrip import Ledstrip
from components.flashlight import limelight


class MyRobot(MagicRobot):

    use_teleop_in_autonomous = True

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
    ledstrip: Ledstrip

    CARGO_INTAKE = 1
    CARGO_SHOOT = 2

    HATCH_CLOSED = 3
    HATCH_OPEN = 4
    HATCH_STOWED = 6

    CARGO_GROUND = 5

    CARGO_LOW = 12
    CARGO_MIDDLE = 10
    CARGO_HIGH = 8

    HATCH_LOW = 11
    HATCH_MIDDLE = 9
    HATCH_HIGH = 7

    s = tunable(0.57)
    m = tunable(1.340508)
    t = tunable(0.381021)
    b = tunable(-0.340508)
    sTwist = tunable(0.75)
    mTwist = tunable(1.56538)
    tTwist = tunable(0.54176)
    bTwist = tunable(-0.56538)
    autoEnable = tunable(True)

    def createObjects(self):
        """Initialize all wpilib motors & sensors"""
        wpilib.CameraServer.launch()
        # LiveWindow slows down the robot, and we aren't using it
        wpilib.LiveWindow.disableAllTelemetry()

        self.mainStick = wpilib.Joystick(0)
        self.extraStick = wpilib.Joystick(1)
        self.armUp = False
        self.drive_l1 = ctre.WPI_TalonSRX(1)
        self.drive_l2 = ctre.VictorSPX(2)
        self.drive_l3 = ctre.VictorSPX(3)
        self.drive_r1 = ctre.WPI_TalonSRX(4)
        self.drive_r2 = ctre.VictorSPX(5)
        self.drive_r3 = ctre.VictorSPX(6)

        self.elevator_motor1 = ctre.WPI_TalonSRX(7)

        self.arm_motor = rev.CANSparkMax(9, rev.MotorType.kBrushless)
        self.cargo_intake_motor = ctre.WPI_TalonSRX(11)
        self.hatch_intake_motor = ctre.WPI_TalonSRX(8)

        self.shiftSolenoid1 = wpilib.DoubleSolenoid(0, 1)
        self.shiftSolenoid2 = wpilib.DoubleSolenoid(3, 2)
        self.blinkin = wpilib.Spark(1)
        self.gear = 1
        self.irSensor = SharpIR2Y0A21(0)
        # self.driveMode = True

    def teleopPeriodic(self):
        """Place code here that does things as a result of operator
           actions"""
        self.drive()
        self.hatchButtons()  # LEFT BUTTONS: 6 and 4
        self.cargoButtons()  # LEFT BUTTONS: 3 and 5b
        self.elevatorButtons()  # LEFT BUTTONS: 1 AND 7 - 12
        self.shiftButtons()  # RIGHT BUTTONS: 1
        # self.autoAlign()
        # self.ledButtons()

    # def ledButtons(self):
    # if self.mainStick.getRawButton(7):
    #    self.ledstrip.setMode(-0.97)
    # pass

    # def autoAlign(self):
    # pass
    # if self.flashlight.autoCheck():
    #     self.ledstrip.setMode(0.67)
    #     if self.mainStick.getRawButton(2):
    #         self.flashlight.autoAlign()
    #         if not self.flashlight.absdistCheck():
    #             self.ledstrip.setMode(0.77)
    #         else:
    #             self.ledstrip.setMode(0.27)
    # else:
    #     self.ledstrip.setMode(0.61)

    def drive(self):
        self.drivetrain.drive(self.getYAxisDrive(), -self.getTwist())

    def getYAxisDrive(self):
        y = self.mainStick.getY()
        scale = 1
        if y < -self.t:
            return scale * (self.m * y - self.b)

        if y > -self.t and y < self.t:
            return scale * (1 / (pow(self.s, 2.0)) * pow(y, 3.0))
        else:
            return scale * (self.m * y + self.b)

    def getTwist(self):
        z = self.mainStick.getZ()
        scale = 1

        if z < -self.tTwist:
            return scale * (self.mTwist * z - self.bTwist)

        if z > -self.tTwist and z < self.tTwist:
            return scale * (1 / (pow(self.sTwist, 2.0)) * pow(z, 3.0))
        else:
            return scale * (self.mTwist * z + self.bTwist)

    def cargoButtons(self):
        if self.mainStick.getRawButton(self.CARGO_INTAKE):
            self.cargo.intake()
        elif self.mainStick.getRawButton(self.CARGO_SHOOT):  # or self.cargo.inRange():
            self.cargo.shoot()
        else:
            self.cargo.off()

    def elevatorButtons(self):
        # fmt: off
        if self.mainStick.getRawButton(self.CARGO_GROUND) or self.elevatorControl.touchButtonIntake:
            self.elevatorControl.elevator_position_cargo_ground()
        elif self.mainStick.getRawButton(self.CARGO_LOW) or self.elevatorControl.touchButtonCargoBottom:
            self.elevatorControl.elevator_position_cargo1()
        elif self.mainStick.getRawButton(self.CARGO_MIDDLE) or self.elevatorControl.touchButtonCargoMiddle:
            self.elevatorControl.elevator_position_cargo2()
        elif self.mainStick.getRawButton(self.CARGO_HIGH) or self.elevatorControl.touchButtonCargoTop:
            self.elevatorControl.elevator_position_cargo3()
        elif self.mainStick.getRawButton(self.HATCH_LOW) or self.elevatorControl.touchButtonHatchBottom:
            self.elevatorControl.elevator_position_hatch1()
        elif self.mainStick.getRawButton(self.HATCH_MIDDLE) or self.elevatorControl.touchButtonHatchMiddle or (
                self.autoEnable
                and self.cargo.isBallIn()
                and self.elevatorControl.isPositionCargoGround()
            ):
            self.elevatorControl.elevator_position_hatch2()
        elif self.mainStick.getRawButton(self.HATCH_HIGH) or self.elevatorControl.touchButtonHatchTop:
            self.elevatorControl.elevator_position_hatch3()
        elif self.extraStick.getRawButton(5) or self.elevatorControl.touchButtonCargoHab:
            self.elevatorControl.elevator_position_cargoBay()

        # fmt: on

    def hatchButtons(self):
        if self.mainStick.getRawButton(self.HATCH_CLOSED):
            self.hatch.lock()
        elif self.mainStick.getRawButton(self.HATCH_OPEN):
            self.hatch.unlock()
        elif self.mainStick.getRawButton(self.HATCH_STOWED):
            self.hatch.halfLock()

    def shiftButtons(self):
        if self.extraStick.getRawButtonPressed(1):
            self.shifter.turnOn()
            if self.gear == 1:
                self.gear = 2
                self.shifter.upShift()
            else:
                self.gear = 1
                self.shifter.downShift()

        if self.extraStick.getRawButtonReleased(1):
            self.shifter.turnOff()


if __name__ == "__main__":
    wpilib.run(MyRobot)
