from abc import ABC, abstractmethod


class Astronaut(ABC):
    UNITS = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    @abstractmethod
    def breathe(self):
        self.oxygen -= self.UNITS
