# from project.space_station import SpaceStation
# from project.planet.planet_repository import PlanetRepository
#
#
# space = SpaceStation()
# print(space.add_astronaut("Biologist", "Lili"))
# print(space.add_astronaut("Geodesist", "Ivan"))
# print(space.add_astronaut("Meteorologist", "Petar"))
# # print(space.add_astronaut("Other", "Pepi"))
# print(space.add_planet("Luna", "apple, knife, glass, table"))
# print(*space.planet_repository)
# print(space.add_planet("Luna", "kl, l;, k"))
# # print(space.retire_astronaut("Petar"))
# # print(space.retire_astronaut("gfh"))
# space.recharge_oxygen()
# for a in space.astronaut_repository:
#     print(a.oxygen)
# print(space.send_on_mission("Luna"))

from project.space_station import SpaceStation

space_station1 = SpaceStation()

print(space_station1.add_astronaut('Geodesist', 'GOGO'))
print(space_station1.add_astronaut('Geodesist', 'GOGO'))
print(space_station1.add_astronaut('Meteorologist', 'ALEX'))
print(space_station1.add_astronaut('Biologist', 'PESHO'))

print(space_station1.add_planet('MARS', 'item1, item2, item3, item4, item5'))
print(space_station1.add_planet('EARTH', 'item1, item2'))

print(space_station1.add_planet('XXX', 'item1, item2, item3, item4, item5'))
print(space_station1.planet_repository.planets)
print(space_station1.recharge_oxygen())

print(space_station1.send_on_mission('MARS'))
print(space_station1.report())
print()

print(space_station1.send_on_mission('EARTH'))
print(space_station1.report())
print()

print(space_station1.send_on_mission('XXX'))
print(space_station1.report())
