from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:

    VALID_FOOD = {
        "Bread": Bread,
         "Cake": Cake
    }

    VALID_DRINKS = {
        "Tea":Tea,
        "Water": Water
    }

    VALID_TABLES = {
        "InsideTable":InsideTable,
        "OutsideTable":OutsideTable
    }


    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def find_food(self, name):
        food = next(filter(lambda x: x.name == name, self.food_menu), None)
        return food

    def find_drink(self, name):
        return next(filter(lambda x: x.name == name, self.drinks_menu), None)

    def find_table(self, number):
        return next(filter(lambda x: x.table_number == number, self.tables_repository), None)

    def add_food(self, food_type: str, name: str, price: float):
        """Creates a food with the correct type and adds it to the menu.
        The possible types of food are "Bread" and "Cake". If the food is created and added successfully, returns:
"Added {baked_food_name} ({baked_food_type}) to the food menu"
If a baked food with the given name already exists in the food menu,
raise an Exception with message "{food_type} {name} is already in the menu!"
"""
        if name in [f.name for f in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = self.VALID_FOOD[food_type](name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        """Creates a drink with the correct type and adds it to the menu.
        If the drink is created and added successfully, returns:
"Added {drink_name} ({drink_brand}) to the drink menu"
If a drink with the given name already exists in the drink menu, raise Exception with the message
"{drink_type} {name} is already in the menu!"
"""
        if any(d.name == name for d in self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = self.VALID_DRINKS[drink_type](name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        """Creates a table with the correct type, adds it to the table repository.
        The possible types of tables are "InsideTable" and "OutsideTable".
        If the table is created and added successfully, returns:
            "Added table number {table_number} in the bakery"
        If a table with the given number already exists in the table repository,
        raise Exception with the message "Table {table_number} is already in the bakery!"
"""
        if table_number in [t.table_number for t in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = self.VALID_TABLES[table_type](table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        """Finds the first possible table which is not reserved,
        and its capacity is enough for the number of people provided.
        Then reserves the table and returns:
        "Table {table_number} has been reserved for {number_of_people} people"
        Otherwise, returns:
        "No available table for {number_of_people} people"
"""
        try:
            table = next(filter(lambda t: not t.is_reserved and t.capacity >= number_of_people,
                                     self.tables_repository))
        except StopIteration:
            return f'No available table for {number_of_people} people'

        table.reserve(number_of_people)
        return f'Table {table.table_number} has been reserved for {number_of_people} people'



    def order_food(self, table_number: int, *food_names: []):
        """The order_food method will receive a table's number and a different number of strings with food's names.
            Finds the table with that number. If there is no such table returns:
            "Could not find table {table_number}"
        Otherwise, adds the food which could be ordered (are in the menu) in the table's orders,
        returns the information about the ordered food and the food that is not in the menu in the format:
"""
        current_table = self.get_table(table_number)
        if not current_table:
            return f'Could not find table {table_number}'
        food_in_menu = []
        food_not_in_menu = []
        for food_name in food_names:
            food = self.find_food(food_name)
            if food:
                food_in_menu.append(food.__repr__())
                current_table.food_orders.append(food)
            else:
                food_not_in_menu.append(food_name)
                current_table.foods_that_cannot_be_ordered.append(food_name)

        display_list = [f'Table {table_number} ordered:', *food_in_menu,
                        f'{self.name} does not have in the menu:', *food_not_in_menu]
        return "\n".join(display_list)


    def order_drink(self, table_number: int, *drink_names: []):
        """The order_drink method will receive a table's number and different number of strings with drink's names.
        Finds the table with that number. If there is no such table, it returns:
        "Could not find table {table_number}"
        Otherwise, adds the drinks which could be ordered (are in the menu) in the table's orders, returns orders of the drinks which are in the menu and the ones that are not:
"""
        current_table = self.find_table(table_number)
        if not current_table:
            return f'Could not find table {table_number}'
        drinks_in_menu = []
        drinks_not_in_menu = []
        for drink_name in drink_names:
            drink = self.find_drink(drink_name)
            if drink:
                drinks_in_menu.append(drink.__repr__())
                current_table.drink_orders.append(drink)
            else:
                drinks_not_in_menu.append(drink_name)
                current_table.drinks_that_cannot_be_ordered.append(drink_name)

        display_list = [f'Table {table_number} ordered:', *drinks_in_menu,
                        f'{self.name} does not have in the menu:', *drinks_not_in_menu]
        return "\n".join(display_list)



    def leave_table(self, table_number: int):
        """Finds the table with the same table number, gets the bill for that table and clears it. Finally returns:
            "Table: {table_number}"
            "Bill: {table_bill}"
            The bill price should be formatted to the second decimal point.
"""
        table = self.get_table(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {table_bill:.2f}"


    def get_free_tables_info(self):
        """For each free table, returns the table info. Each table info should start on a new row."""
        output = []
        for table in self.tables_repository:
            if not table.is_reserved:
                output.append(table.free_table_info())
        return "\n".join(output)

    def get_total_income(self):
        """Returns the total income in the format, formatted to the second decimal point:
"Total income: {income}lv"
"""
        return f"Total income: {self.total_income:.2f}lv"


    def get_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

