employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
]

# Step 1: Extract salaries
salaries = list(map(lambda emp: emp["salary"], employees))

# Step 2: Find min and max salary
min_salary = min(salaries)
max_salary = max(salaries)

# Step 3: Filter out employees with min and max salary
filtered_salaries = list(
    map(
        lambda emp: emp["salary"],
        filter(lambda emp: emp["salary"] != min_salary and emp["salary"] != max_salary, employees)
    )
)

# Step 4: Calculate average
average_salary = sum(filtered_salaries) / len(filtered_salaries)

print("Average Salary (excluding min and max):", average_salary)
