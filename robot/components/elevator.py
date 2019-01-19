import ctre


class Elevator:

    motor1: ctre.WPI_TalonSRX
    motor2: ctre.WPI_TalonSRX

    def setup(self):
        self.motor2.follow(self.motor1)

    ## Go to specific position
    def goToPosition(self, position):
        self.position = position

    def goToTop(self):
        self.goToPosition(1)

    def goToMid(self):
        self.goToPosition(2)

    def gotToBottom(self):
        self.goToPosition(3)

    ## STOP
    def stop(self):
        pass

    ## Incremental up and down
    def execute(self):
        pass
