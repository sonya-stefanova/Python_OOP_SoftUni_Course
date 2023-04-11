from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    INCREASE_INCREMENT = 1

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, 7)

    def eating(self):
        self.weight+=FemaleRobot.INCREASE_INCREMENT

#
# female = FemaleRobot("Female", "female", 15)
# female.eating()
# female.eating()
# print(female.weight)