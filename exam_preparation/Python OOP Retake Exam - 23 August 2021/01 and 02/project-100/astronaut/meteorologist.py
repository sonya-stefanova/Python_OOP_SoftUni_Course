from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    UNITS = 15

    def __init__(self, name: str, oxygen: int = 90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.UNITS
