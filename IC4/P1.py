class Employee():
    def __init__(self):
        self.name = ''
        self.family = ''
        self.salary = 0
        self.department = ''

class FullTimeEmployee(Employee):

    def __init__(self):
        super(FullTimeEmployee, self).__init__()
        self._hours = 40


    def setHours(self,hours):
        self._hours=hours

    def getHours(self):
        return self._hours



def averageSalary(EmployeeArray):
        count = 0
        for i in EmployeeArray:
            count = count + i.salary
        salary = count/len(EmployeeArray)
        print(salary)

class Employee():
    def __init__(self):
        self.name = ''
        self.family = ''
        self.salary = 0
        self.department = ''






countEmployees = 0
employeeArray =[]
newEmployee = Employee()
newEmployee.name = 'Garth Brooks'
newEmployee.family = 'Wife,Son,Daughter'
newEmployee.salary = 130000
newEmployee.department = 'Computer Engineering'
employeeArray.append(newEmployee)
newEmployee = Employee()
newEmployee.name = 'James Harden'
newEmployee.family = 'Wife,Son,Daughter'
newEmployee.salary = 20000000
newEmployee.department = 'Vice President'
employeeArray.append(newEmployee)
newEmployee1 = FullTimeEmployee()
newEmployee1.name = 'Patrick Mahomes'
newEmployee1.family = 'Wife,Son,Daughter'
newEmployee1.salary = 3000000
newEmployee1.department = 'Quarterback: Football'
newEmployee1.setHours(70)
newEmployee1.getHours()
employeeArray.append(newEmployee1)
averageSalary(employeeArray)