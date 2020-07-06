from actuator import Actuator

class CarIO:
    def __init__(self):
        self.actuator = Actuator(self)

    def _send_message(self, message):
        pass