from project.supply.supply import Supply


class Food(Supply):
    def __init__(self,name: str, energy = 25):
        super().__init__(name, energy)

# food = Food("Musaka", 23)
# print(food.details())
# food = Food("Musaka", 23)
# print(food.name)
# # food = Food("Musaka", -23)
# # print(food.details())
# food = Food("", 23)
# print(food.details())