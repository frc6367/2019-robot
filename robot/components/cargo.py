import ctre
from robotpy_ext.common_drivers.distance_sensors import SharpIR2Y0A21

from magicbot import feedback

class Cargo:

    cargo_intake_motor: ctre.WPI_TalonSRX
    irSensor: SharpIR2Y0A21

    def setup(self):
        self.speed = 0
        self.enabled = True
        self.kMin = 1
        self.kMax = 4  #
    
    @feedback
    def ball_distance(self):
        return self.irSensor.getDistance() * 0.393701

    def inRange(self):
        dist = self.ball_distance()
        return dist <= self.kMax and dist >= self.kMin
        
    def forward(self):
        self.speed = 1
    
    def reverse(self):
        self.speed = -1
    
    def off(self):
        self.speed = 0


    def execute(self):
        if self.enabled:
            self.cargo_intake_motor.set(self.speed)
