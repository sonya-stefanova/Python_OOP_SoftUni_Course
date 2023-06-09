from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_FOR_PERSON = 3.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        price_for_reservation = PrivateBooth.PRICE_FOR_PERSON * number_of_people
        self.price_for_reservation = price_for_reservation
        self.is_reserved = True