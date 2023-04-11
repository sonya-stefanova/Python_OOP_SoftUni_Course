from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:

    VALID_MEALS = {
        "Starter": Starter,
        "MainDish": MainDish,
        "Dessert": Dessert
    }
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def __find_client(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client
        return False

    def __get_meal(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal

    def __check_menu_not_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def register_client(self, client_phone_number: str):
        """•	Creates a client (object) and adds it to the client list and returns the message
                    "Client {phone_number} registered successfully."
            •	If a client with the same phone number is already registered,
            raise an Exception with the message "The client has already been registered!"
"""
        if self.__find_client(client_phone_number):
            raise Exception("The client has already been registered!")
        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        """•	This method adds all the meals (objects) given to the menu list.
        •	If one or more of the provided objects are NOT meals (not a "Starter", a "MainDish", or a "Dessert") ignore them and keep adding only the meals.
        •	Note: you will always be given meals with different names
"""
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        """•	It should return the details() for each meal on the menu on separate lines
            •	If there are less than 5 meals on the menu,
            raise an Exception with the message "The menu is not ready!"
"""
        self.__check_menu_not_ready()

        result = []
        for meal in self.menu:
            result.append(meal.details())
        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):

        self.__check_menu_not_ready()

        if not self.__find_client(client_phone_number):
            self.register_client(client_phone_number)

        current_shopping_cart = []
        current_bill = 0
        client = self.__find_client(client_phone_number)

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = self.__get_meal(meal_name)
            if meal is None:
                raise Exception(f"{meal_name} is not on the menu!")

            if quantity > meal.quantity:
                raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")

            current_meal = meal.__class__(meal.name, meal.price, quantity)
            current_shopping_cart.append(current_meal)
            current_bill += meal.price * quantity

        client.shopping_cart.extend(current_shopping_cart)
        client.bill += current_bill

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = self.__get_meal(meal_name)
            meal.quantity -= quantity

        meal_names = []
        for meal in client.shopping_cart:
            meal_names.append(meal.name)
        return f"Client {client_phone_number} successfully ordered {', '.join(meal_names)} for {client.bill:.2f}lv."



    def cancel_order(self, client_phone_number):
        client = self.__find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        for client_meal in client.shopping_cart:
            for meal in self.menu:
                if client_meal.name == meal.name:
                    meal.quantity += client_meal.quantity
        client.shopping_cart = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        client.shopping_cart = []
        total_paid_money = client.bill
        client.bill = 0
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
