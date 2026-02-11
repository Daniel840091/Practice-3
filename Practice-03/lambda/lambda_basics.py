# lambda_basics.py
# Basic lambda examples

square = lambda x: x * x
add = lambda a, b: a + b
is_long = lambda s: len(s) >= 8
format_name = lambda first, last="User": f"{first.title()} {last.title()}"

print(square(5))
print(add(10, 7))
print(is_long("practice"))
print(format_name("daniel"))
print(format_name("daniel", "kbtU"))
