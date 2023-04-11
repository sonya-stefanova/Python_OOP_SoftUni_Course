from project.supply.supply import Supply


class Drink(Supply):
    INITIAL_ENERGY = 15
    def __init__(self,name: str):
        super().__init__(name, Drink.INITIAL_ENERGY)

# drink = Drink("CocaCola")
# print(drink.details())
# drink1 = Drink("")
# print(drink1.details())
