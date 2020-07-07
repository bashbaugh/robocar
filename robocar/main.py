from car_io import CarIO
from web_interface import WebInterface
from logger import logger

class Robocar:
    def __init__(self):
        logger.debug("Starting Robocar")

        self.io = CarIO()
        self.actuator = self.io.actuator

        self.webi = WebInterface()

car = Robocar()