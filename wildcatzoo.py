# nhap du lieu tu code khac vao 
from Caretaker import Caretaker
from Cheetah import Cheetah
from Keeper import Keeper
from Lion import Lion
from Tiger import Tiger
from Vet import Vet

# init quan li Zoo
class Zoo:
    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.worker_capacity = worker_capacity
        self.animals = []
        self.workers = []

# them dong vat vao
    def add_animal(self, animal, price):
        if len(self.animals) < self.animal_capacity:
            if self.budget >= price:
                self.animals.append(animal)
                self.budget -= price
                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            else:
                return "Not enough budget"
        else:
            return "Not enough space for animal"

# them nhan vien
    def hire_worker(self, worker):
        if len(self.workers) < self.worker_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

# tRẢ lương nhan viên 
    def pay_workers(self):
        total_salaries = sum([worker.salary for worker in self.workers])
        if self.budget >= total_salaries:
            self.budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy."
        
#chăm sóc animal với ngân sách 
    def tend_animals(self):
        total_needs = sum([animal.get_needs() for animal in self.animals])
        if self.budget >= total_needs:
            self.budget -= total_needs
            return f"You tended all the animals. They are happy. Budget left: {self.budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals"
        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        if lions:
            result += f"\n----- {len(lions)} Lions:\n" + "\n".join(lions)
        if tigers:
            result += f"\n----- {len(tigers)} Tigers:\n" + "\n".join(tigers)
        if cheetahs:
            result += f"\n----- {len(cheetahs)} Cheetahs:\n" + "\n".join(cheetahs)
        return result
# bao cao cuoi cung 
    def workers_status(self):
        result = f"You have {len(self.workers)} workers"
        keepers = [repr(w) for w in self.workers if isinstance(w, Keeper)]
        caretakers = [repr(w) for w in self.workers if isinstance(w, Caretaker)]
        vets = [repr(w) for w in self.workers if isinstance(w, Vet)]
        if keepers:
            result += f"\n----- {len(keepers)} Keepers:\n" + "\n".join(keepers)
        if caretakers:
            result += f"\n----- {len(caretakers)} Caretakers:\n" + "\n".join(caretakers)
        if vets:
            result += f"\n----- {len(vets)} Vets:\n" + "\n".join(vets)
        return result
# Test Code from Đề Bài 
zoo = Zoo("Zootopia", 3000, 5, 8)
# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), 
Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), 
Lion("Nala", "Female", 4)]
# Animal prices
prices = [200, 190, 204, 156, 211, 140]
# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), 
Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), 
Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
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