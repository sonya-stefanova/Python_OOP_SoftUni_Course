class Validator:
    @staticmethod
    def find_astronaut(name, astronauts):
        for astronaut in astronauts:
            if astronaut.name == name:
                return astronaut

    @staticmethod
    def find_planet(planet_name, planets):
        for planet in planets:
            if planet.name == planet_name:
                return planet
