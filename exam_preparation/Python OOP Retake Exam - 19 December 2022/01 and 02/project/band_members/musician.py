from abc import ABC, abstractmethod


class Musician(ABC):
    MIN_AGE = 16

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = [] #CANNOT learn a skill that is NOT in the list of available types --> children.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        ''''If the name is an empty string or contains only white spaces,
        raise a ValueError with the message: "Musician name cannot be empty!"'''
        if not value.strip():
            raise ValueError("Musician name cannot be empty!")
        self.__name = value


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        '''The musician must be at least 16 years old;
        if not - raise a ValueError with the message "Musicians should be at least 16 years old!"'''
        if value < Musician.MIN_AGE:
            raise ValueError(f"Musicians should be at least {self.MIN_AGE} years old!")
        self.__age = value

    @abstractmethod
    def learn_new_skill(self, new_skill: str):
        ...