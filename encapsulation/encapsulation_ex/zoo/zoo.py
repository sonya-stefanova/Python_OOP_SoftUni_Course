from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if self.__budget - price < 0 and self.__animal_capacity - len(self.animals) > 0:
            return "Not enough budget"

        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity - len(self.workers)>0:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for each_worker in self.workers:
            if each_worker.name == worker_name:
                self.workers.remove(each_worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = sum(each_worker.salary for each_worker in self.workers)
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending_care = sum(each_animal.MONEY_FOR_CARE for each_animal in self.animals)
        if self.__budget >= tending_care:
            self.__budget -= tending_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_lions = 0
        total_tigers = 0
        total_cheetahs = 0

        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if type(animal).__name__ == "Lion":
                total_lions += 1
                lions.append(animal)
            elif type(animal).__name__ == "Tiger":
                total_tigers += 1
                tigers.append(animal)
            elif type(animal).__name__ == "Cheetah":
                total_cheetahs += 1
                cheetahs.append(animal)

        lions_info = '\n'.join(str(lion) for lion in lions)
        tigers_info = '\n'.join(str(tiger) for tiger in tigers)
        cheetahs_info = '\n'.join(str(cheetah) for cheetah in cheetahs)

        return f"You have {len(self.animals)} animals\n----- {len(lions)} " \
               f"Lions:\n{lions_info}\n----- {len(tigers)} Tigers:\n" \
               f"{tigers_info}\n----- {len(cheetahs)} Cheetahs:\n{cheetahs_info}"

    def workers_status(self):
        total_caretakers = 0
        total_keepers = 0
        total_vets = 0

        caretakers = []
        keepers = []
        vets = []

        for worker in self.workers:
            if type(worker).__name__ == "Caretaker":
                total_caretakers += 1
                caretakers.append(worker)
            elif type(worker).__name__ == "Keeper":
                total_keepers += 1
                keepers.append(worker)
            elif type(worker).__name__ == "Vet":
                total_vets += 1
                vets.append(worker)

        caretakers_info = '\n'.join(str(caretaker) for caretaker in caretakers)
        keepers_info = '\n'.join(str(keeper) for keeper in keepers)
        vets_info = '\n'.join(str(vet) for vet in vets)

        return f"You have {len(self.workers)} workers\n----- {len(keepers)} " \
               f"Keepers:\n{keepers_info}\n----- {len(caretakers)} Caretakers:\n" \
               f"{caretakers_info}\n----- {len(vets)} Vets:\n{vets_info}"

  # def animals_status(self):
  #       animals = {'Lion': [], 'Tiger': [], 'Cheetah': []}
  #       [animals[animal.__class__.__name__].append(str(animal)) for animal in self.animals]
  #
  #       output = [f'You have {len(self.animals)} animals']
  #
  #       for animal_class, animal_names in animals.items():
  #           output.append(f'----- {len(animal_names)} {animal_class}s:\n' + '\n'.join(animal_names))
  #       return '\n'.join(output)
  #
  #   def workers_status(self):
  #       workers = {'Keeper': [], 'Caretaker': [], 'Vet': []}
  #       [workers[worker.__class__.__name__].append(str(worker)) for worker in self.workers]
  #
  #       output = [f'You have {len(self.workers)} workers']
  #
  #       for worker_class, worker_names in workers.items():
  #           output.append(f'----- {len(worker_names)} {worker_class}s:\n' + '\n'.join(worker_names))
  #       return '\n'.join(output)

zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())