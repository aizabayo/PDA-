from employee import Employee

class Director(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, department, annual_bonus):
        super().__init__(employee_id, first_name, last_name, email, salary)
        self.__department = department
        self.__annual_bonus = annual_bonus
    def get_department(self):
        return self.__department
    def get_annual_bonus(self):
        return self.__annual_bonus
        
    def percentage_earning(self):
        return self.get_salary() + self.__annual_bonus
    def __str__(self):
        return super().__str__() + f'\nDepartment:{self.__department}\nAnnual Bonus: ${self.__annual_bonus}\nTotal Earning:$ {self.percentage_earning()}' 