class Flyable:
    def fly(self):
        return "I can fly"

class Swimmable:
    def swim(self):
        return "I can swim"

class Duck(Flyable, Swimmable):
    def sound(self):
        return "Quack!"

d = Duck()
print(d.sound())
print(d.fly())
print(d.swim())
