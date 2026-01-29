from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Lion(Animal):
    def sound(self):
        return "Rooar"

class Monkey(Animal):
    def sound(self):
        return "Oo-aa"

class Elephant(Animal):
    def sound(self):
        return "Poooh"

class Keeper:
    def hear(self, animal):
        print(animal.sound())

animals = [Lion(), Monkey(), Elephant()]
k = Keeper()

for a in animals:
    k.hear(a)
