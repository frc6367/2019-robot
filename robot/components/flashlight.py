class Flashlight:
    def setup(self):
        self.currentGear = 1

    def gearShiftUp(self):
        if self.currentGear == 1:
            self.currentGear = 2

    def gearShiftDown(self):
        if self.currentGear == 2:
            self.currentGear = 1

    def execute(self):
        pass
