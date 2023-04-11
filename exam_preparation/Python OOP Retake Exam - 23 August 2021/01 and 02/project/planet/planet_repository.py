from project.planet.planet import Planet


class PlanetRepository:
    #It is a repository for planets that await to be explored.

    def __init__(self):
        self.planets = [] #empty list of planets

    def add(self, planet: Planet):
        """Adds a planet for exploration."""
        self.planets.append(planet)

    def remove(self, planet: Planet):
        """Removes a planet from the collection."""
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        """Returns a planet with that name if it exists."""
        for planet in self.planets:
            if planet.name == name:
                return planet