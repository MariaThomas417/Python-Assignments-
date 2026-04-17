
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")



class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        # Call Person constructor
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def show_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary}")



class Manager(Employee, Person):
    def __init__(self, name, age, employee_id, salary, department):
        # Call Employee constructor (which already calls Person)
        super().__init__(name, age, employee_id, salary)
        self.department = department

    
    def show_manager_info(self):
        print(f"Department: {self.department}")

    
    def display_full_details(self):
        print("\nManager Details")
        self.show_person_info()
        self.show_employee_info()
        self.show_manager_info()


t
m1 = Manager("Maria", 25, "E101", 50000, "IT")


m1.display_full_details()