"""Designing the intern class which is designied to show intern information and how much they\
    earned during the period of the internship, it was also inherited from super class Employee\
        to class its attribute"""
from employee import Employee                       # importing the Super class Employee inorder to interact with its property

class Intern(Employee):                         # creating intern class
    def __init__(self, employee_id, first_name, last_name, email, salary,University, program, internship_duration, start_date, end_date, intern):      #initializing the attribute
        super().__init__(employee_id, first_name, last_name, email, salary) #Using super to call the attribute of super class
        self.__University_name = University            #initializing the attribute with private property
        self.__Program_name = program
        self.__Internship_duration = internship_duration
        self.__start_date = start_date
        self.__end_date = end_date
        self.__intern = intern
    # Using Methode to access the private attribute data
    def get_univiversity_name(self):
        return self.__University_name
    def get_program_name(self):
        return self.__Program_name
    def get_internship_duration(self):
        return self.__Internship_duration
    def get_start_date(self):
        return self.__start_date
    def get_end_date(self):
        return self.__end_date
    def get_intern(self):
        return self.__intern
    #called methode for determing the total earned of intern
    def percentage_earning(self):
        if self.__Internship_duration <3 or self.__Internship_duration > 6:
            return 'Error: The system is designed to provide earn where internship is in duration between 3 to 6'
        else:
            return self.get_salary()*(self.__Internship_duration/12)
    #Creating overriding methode to present the detailed information of intern
    def __str__(self):
        return (super().__str__() + f'\nRole: {self.__intern}'
            f'\nUniversity:{self.__University_name}\nProgram:{self.__Program_name}\n'
            f'Start Date:{self.__start_date} - End Date: {self.__end_date}\n'
            f'Internship Duration:{self.__Internship_duration} Months\nTotal Earning: ${self.percentage_earning()}\n') 
            
#interm = Intern('10089', "Jan", "levikson", "ljan@andrew.cmu.edu", 5000, "CMU Africa", "Electrical and Computer Engineering", 6, '02-02-2023', '01-07-2023', 'Intern')
#print(interm)
