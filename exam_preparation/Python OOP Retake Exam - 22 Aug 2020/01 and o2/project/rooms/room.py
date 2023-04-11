from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        
    @property
    def expenses(self):
        return self.__expenses
    
    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        #Each element of args will be a list (with children or appliances).
        # Calculate the total cost for a month (30 days) of all elements in the lists
        # and set the expenses attribute to the result.

        total_expenses = 0

        for elements in args:
            for el in elements:
                if isinstance(el, Appliance):
                    total_expenses += el.get_monthly_expense()
                elif isinstance(el, Child):
                    total_expenses += el.get_monthly_expense()
        self.expenses = total_expenses

