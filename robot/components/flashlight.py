from networktables import NetworkTables
from components.flashdrive import Drivetrain


class limelight:

    drivetrain: Drivetrain

    def setup(self):
        self.table = NetworkTables.getTable("limelight")
        self.kP = 0.1
        self.minCommand = 0.05
        self.tx = 0

    def autoCheck(self):
        return self.table.getNumber("tv", 0) != 0

    def distCheck(self):
        return self.tx > 1

    def absdistCheck(self):
        return abs(self.tx) > 3

    def autoAlign(self):
        self.tx = self.table.getNumber("tx", 0)
        if self.autoCheck:
            if self.distCheck():
                self.drivetrain.autoAlign(self.tx * self.kP - self.minCommand)
            elif not self.distCheck():
                self.drivetrain.autoAlign(self.tx * self.kP + self.minCommand)

    def execute(self):
        pass
