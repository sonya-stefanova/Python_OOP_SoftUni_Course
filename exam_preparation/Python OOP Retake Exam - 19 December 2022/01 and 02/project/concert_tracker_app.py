from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert
from project.factory.musician_factory import MusicianFactory


class ConcertTrackerApp:


    # NEEDED_SKILLS_CONCERT_START = {
    #     {"Rock":
    #          {
    #              "Drummer": ["play the drums with drumsticks"],
    #              "Singer": ["sing high pitch notes"],
    #              "Guitarist": ["play rock"]
    #           },
    #      "Metal":
    #          {
    #              "Drummer": ["play the drums with drumsticks"],
    #              "Singer": ["sing low pitch notes"],
    #              "Guitarist": ["play metal"]},
    #      "Jazz":
    #          {
    #              "Drummer": ["play the drums with drum brushes"],
    #              "Singer": ["sing high pitch notes", "sing low pitch notes"],
    #              "Guitarist": ["play jazz"]
    #          }
    #      }

    def __init__(self):
        self.concerts = []
        self.bands = []
        self.musicians = []

        self.musician_factory = MusicianFactory()

    def create_musician(self, musician_type: str, name: str, age: int):
        """The method creates a new musician.
        •	If the musician type is not a valid type,
        raise a ValueError with the message "Invalid musician type!"
      •	If there is a musician with the same name,
        raise an Exception with the message "{musician_name} is already a musician!"
        •	If everything is valid, create the musician,
        add it to the musicians' list, and return a message "{musician_name} is now a {musician_type}."
"""

        if any(m.name == name for m in self.musicians):
            raise Exception(f"{name} is already a musician!")

        try:
            musician = self.musician_factory.create_musician(musician_type, name, age)
            self.musicians.append(musician)
            return f"{name} is now a {musician_type}."

        except KeyError as error:
            return str(error)

    def create_band(self, name: str, band=None):
        """The method creates a new band.
        •	If there is already a band with the same name, raise an Exception with the message
        "{band_name} band is already created!"
        •	If everything is valid, create a new band,
        add it to the bands' list, and return a message "{band_name} was created."""
        if any(band.name == name for band in self.bands):
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{band.name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        """•	If there is already a concert in the same place,
        raise an Exception with the message
        "{concert_place} is already registered for {concert_genre} concert!"
            •	If everything is valid, create a new concert,
            add it to the concerts' list, and
            return a message "{concert_genre} concert in {concert_place} was added."
"""
        if any(c.place == place for c in self.concerts):
            concert = [c for c in self.concerts if c.place == place][0]
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        """The method adds a musician to the band.
        •	If there isn't a musician with the given name, raise an Exception with the message
        "{musician_name} isn't a musician!"
        •	If there isn't a band with the given name, raise an Exception with the message
        "{band_name} isn't a band!"
        •	If everything is valid, add the musician to the band and return the message
        "{musician_name} was added to {band_name}."
"""
        try:
            musician = next(filter(lambda x: x.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda x: x.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        """The method removes a musician from the band.
        •	If there isn't a band with the given name, raise an Exception with the message
        "{band_name} isn't a band!"
        •	If there isn't a musician with the given name who is a member of the given band, raise an Exception with the message
         "{musician_name} isn't a member of {band_name}!"
        •	If everything is valid, remove the musician from the band and return the message
        "{musician_name} was removed from {band_name}."
"""
        try:
            band = next(filter(lambda x: x.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda x: x.name == musician_name, band.members))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        """The method is to start a concert at the given place with the given band.
        The concert place and the band name will always be valid.
        However, there are some rules for the band to start a concert depending on the band members and the concert type:
        •	If there is NOT at least one member of each type
        (at least 1 singer, at least 1 drummer, and at least 1 guitarist),
        raise an Exception with the exception_message
        "{band name} can't start the concert because it doesn't have enough members!"

        •	Then, check if the band can play at the concert:
        o	For a band to play at a "Rock" concert, the needed skills for all members depending on the musician type are:
            	Drummer - play the drums with drumsticks
            	Singer - sing high pitch notes
            	Guitarist – play rock
        o	For a band to play at a "Metal" concert, the needed skills for all members depending on the musician type are:
            	Drummer - play the drums with drumsticks
            	Singer - sing low pitch notes
            	Guitarist – play metal
        o	For a band to play at a "Jazz" concert, the needed skills for all members depending on the musician type are:
            	Drummer - play the drums with drum brushes
            	Singer - sing high pitch notes and sing low pitch notes
            	Guitarist – play jazz
        •	If one or more band members don't have the required skills to play at a concert, raise an Exception with the exception_message "The {band_name} band is not ready to play at the concert!"
        •	If all members can play at a concert, calculate the profit by the following formula: "(audience * ticket price) - expenses", and return the following exception_message: "{band_name} gained {profit}$ from the {concert_genre} concert in {concert_place}."
        o	Profit should be formatted to the second decimal place.
        """

        band = next(filter(lambda b: b.name == band_name, self.bands))  # always valid as per description above
        concert = next(
            filter(lambda c: c.place == concert_place, self.concerts))  # always valid as per description above

        actual_band_member_types = [member.__class__.__name__ for member in band.members]
        if len(set(actual_band_member_types)) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        # all_musicians = []
        # for musician, skills in self.NEEDED_SKILLS_CONCERT_START[concert.CONCERT_TYPES].items():
        #     for band_musician in band.members:
        #         if band_musician.__class__.__name__ == musician and \
        #                 all(skill in band_musician.skills for skill in skills):
        #             all_musicians.append(band_musician)
        #
        # if len(all_musicians) != len(band.members):
        #     raise Exception(f"The {band_name} band is not ready to play at the concert!")
        exception_message = f"The {band_name} band is not ready to play at the concert!"

        if concert.genre == "Rock":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(exception_message)
                elif member.__class__.__name__ == "Singer" and "sing high pitch notes" not in member.skills:
                    raise Exception(exception_message)
                elif member.__class__.__name__ == "Guitarist" and "play rock" not in member.skills:
                    raise Exception(exception_message)

        elif concert.genre == "Metal":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(exception_message)
                elif member.__class__.__name__ == "Singer" and "sing low pitch notes" not in member.skills:
                    raise Exception(exception_message)
                elif member.__class__.__name__ == "Guitarist" and "play metal" not in member.skills:
                    raise Exception(exception_message)

        elif concert.genre == 'Jazz':
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drum brushes" not in member.skills:
                    raise Exception(exception_message)
                elif member.__class__.__name__ == "Singer":
                    if "sing low pitch notes" not in member.skills or "sing high pitch notes" not in member.skills:
                        raise Exception(exception_message)
                elif member.__class__.__name__ == "Guitarist" and "play jazz" not in member.skills:
                    raise Exception(exception_message)

        profit = concert.audience * concert.ticket_price - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
