from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:

    VALID_DELICACIES = {
        'Gingerbread': Gingerbread,
        'Stolen': Stolen
    }

    VALID_BOOTHS = {
        'Open Booth': OpenBooth,
        'Private Booth': PrivateBooth
    }


    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income: float = 0.00 #total income of the pastry shop


    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        """The method creates a delicacy of the given type and adds it to the delicacies' collection.
            All delicacy names should be unique.
            •	If a delicacy with that name exists,
            raise an Exception with the following message: "{delicacy name} already exists!"
            •	If the delicacy type is not valid,
            raise an Exception with the following message: "{type of delicacy} is not on our delicacy menu!"
            •	Otherwise, create the delicacy, add it to the delicacies' list, and
            return the following message: "Added delicacy {delicacy name} - {type of delicacy} to the pastry shop."
"""
        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = ChristmasPastryShopApp.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {delicacy.name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        """The method creates a booth of the given type and adds it to the booths' collection.
        All booth numbers should be unique.
        •	If a booth with that number exists,
        raise an Exception with the following message: "Booth number {booth number} already exists!"
        •	If the booth type is not valid,
        raise an Exception with the following message: "{type of booth} is not a valid booth!"
        •	Otherwise, create the booth,
         add it to the booths' list and return the following message:
         "Added booth number {booth number} in the pastry shop."
        •	Valid types of delicacies are: "Open Booth" and "Private Booth"
"""
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ChristmasPastryShopApp.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = ChristmasPastryShopApp.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth.booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        """Finds the first booth that is not reserved and whose capacity is enough for the number of people provided.
        •	If there is no such booth,
        raise an Exception with the following message: "No available booth for {number of people} people!"
        •	Otherwise, reserves the booth and
        return: "Booth {booth number} has been reserved for {number of people} people."
"""
        try:
            booth = next(filter(lambda b: b.capacity >= number_of_people and not b.is_reserved, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        """Finds the booth with the provided number and the delicacy with the provided name;
        and orders the delicacy for that booth.
            •	If there is no such booth,
            raise an Exception with the following message: "Could not find booth {booth number}!"
            •	If there is no such delicacy,
            raise an Exception with the following message: "No {delicacy name} in the pastry shop!"
            •	Otherwise, order the delicacy for that booth and
            return: "Booth {booth number} ordered {delicacy name}."
"""
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        """Finds the booth with the same booth's number (the booth's number will always be valid).
            •	Calculates the bill for that booth
            taking the price for reservation and all the price of all orders.
            The bill is added to the pastry shop's total income.
            •	Removes all the ordered delicacies,
                frees the booth,
                and sets the price for reservation to 0.
            •	Finally returns:
            "Booth {booth number}:"
            "Bill: {bill - formatted to the second decimal}lv."
"""
        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))

        bill = 0
        bill += booth.price_for_reservation
        for delicacy in booth.delicacy_orders:
            bill += delicacy.price

        self.income+=bill

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
