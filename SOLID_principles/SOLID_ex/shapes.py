from abc import ABC, abstractmethod


# OCP -----------Open/Closed / Liskov Substitution Principle------------
# The code should be open for extension and not for modification/refactoring
# In this task the polymorphism concept fails ==> Liskov
# We need to implement the calculate_area abstract method in an abstract class Shape

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        ...


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height / 2


class AreaCalculator:
    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area() #single responsibility edit

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]

calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)