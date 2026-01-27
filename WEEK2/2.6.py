class Animal:
    def sound(self):
        print("Звук тварини")

class Dog(Animal):
    def sound(self):
        print("Гав")

class Cat(Animal):
    def sound(self):
        print("Мяу")

class Cow(Animal):
    def sound(self):
        print("Муу")

Dog().sound()
Cat().sound()
Cow().sound()
