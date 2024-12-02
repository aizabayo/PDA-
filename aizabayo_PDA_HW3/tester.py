"""Ïmporting the Bank account class its child class to perform polymorphism\
     and printing the the class object and function of each class"""
# importing the class modules
from account import Bank_Account
from savings import Savings_Account
from checking import Checking_Account
from credit import Credit_Card_Account

Account = Bank_Account('Daniel Jan', '21002', 1000)    # creating the instance of Bank account class            #
print(Account.Withdraw(500))                          # performing withdraw
print(Account.Deposit(300))
print(Account)                                     # displaying the account detail

Save = Savings_Account('Rodrigue de paul', '21023',3000, 15)    # creating the instance of saving account class
print(Save.Withdraw(25))
print(Save.Deposit(50))
print(Save.calculate_Interest())
print(Save)                                            # calling and return the account detail with saving account class append

Check = Checking_Account('Miguel Mike', '21200', 2500.0, 50.0)    # Creating the instance of checking account class object
print(Check.Withdraw(100))                                      # returning the function of withdraw and perform the function
print(Check.Deposit(200))
print(Check)                                              # printing the detail of checking account and accound information with overrided checking account

Card = Credit_Card_Account('Frank Davis', '21340', 5000, 6000, 100)   # creating instance of credit card account object
print(Card.Withdraw(1200))                     # example of performing withdraw and returning output
print(Card.Deposit(1500))                        # performing  deposit
print(Card.make_Purchase(300))                  # making purchase and return the result
print(Card.make_Payment(500))                  # returning the detail information of bank account and credit card account
print(Card)

Lists = [Account, Save, Check, Card]                                              #  creating the list of all instances 
for Detail in Lists:                                                               # creating loop that will iterate in all object list and return the detail
    print(Detail)