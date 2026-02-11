# Basic class definition

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand} ({self.year})"

# Creating objects
c1 = Car("Toyota", 2015)
c2 = Car("BMW", 2020)

print(c1.info())
print(c2.info())
