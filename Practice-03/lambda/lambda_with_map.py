# Using lambda with map()

nums = [1, 2, 3, 4, 5]

# Transform each element
squares = list(map(lambda x: x * x, nums))

prices = [100, 250, 80]
with_tax = list(map(lambda p: p * 1.12, prices))

words = ["Python", "FuNcTiOn", "LAMBDA"]
lowered = list(map(lambda w: w.lower(), words))

print(squares)
print(with_tax)
print(lowered)
