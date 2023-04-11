# OCP
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Dog(Animal):
    def make_sound(self):
        return "Woof"


class Chicken(Animal):
    def make_sound(self):
        return "Peow"


class Pig(Animal):
    def make_sound(self):
        return "Oich Oich"

class Owl(Animal):
    def make_sound(self):
        return "Hood Hood"

class Chicken(Animal):
    def make_sound(self):
        return "Cluck"

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken(), Pig(), Owl(), Chicken()]
animal_sound(animals)