class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
            return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2



class SuperVIPDiscount(VIPDiscount):
    """
    If you decide getting 60% discount for super VIP customers, it should be like this:
    You see, extension without modification.
    """
    def get_discount(self):
        return super().get_discount() * 1.5

