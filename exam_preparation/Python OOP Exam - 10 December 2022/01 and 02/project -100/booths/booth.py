from abc import ABC, abstractmethod


class Booth(ABC):
    def __init__(self, booth_number: int,  capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity

        self.delicacy_orders: list = [] #will contain delicacies (objects) that are ordered
        self.price_for_reservation: float = 0      #Each time a booth is reserved, the price for a reservation should be set.
        self.is_reserved:bool = False

    @property
    def capacity(self):
        return self.__capacity


    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        """1 Calculates the price for reservation,
            self.price_for_reservation = price per person * number of people.
           2 Set the price for reservation and
           3 reserve the booth
        """
        ...
