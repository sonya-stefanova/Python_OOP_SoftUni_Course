class Planet:
    """it holds information about the items that can be found on its surface."""

    def __init__(self, name):
        self.name = name
        self.items = [] #each item that could be found on that planet

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value