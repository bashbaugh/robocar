from car_io import CarIO

class Robocar:
    def __init__(self):
        self.io = CarIO()
        self.actuator = self.io.actuator