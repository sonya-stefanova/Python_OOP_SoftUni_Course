from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_monthly_consumption = 0
        for room in self.rooms:
            total_monthly_consumption += (room.expenses +room.room_cost)

        return f"Monthly consumption: {total_monthly_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_expenses = room.expenses +room.room_cost
            if room.budget >= total_expenses:
                room.budget -= total_expenses
                result.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
        return "\n".join(result)

    def status(self):
        result = []

        total_people_in_hotel = sum([r.members_count for r in self.rooms])

        result.append(f'Total population: {total_people_in_hotel}')

        for room in self.rooms:
            result.append(f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, '
                          f'Expenses: {room.expenses:.2f}$')

            if room.children: # if len(room.children)>0:
                child_number = 1
                for child in room.children:
                        result.append(f"--- Child {child_number} monthly cost: {child.get_monthly_expense():.2f}$")
                        child_number += 1

            else:
                for appliance in room.appliances:
                    result.append(f"--- Appliances monthly cost: {appliance.get_monthly_expense():.2f}$")

        return "\n".join(result)