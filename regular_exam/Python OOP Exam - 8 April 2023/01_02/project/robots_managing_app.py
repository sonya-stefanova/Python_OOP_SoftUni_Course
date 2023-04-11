from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_ROBOTS = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }
    VALID_SERVICES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    VALID_RELATIONS = {
        "FemaleRobot": "SecondaryService",
        "MaleRobot": "MainService"
    }

    def __init__(self):
        self.robots = []  # robots collection
        self.services = []  # services collection

    def add_service(self, service_type: str, name: str):
        """The method creates a service of the given type and adds it to the services collection.

        All service names will be unique.
        •	If the service type is not valid, raise an Exception with the following message:
        "Invalid service type!"
        •	Otherwise, create the service, add it to the services list, and return the following message:
        "{service_type} is successfully added."
"""
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        new_service = self.VALID_SERVICES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        """The method creates a robot of the given type and adds it to the robots' collection.

        All robots' names will be unique.
        •	If the robot type is not valid, raise an Exception with the following message:
        "Invalid robot type!"
        •	Otherwise, create the robot, add it to the robots' list, and return the following message:
        "{robot_type} is successfully added."
"""
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        new_robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(new_robot)
        # BaseService.add_robot(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        """The method adds the robot with the given name to the service if there is a capacity for that.
        Both robot and service with the given names will always exist.
    •	First, check if the robot can be added to the service.
    The Female robot can be ONLY added to the Secondary Service and the Male robot can be ONLY added to the Main Service.
    In case of a mismatch, return the message: "Unsuitable service."
    •	Next, if there is NOT enough capacity to add the robot to the service,
    raise an Exception with the following message: "Not enough capacity for this robot!"
    •	If the robot can be added successfully to the service,
    remove it from the robots' collection, and add it to the service.
    Return the following message: "Successfully added {robot_name} to {service_name}."
"""
        robot = self.__find_robot_by_name(robot_name)
        service = self.__find_service_by_name(service_name)

        if self.VALID_RELATIONS[robot.__class__.__name__] != service.__class__.__name__:
            return "Unsuitable service."

        if service.capacity == len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.__find_service_by_name(service_name)
        robot = next(filter(lambda r: r.name == robot_name, service.robots), None)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        found_service = self.__find_service_by_name(service_name)
        for robot in found_service.robots:
            robot.eating()
        return f"Robots fed: {len(found_service.robots)}."

    def service_price(self, service_name: str):
        found_service = self.__find_service_by_name(service_name)
        total_price = sum(robot.price for robot in found_service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        output = []
        for service in self.services:
            output.append(service.details())
        return '\n'.join(output)


    def __find_robot_by_name(self, robot_name):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot
        return None

    def __find_service_by_name(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service
        return None
