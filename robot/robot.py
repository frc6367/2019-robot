#!/usr/bin/env python3

import wpilib
from magicbot import MagicRobot


class MyRobot(MagicRobot):

    #
    # Define components here
    #

    def createObjects(self):
        """Initialize all wpilib motors & sensors"""

        self.joystick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        """Place code here that does things as a result of operator
           actions"""


if __name__ == "__main__":
    wpilib.run(MyRobot)
