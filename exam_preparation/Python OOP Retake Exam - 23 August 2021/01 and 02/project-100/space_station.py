from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository


class SpaceStation:
    number_of_successful_missions = 0
    number_of_not_completed_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type == "Biologist":
            self.astronaut_repository.add(Biologist(name))
        elif astronaut_type == "Geodesist":
            self.astronaut_repository.add(Geodesist(name))
        elif astronaut_type == "Meteorologist":
            self.astronaut_repository.add(Meteorologist(name))
        else:
            raise Exception("Astronaut type is not valid!")

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = Validator.find_astronaut(name, self.astronaut_repository.astronauts)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.astronauts.remove(astronaut)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = Validator.find_planet(planet_name, self.planet_repository.planets)
        if not planet:
            raise Exception("Invalid planet name!")

        astronauts_for_mission = []
        for astronaut in sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen):
            if astronaut.oxygen > 30:
                astronauts_for_mission.append(astronaut)
        astronauts_for_mission = astronauts_for_mission[0:5]

        if not astronauts_for_mission:
            raise Exception("You need at least one astronaut to explore the planet!")

        count_astronauts = 0
        for astronaut in astronauts_for_mission:
            if not planet.items:
                break
            while astronaut.oxygen > 0 and planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            count_astronauts += 1

        if not planet.items:
            self.number_of_successful_missions += 1
            return f"Planet: {planet_name} was explored. {count_astronauts} astronauts participated in collecting items."
        else:
            self.number_of_not_completed_missions += 1
            return "Mission is not completed."

    def report(self):
        output = [f"{self.number_of_successful_missions} successful missions!",
                  f"{self.number_of_not_completed_missions} missions were not completed!", "Astronauts' info:"]

        for astronaut in self.astronaut_repository.astronauts:
            output.append(f'Name: {astronaut.name}')
            output.append(f"Oxygen: {astronaut.oxygen}")
            if astronaut.backpack:
                output.append(f"Backpack items: {', '.join(astronaut.backpack)}")
            else:
                output.append(f"Backpack items: none")

        return '\n'.join(output)

        
