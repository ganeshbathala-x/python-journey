class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def manage(self):
        print("Managing", self.department, "department")


manager = Manager("Arun", 50000, "IT")

manager.show_details()
manager.manage()







