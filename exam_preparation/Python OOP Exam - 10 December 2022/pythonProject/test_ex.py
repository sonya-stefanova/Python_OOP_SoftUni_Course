class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.__gender = None

    def say_hello(self):
        return "Say hello, mate!"

    def __str__(self):
        return f"{self.__class__.__name__} {self.name} is {self.age} years old"

    def __repr__(self):
        return self.name

class Daughter(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return super().__str__()

person = Person("Sonya", 36)
print(person.__dict__)
print(str(person))
print(repr(person))
daughter = Daughter("Mihaela", 6)
print(str(daughter))
print(Daughter.mro())
print(Person.mro())
print(daughter.__dict__)
print(person._Person__gender)