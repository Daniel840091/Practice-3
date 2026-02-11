# Using lambda with filter()

nums = list(range(1, 21))

evens = list(filter(lambda x: x % 2 == 0, nums))
multiples_of_3 = list(filter(lambda x: x % 3 == 0, nums))

values = [-3, -1, 0, 2, 5]
positive = list(filter(lambda x: x > 0, values))

print(evens)
print(multiples_of_3)
print(positive)
