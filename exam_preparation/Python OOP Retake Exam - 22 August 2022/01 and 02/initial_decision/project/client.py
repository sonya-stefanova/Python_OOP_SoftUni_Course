class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = [] #o	An empty list that will contain all meals (objects) added by the client
        self.bill = 0.0
        self.ordered_meals = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value.startswith("0") and len(value) == 10 and all(value.isdigit() for el in value):
            self.__phone_number = value
        else:
            raise ValueError("Invalid phone number!")

    def __repr__(self):
        return self.__phone_number
