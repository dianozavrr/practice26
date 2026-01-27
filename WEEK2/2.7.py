class Animal:
    def sound(self):
        return "звук"

class Dog(Animal):
    def sound(self):
        return "Гав"

class Cat(Animal):
    def sound(self):
        return "Мяу"

class Cow(Animal):
    def sound(self):
        return "Му"

animals = [Dog(), Cat(), Cow()]

for a in animals:
    print(a.sound())
