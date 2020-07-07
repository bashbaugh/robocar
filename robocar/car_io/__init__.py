from .actuator import Actuator
from logger import logger

class CarIO:
    def __init__(self):
        logger.debug("Connecting to IO board")
        self.actuator = Actuator(self)

    def _send_message(self, message):
        pass