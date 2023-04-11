from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OX_DECREASE_INCREMENT = 5

    def __init__(self, name: str, oxygen = 70):
        super().__init__(name, oxygen)

