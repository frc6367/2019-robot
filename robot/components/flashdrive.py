import ctre
import wpilib.drive
import magicbot


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
        self.ddrive.arcadeDrive(self.speed, self.rotation)
