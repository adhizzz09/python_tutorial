from functools import reduce
from itertools import chain

students = [
    {"name": "A", "marks": [50, 60, 70]},
    {"name": "B", "marks": [30, 40]},
    {"name": "C", "marks": [80, 90]}
]

# Step 1: Filter students with average >= 60
eligible_students = filter(
    lambda s: sum(s["marks"]) / len(s["marks"]) >= 60,
    students
)

# Step 2 & 3: Add grace marks and compute total
total_updated_marks = reduce(
    lambda acc, mark: acc + mark,
    map(
        lambda m: m + 5,
        chain.from_iterable(
            map(lambda s: s["marks"], eligible_students)
        )
    ),
    0
)

print(total_updated_marks)
