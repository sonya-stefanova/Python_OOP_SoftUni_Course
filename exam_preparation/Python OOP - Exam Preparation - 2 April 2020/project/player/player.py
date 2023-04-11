from abc import ABC, abstractmethod

from project.card.card_repository import CardRepository
from project.core.validator import Validator


class Player(ABC):

    @abstractmethod
    def __init__(self, username, health):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()  # new card repository upon initialization.

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        Validator.check_if_empty_string(value, "Player's username cannot be an empty string. ")
        self.__username = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        Validator.check_if_negative_value(value, "Player's health bonus cannot be less than zero. ")
        self.__health = value

    @property
    def is_dead(self):
        return self.health < 0

    def take_damage(self, damage_points:int):
        # The take_damage method decreases players' health with the damage points.
        # If the damage_points are below 0 raise a ValueError with message "Damage points cannot be less than zero."
        if damage_points<0:
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points

    def __str__(self):
        return f'Username: {self.username} - Health: {self.health} - Cards {", ".join(self.card_repository.count)}'