def divide(a, b):
    if b == 0:
        return None
    return a / b

def min_max(nums):
    return min(nums), max(nums)

print(divide(10, 2))
print(divide(10, 0))
mn, mx = min_max([3, 9, 1, 7])
print(mn, mx)
