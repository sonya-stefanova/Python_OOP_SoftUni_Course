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
