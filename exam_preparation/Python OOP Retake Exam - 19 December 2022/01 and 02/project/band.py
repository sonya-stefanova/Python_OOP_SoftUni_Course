class Band:
    def __init__(self, name: str):
        self.name = name
        self.members = [] #members (musician objects) of the band
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):

        """If the name is an empty string,
        raise a ValueError with the message: "Band name should contain at least one character!"""

        if not value:
            raise ValueError("Band name should contain at least one character!")
        self.__name = value


    def __str__(self):
        return f"{self.name} with {len(self.members)} members."