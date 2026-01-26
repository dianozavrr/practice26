class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return self.brand + " " + str(self.year) + " " + str(self.mileage)

    def info(self):
        print("Марка:", self.brand)
        print("Рік:", self.year)
        print("Пробіг:", self.mileage)

    def drive(self, km):
        self.mileage = self.mileage + km


a = Car("Audi", 2010, 175000)
a.info()
a.drive(60)
a.info()
print(a)
