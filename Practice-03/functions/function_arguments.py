def power(base, exp=2):
    return base ** exp

def introduce(name, age, city="Almaty"):
    return f"My name is {name}, I'm {age}, from {city}."

print(power(3))                 # default
print(power(2, 5))              # custom exp
print(introduce("Daniel", 17))  # default city
print(introduce(name="Daniel", age=17, city="Astana"))  # keyword args