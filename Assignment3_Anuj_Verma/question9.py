
# 9. Create class OOPS and implement all oops concept in that.


class OOPS:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def getSalary(self):
        return self.salary

    def getName(self):
        return self.name

    def getRole(self):
        return self.role

emp1 = OOPS("Anuj", 10000, "Software Trainee")
print("Employee Name: ", emp1.getName())
print("Employee Role: ", emp1.getRole())
print("Employee Slary: ", emp1.getSalary())

