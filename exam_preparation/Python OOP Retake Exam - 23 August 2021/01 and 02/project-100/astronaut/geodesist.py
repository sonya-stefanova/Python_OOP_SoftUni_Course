from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    UNITS = 0
    def __init__(self, name: str, oxygen: int = 50):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.UNITS
