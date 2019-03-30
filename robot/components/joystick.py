import wpilib

class Joystick():
    mainStick: wpilib.Joystick

    def setup(self):
        self.s = 0.57
        self.m = 1.340508
        self.t = 0.381021
        self.b = -0.340508
        self.sTwist = 0.75
        self.mTwist = 1.56538
        self.tTwist = 0.54176
        self.bTwist = -0.56538

    def getRawAxis(self):
        y = self.mainStick.getY()
        scale = 1

        if y < -self.t:
            return scale * (self.m * y - self.b)
    
        if y > -self.t and y < self.t:
            return scale * (1 / (pow(self.s,2.0)) * pow(y,3.0))
        else:
            return scale * (self.m * y + self.b)



    def getTwist(self):
        z = self.mainStick.getZ()
        scale = 1

        if z < -self.tTwist:
            return scale * (self.mTwist * z - self.bTwist)

        if z > -self.tTwist and z < self.tTwist:
            return scale * (1 / (pow(self.sTwist,2.0)) * pow(z,3.0))
        else:
            return scale * (self.mTwist * z + self.bTwist)
    def execute(self):
        pass
  