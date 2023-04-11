from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INCREASE_INCREMENT = 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, 9)

    def eating(self):
        self.weight+=MaleRobot.INCREASE_INCREMENT

# male = MaleRobot("Male", "male", 15)
# male.eating()
# male.eating()
# print(male.weight)
# male = MaleRobot("   ", "male", 15)
# print(male.name)