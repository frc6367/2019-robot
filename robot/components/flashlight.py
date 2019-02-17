from networktables import NetworkTables
from components.flashdrive import Drivetrain


class limelight:

    drivetrain: Drivetrain

    def setup(self):
        self.table = NetworkTables.getTable("limelight")
        self.kP = 0.1
        self.minCommand = 0.05

    def autoAlign(self):
        tx = self.table.getNumber("tx", 0)
        if self.table.getNumber("tv", 0) != 0:
            if tx > 1:
                self.drivetrain.autoAlign(tx * self.kP - self.minCommand)
            elif tx < 1:
                self.drivetrain.autoAlign(tx * self.kP + self.minCommand)

    def execute(self):
        pass

