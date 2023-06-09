from abc import ABC, abstractmethod


class Booth(ABC):
    PRICE_PER_PERSON = None

    @abstractmethod
    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity

        self.delicacy_orders = [] #o	Empty list that will contain delicacies (objects) that are ordered.
        self.price_for_reservation = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        total = number_of_people * self.PRICE_PER_PERSON
        self.price_for_reservation = total
        self.is_reserved = True