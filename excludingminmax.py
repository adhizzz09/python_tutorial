employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
]

def get_salary(employee):
    return employee["salary"]
    
def is_middle_salary(salary,min,max):
    return salary != min and salary != max

    def average_salary(values):
        return sum(values) / len(values)
        def average_salary_excluding_min_max(employees):
            salaries = list(map(get_salary, employees))
            min_salary = min(salaries)  
            max_salary = max(salaries)
            middle_salaries = list(filter(salary_filter,salaries))
            return average_salary(middle_salaries)

            def main():
                avg_salary = average_salary_excluding_min_max(employees)
                print("Average Salary (excluding min and max):", avg_salary)

            if __name__ == "__main__":
                main()


