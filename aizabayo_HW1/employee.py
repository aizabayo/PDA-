class Employee: 
    """Creating Super class Employe and use __init__ methode to initialize the attribute"""               
    def __init__(self,employee_id,first_name, last_name,  email, salary):
        self.__employee_id = employee_id
        self.__first_name = first_name             # initializing private attribute
        self.__last_name = last_name                
        self.__email = email
        self.__salary = salary
        # using Getter methode to access the private attribute
    def get_employee_id(self):            
        return self.__employee_id
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_email(self):
        return self.__email
    
    def get_salary(self):
        return self.__salary
    
    def get_salary(self):
        return self.__salary
    
    def get_employee_earning(self):
        return self.__salary
    # using override __str__ methode to display the Employee information
    def __str__(self):
        return f'\tEmployee Information:\n\nThe Employee ID:{self.__employee_id}\nFirst Name:{self.__first_name}\nLast Name:{self.__last_name}\nEmail:{self.__email}\nEmployee Salary:${self.__salary}'
    



  
    