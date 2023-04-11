from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OX_DECREASE_INCREMENT = 15

    def __init__(self, name: str, oxygen = 90):
        super().__init__(name, oxygen)
