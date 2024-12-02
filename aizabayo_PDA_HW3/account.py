"""Designing Bank account class Object-Oriented Programming \
    with methods that allow user to withdraw and deposit to the account"""
class Bank_Account:
    # using init special method to initialize attribute
    def __init__(self, Owner_name, Account_number, Current_balance):
        self.__name = Owner_name                     # initialize the bank account info as attribute
        self.__account = Account_number
        self.__balance = float(Current_balance)
    
    def Deposit(self, Amount):                      # Declaring Deposit method for perfoming deposit process
        if Amount > 0:                               # statement to check whether the amount to be deposit is valid or not
            self.__balance = self.__balance + Amount
            return f'Dear customer, ${Amount} has been credited to your account\
            the new balance is ${self.__balance}'
        else:
            return f'Invalid deposit \nTry again later'                                      # returning message if you try to enter negetive money
    def Withdraw(self,Amount):                                                                # Withdrawing method
        if self.__balance >= Amount:                                                       # Checking first if you have sufficient fund on your using if statement 
            
            self.__balance = self.__balance - Amount
            return f'Dear customer, ${Amount} has been debited to your account\
            new balance is {self.__balance}'
        else:
            return f'\nYou have Insufficient fund ${Amount} is above your limit. Your balance is ${self.__balance}. \nPlease deposit before you withdraw'
    @property                                           # using decorator to access the instance private balance in class
    def balance(self):
        return self.__balance
    @balance.setter                                    # using decorator setter to help in assign new value to balance as private attribute being updated
    def balance(self,update_balance):                   # condition if to check if the new balance is positive value before updating the balance
        if update_balance >= 0:
            self.__balance = update_balance
        elif update_balance < 0:
            print("Error!! It is impossible to have balance below zero")    # returning message if is negative balance want to be new update
    
    def get_balance(self):                     #Using getter method to access the private attribute initialized 
        return self.__balance 
    
    def get_name(self):                        # Getter method for access private attribute of Bank account class
        return self.__name
    def get_Acc_number(self):
        return self.__account
    def __str__(self):                                 # creating override method for returning the Bank account information
        return f'The Account detail:\n\nAccount owner: {self.__name} \nAccount number:{self.__account} \nBalance:{self.__balance}'

