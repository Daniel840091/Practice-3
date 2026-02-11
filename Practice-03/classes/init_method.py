class User:
    def __init__(self, username, age=0):
        self.username = username
        self.age = age
        self.is_active = True

    def deactivate(self):
        self.is_active = False

u1 = User("daniel", 17)
u2 = User("guest")

print(u1.username, u1.age, u1.is_active)
u1.deactivate()
print(u1.username, u1.is_active)
print(u2.username, u2.age, u2.is_active)
