"""Designing credit card account class that will inherit from Bank account class perfome the operation\
    of purchasing and payment method using the credit card and has limit on the amout to use\
        use outstand balance to be paid and remove from the balance"""
from account import Bank_Account                         #calling the super class information
 
class Credit_Card_Account(Bank_Account):                  # creating credit card account as child class
    def __init__(self, Owner_name, Account_number, Current_balance, credit_limit, outstanding_balance):          #Using init method to initialize new attribute
        super().__init__(Owner_name, Account_number, Current_balance)                                           # calling init method from super class
        self.__credit_limit = credit_limit                                               # declaring new attribute as private attribute
        self.__outstanding_balance = outstanding_balance                                 # declaring outstanding balance
    @property                                                                           # use decorator to easily access property of private attribute
    def credit_limit(self):                                                            # defining method that will get the property of private feature
        return self.__credit_limit
    @property
    def Outstanding_balance(self):
        return self.__outstanding_balance
    def make_Purchase(self, Amount):                                          # creating make purchase methode with instance amount
        Max_credit = self.get_balance() - self.__outstanding_balance          # Calculating the amount available to the credit card after paying debt if is sufficient to make purchase 
        if Amount <= Max_credit:                                                # condition statement if the credit card balance is greater than the amount the purchase operation will continue
            self.__outstanding_balance = self.__outstanding_balance + Amount
            return f'Your purchase is accepted amount $ {Amount}\
                the Outstanding balance is ${self.__outstanding_balance}'   
        else:
            return f'Sorry the Purchase Amount Exceed available Amount.'              # if the credit amount is less than the amount to make purchase will diplay the message that action is not failed.
    def make_Payment(self, Amount):                                                  # defining the make payment 
        if Amount >= 0 and Amount <= self.__outstanding_balance:                     # check if the amount to pay is non negative and if the amount to pay does not exceed what we are suppossed to pay 
            self.__outstanding_balance = self.__outstanding_balance - Amount
            return f'Your payment of ${Amount} is successfully. \
                the Outstanding balance is ${self.__outstanding_balance}'                #If the  condition meet pay the debt 
        elif Amount < 0:
            return 'Error. Negative amount does not exist'                                  # if the amount is negative value do not pay display the message
        else:
            return 'The payment exceed what we owe or debt'                         # if the amount exceed the debt we have displat also the message
              
        
    def __str__(self):                                                              # using the override methode to display the super class inform with the status of credit card
        return super().__str__()+ f'Credit Card Account Detail:Credit Card Limit: ${self.__credit_limit}'
