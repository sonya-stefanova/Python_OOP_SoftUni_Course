
class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def weight_idx(self):
        return 0.25

    @property
    def living_food(self):
        return [Meat]


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    @property
    def weight_increase(self):
        return 0.35

    @property
    def eats(self) -> list:
        return [Vegetable, Fruit, Meat, Seed]
