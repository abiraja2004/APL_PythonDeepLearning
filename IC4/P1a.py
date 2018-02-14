
class Employees:
    employeeCount=0
    salary_expense=0
    employee_list=[]
    def __init__(self, name,dependents,salary,department):
        self.name = name
        self.family = dependents
        self.salary = salary
        self.department = department
        Employees.employeeCount+=1
        Employees.salary_expense += salary
        Employees.employee_list.append(self.name+' '+self.family)

class FTemployees(Employees):
    FTemployeeCount=0
    def __init__(self, name, family, salary, department):
        Employees.__init__(self, name, family, salary, department)
        self.__status = 'FT'
        FTemployees.FTemployeeCount += 1


class Company():

    def get_avg_salary(self):
        print(Employees.salary_expense/Employees.employeeCount)

    def get_employee_count(self):
        print(Employees.employeeCount)

    def get_employee_list(self):
        print(Employees.employee_list)

    def get_FTemployee_count(self):
        print(FTemployees.FTemployeeCount)

def main():
    John=Employees('John Smith','married',45000,'marketing')
    Carol=Employees('Carol Robinson','single''Robinson',60000,'marketing')
    Jim=FTemployees('Jim Thompson','married, children',145000,'operations')
    Sarah=FTemployees('SarahJohnson',100000,'single''operations', 'Full Time')
    ABC=Company()
    ABC.get_avg_salary()
    ABC.get_employee_count()
    ABC.get_employee_list()
    ABC.get_FTemployee_count()
main()