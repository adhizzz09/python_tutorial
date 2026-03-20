class Employee:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
    def display_employee(self):
        print("employee ID:",self.emp_id)
        print("employee name:",self.name)
        print("Base Salary:",self.base_salary)

    def annual_salary(self):
        return self.base_salary*12
    
class Manager(Employee):
    def __init__(self,emp_id,name,base_salary,department,bonus):
        super().__init__(emp_id,name,base_salary)
        self.department=department
        self.bonus=bonus
        
    def total_salary(self):
        return self.annual_salary()+self.bonus
    
    def display_manager(self):
        self.display_employee()
        print("Department:",self.department)
        print("Bonus:",self.bonus)
        print("Total Annual Salary:",self.total_salary())
        print()

    m1= Manager(101,"adhi",50000,"sales",100000)
    m2= Manager(102,"tithi",60000,"HR",120000)
    m3= Manager(103,"Vikram",55000,"IT",90000)

    Managers=[m1,m2,m3]
    for manager in Managers:
        manager.display_manager()

