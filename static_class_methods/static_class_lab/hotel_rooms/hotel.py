from project.room import Room


class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = [] #room objects are collected here

    @property
    def guests(self):
        return sum([room.guests for room in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = next(filter(lambda r: room_number == r.number, self.rooms))
        room.take_room(people)

    def free_room(self, room_number: int):
        room = next(filter(lambda r: room_number == r.number, self.rooms))
        room.free_room()

    def status(self):
        free_rooms = ', '.join([str(r.number) for r in self.rooms if not r.is_taken])
        taken_rooms = ', '.join([str(r.number) for r in self.rooms if r.is_taken])
        return f'Hotel {self.name} has {self.guests} total guests\n' \
               f'Free rooms: {free_rooms}\n' \
               f'Taken rooms: {taken_rooms}'


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
