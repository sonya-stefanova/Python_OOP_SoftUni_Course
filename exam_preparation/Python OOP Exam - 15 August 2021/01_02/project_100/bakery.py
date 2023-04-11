from project_100.baked_food.bread import Bread
from project_100.baked_food.cake import Cake
from project_100.drink.tea import Tea
from project_100.drink.water import Water
from project_100.table.inside_table import InsideTable
from project_100.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def __find_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def __find_food(self, name):
        food = [f for f in self.food_menu if f.name == name]

    def __find_drink(self, drink_name):
        drink = [d for d in self.drinks_menu if d.name == drink_name]


    @staticmethod
    def food_factory(food_type: str, name: str, price: float):
        food = None
        if food_type == "Bread":
            food = Bread(name, price)
        elif food_type == "Cake":
            food = Cake(name, price)
        return food

    @staticmethod
    def drink_factory(drink_type, name, portion, brand):
        drink = None
        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
        elif drink_type == "Water":
            drink = Water(name, portion, brand)
        return drink

    @staticmethod
    def table_factory(table_type, table_number, capacity):
        table = None
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
        return table

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):

        if self.__find_food(name):
            raise Exception(f"{food_type} {name} is already in the menu!")
        food = self.food_factory(food_type, name, price)
        self.food_menu.append(food)
        return f"Added {food.name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if self.__find_drink(name):
            raise Exception(f"{drink_type} {name} is already in the menu!")
        drink = self.drink_factory(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if self.__find_table(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")
        table = self.table_factory(table_type, table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: []):
        table = self.__find_table(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_food = f"Table {table_number} ordered:\n"
        skipped_order = f"{self.name} does not have in the menu:\n"

        for food_name in food_names:
            food = self.__find_food(food_name)
            if food is None:
                skipped_order += food_name + '\n'
            else:
                table.order_food(food)
                ordered_food += str(food) + '\n'

        return ordered_food + skipped_order.strip()

    def order_drink(self, table_number: int, *drink_names: []):
        table = self.__find_table(table_number)
        if table is None:
            return f'Could not find table {table_number}'

        ordered_drinks = f'Table {table_number} ordered:\n'
        skipped_order_drinks = f'{self.name} does not have in the menu:\n'

        for drink_name in drink_names:
            drink = self.__find_drink(drink_name)

            if drink is None:
                skipped_order_drinks += drink_name + '\n'
            else:
                table.order_drink(drink)
                ordered_drinks += str(drink) + '\n'

        return ordered_drinks + skipped_order_drinks.strip()

    def leave_table(self, table_number: int):
        table = self.__find_table(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {table_bill:.2f}"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())
        return '\n'.join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
