    # Basic inheritance example

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

a = Animal("Unknown")
d = Dog("Rex")
c = Cat("Murka")

print(a.name, a.speak())
print(d.name, d.speak())
print(c.name, c.speak())
