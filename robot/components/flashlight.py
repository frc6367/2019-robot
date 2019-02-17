from networktables import NetworkTables
from components.flashdrive import Drivetrain


class limelight:

    drivetrain: Drivetrain

    def setup(self):
        self.table = NetworkTables.getTable("limelight")
        self.tx = self.table.getNumber("tx", 0)
        self.kP = 0.1
        self.minCommand = 0.05

    def autoAlign(self):
        if self.table.getTable("tv") != 0:
            if self.tx > 1:
                self.drivetrain.autoAlign(self.tx * self.kP - self.minCommand)
            elif self.tx < 1:
                self.drivetrain.autoAlign(self.tx * self.kP + self.minCommand)

    def execute(self):
        pass

