"""Designing Saving Account class inherit from Bank Account class with function of \
    performing saving operation and calculate the interest\
        and then use override method to return the saving account detail"""
from account import Bank_Account      # by using file name i called the Bank account class to use its module             

class Savings_Account(Bank_Account):                # creatind child class Saving account of super class Bank account
    def __init__(self, owner_name, account_number, current_balance, interest_Rate):            # using init method to initialize the attribute of the class
        super().__init__(owner_name, account_number, current_balance)
        self.__interest_Rate = interest_Rate
    @property                         # using decorator to access the property of private interest rate 
    def interest_rate(self):
       return self.__interest_Rate
    def calculate_Interest(self):                         #creating method that calculate the interest and return the earned rate
        interest_earned = self.get_balance() * (self.__interest_Rate/100)         # by using balance from super class and apply interest rate initialized to find interest earned
        return f'The interest earned is equal to ${interest_earned}'                           # returning the interest earned 
                          
    
    
    def __str__(self):                                    # creating overriding method to access and call the super class bank account info
        return super().__str__()+ f'\nSaving Account Details:\nInterest rate: {self.__interest_Rate}%\n{self.calculate_Interest()} \n'
