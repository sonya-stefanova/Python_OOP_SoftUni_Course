class IShape:
    def draw(self):
        pass

class Circle(IShape): #they should have in the init the specific attributes
    "The idea is to implement own behaviour of each class to avoid inheritance of behaviour that doesn't belong to this class"
    def draw(self):
        return "draw circle"

class Square(IShape):
    def draw(self):
        return "draw square"


class Rectangle(IShape):
    def draw(self):
        return "draw rectangle"

