
class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.sum = 0
        self.temp = 0
    def regulator(self, diff):
        self.sum = diff + self.sum
        u = self.Kp * diff + self.Ki* self.sum + (self.temp - diff)* self.Kd
        self.temp = diff
        return u
    def setKp(self, kp):
        self.Kp = kp
    def setKi(self, ki):
        self.Ki = ki
    def setKd(self, kd):
        self.Kd =kd