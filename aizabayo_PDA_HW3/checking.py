"""Designing Checking Account class that inherits from the super class Bank account performing \
     the operation of withdraw with access to overdraft and then update the balance in the supper class\
         then return Account detail with overridden attribute"""
from account import Bank_Account

class Checking_Account(Bank_Account):                       # Creating child class
    def __init__(self, Owner_name, Account_number, Current_balance, overdraft_limit ):           # initializing attribute of child class
        super().__init__(Owner_name, Account_number, Current_balance)                            # calling the instance of super class
        self.__overdraft_limit  =overdraft_limit                                                 # initialize new attribute
    @property                                              # using decorate to proved access to private attribute
    def get_overdraft(self):                               # getter method that will help in calling the private attribute
        return self.__overdraft_limit
    def Withdraw(self, Amount):                             # Creating Withdraw method that will check the status of balance and amount to be withdrawn first
        balance_limit = self.get_balance() + self.__overdraft_limit               # adding overdraft amount to the balance
        if Amount <= balance_limit:                          # condition if the amount to withdraw does not exceed the availabe amount with additional overdraft
            return super().Withdraw(Amount)
        else:
            return f'Insufficient Fund! Please try later when you have enough Amount'         # returning message whenever trying to withdraw more than you have.
   
    def __str__(self):                                                # creating override method for overring the super class detail with the new information
        return super().__str__()+ f'\nThe checking Acount info:\nOverdraft Limit:{self.__overdraft_limit}'
