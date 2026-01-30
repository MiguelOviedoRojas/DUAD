class Employee():
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    @property
    def name(self):
        return self.__name
    
    @property
    def user_salary(self):
        return self.__salary
    
    @user_salary.setter
    def user_salary(self, salary):
        if isinstance(salary,(int, float)):
            if salary < 0:
                raise ValueError
            else:
                self.__salary = salary
        else:
            raise TypeError
        


    def promote(self, percentage):
        if isinstance (percentage,(int,float)):
            if percentage > 0:
                new_salary = (self.user_salary * percentage) + self.user_salary
                self.user_salary = new_salary
                return self.user_salary
            else:
                raise ValueError
        else:
            raise TypeError
            
                
    
    def print_salary(self):
        return self.user_salary
        




employee_name = "Migue"
employee_salary = float(input("Insert Salary: "))
employee = Employee(employee_name, employee_salary)
print(f"Employee Name: {employee.name}, Employee Salary: {employee.user_salary}.")

try:
    employee.salary = employee_salary
except ValueError as ex:
    print(ex)

try:
    salary_promote = float(input("Insert Promote Salary: "))
    print(f"New Salary is: {employee.promote(salary_promote)}")
except ValueError as ex:
    print(f"Error: {ex}")
except TypeError as tex:
    print(f"Error: {tex}")

