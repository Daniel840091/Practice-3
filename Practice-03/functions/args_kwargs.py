def sum_all(*args):
    total = 0
    for x in args:
        total += x
    return total

def build_profile(**kwargs):
    return kwargs

print(sum_all(1, 2, 3, 4))
print(build_profile(age=17, city="Almaty", track="IT"))