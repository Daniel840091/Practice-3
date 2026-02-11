# Using lambda with sorted()

students = [
    {"name": "Daniel", "score": 88},
    {"name": "Aruzhan", "score": 95},
    {"name": "Timur", "score": 74},
]

by_score = sorted(students, key=lambda s: s["score"])
by_score_desc = sorted(students, key=lambda s: s["score"], reverse=True)
by_name = sorted(students, key=lambda s: s["name"].lower())

words = ["lambda", "map", "filter", "sorted", "py"]
by_length = sorted(words, key=lambda w: len(w))

print(by_score)
print(by_score_desc)
print(by_name)
print(by_length)
