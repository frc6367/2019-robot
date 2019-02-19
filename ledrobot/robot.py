import wpilib
import random
import rev
import ctre
import wpilib.drive
import magicbot
from magicbot import MagicRobot


class Drivetrain:

    drive_l1: ctre.WPI_TalonSRX
    drive_l2: ctre.VictorSPX
    drive_l3: ctre.VictorSPX
    drive_r1: ctre.WPI_TalonSRX
    drive_r2: ctre.VictorSPX
    drive_r3: ctre.VictorSPX

    speed = magicbot.will_reset_to(0)
    rotation = magicbot.will_reset_to(0)

    def setup(self):
        self.drive_l2.follow(self.drive_l1)
        self.drive_l3.follow(self.drive_l1)
        self.drive_r2.follow(self.drive_r1)
        self.drive_r3.follow(self.drive_r1)
        self.ddrive = wpilib.drive.DifferentialDrive(self.drive_l1, self.drive_r1)

    # def on_enable(self):
    #     self.x = 0
    #     self.y = 0

    def drive(self, speed, rotation):
        self.speed = -speed
        self.rotation = -rotation

    def execute(self):
        self.ddrive.arcadeDrive(-self.speed, -self.rotation)

class MyRobot(MagicRobot):

    drivetrain: Drivetrain

    def createObjects(self):
        self.joystickR = wpilib.Joystick(0)
        self.drive_l1 = ctre.WPI_TalonSRX(1)
        self.drive_l2 = ctre.VictorSPX(2)
        self.drive_l3 = ctre.VictorSPX(3)
        self.drive_r1 = ctre.WPI_TalonSRX(4)
        self.drive_r2 = ctre.VictorSPX(5)
        self.drive_r3 = ctre.VictorSPX(6)

    def teleopPeriodic(self):
        self.drivetrain.drive(
            -self.joystickR.getY() * 0.75, self.joystickR.getX()
            
        )

    

if __name__ == "__main__":
    wpilib.run(MyRobot)
