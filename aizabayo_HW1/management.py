"""Designing the Manager class to inherit from Employee super classto access the super class attribute and methode"""
from employee import Employee             # importing the super class
class Manager(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, department, direct_report,Earning_rate): # initialization methode
        super().__init__(employee_id, first_name, last_name, email, salary) 
        #initializing the private attribute 
        self.__department = department
        self.__direct_report = direct_report
        self.__earning_rate = Earning_rate 
    # using getter to access the property of the private attribute
    def get_department(self):
        return self.__department
    def get_direct_report(self):
        return self.__direct_report
    def get_earning_rate(self):
        return self.__earning_rate
   # methode for calculating the total amaount the manager earned with bonus 
    
    def percentage_earning(self):
        return self.get_salary() + self.__earning_rate*self.get_salary()
    # using override methode to print the manager class information with super class detail

    def __str__(self):
        return super().__str__()+ f'\nDepartment:{self.__department}\nDirect report:{self.__direct_report}\nEarning Rate:{self.__earning_rate}%, \nTotal Earned:$ {self.percentage_earning()}\n'

