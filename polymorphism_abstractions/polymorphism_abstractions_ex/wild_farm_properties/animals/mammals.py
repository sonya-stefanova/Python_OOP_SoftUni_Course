

from project_wild_farm.food import Meat
from wild_farm_properties.animals.animal import Mammal
from wild_farm_properties.food import Fruit


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    @property
    def weight_idx(self):
        return 0.10

    @property
    def living_food(self) -> list:
        return [Vegetable, Fruit]


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    @property
    def weight_idx(self):
        return 0.40

    @property
    def living_food(self) -> list:
        return [Meat]


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    @property
    def weight_idx(self):
        return 0.30

    @property
    def living_food(self) -> list:
        return [Vegetable, Meat]


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    @property
    def weight_idx(self):
        return 1

    @property
    def living_food(self) -> list:
        return [Meat]