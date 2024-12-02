"""Designing the code that will serialize the the bank account object in json file with its child class detail\
    and then has the method of deserializing from json and retrieve the stored \
        Super class detail and all child class detail"""

import json                                     # importing the json module
# import the Bank account information and all inherited class
from account import Bank_Account
from savings import Savings_Account
from checking import Checking_Account
from credit import Credit_Card_Account

ACCOUNT_TYPE_MAP = {                                      # creating dictionary that will help to translate from deserialzed human readable to serialized json data
    'Bank account' : Bank_Account,
    'Saving account': Savings_Account,                     # conversion of the class names
    'Checking account': Checking_Account,
    'Credit card account': Credit_Card_Account
}
def SerializeToJson(account_obj, File = 'account.json'):       # defining the method that will perfom the function of converting account object into json format
    try:                                                    # excptional error handly to ditact the error in the code                    
        Account_type = type(account_obj).__name__           # function that deal with finding the type of the class to be used in serialization
        Data = {                                           # creating dictionary of the object's attribute in super class 
            'Account_type': Account_type,
            'Detail': {
                'Account Owner': account_obj.get_name(),
                'Account Number': account_obj.get_Acc_number(),
                'Balance': account_obj.get_balance(),
            }
        }
        # condition that will specify the type of the account and then assign on it its details or information in json format
        if Account_type == 'Savings_Account':                             
            Data['Data']['Interest rate'] = account_obj.interest_Rate
        elif Account_type == 'Checkings_Account':
            Data['Data']['Overdraft Limit'] = account_obj.overdraft_limit
        elif Account_type == 'Credit_Card_Account':
            Data['Data']['Credit Limit'] = account_obj.credit_limit
            Data['Data']['Outstanding Balance'] = account_obj.outstanding_balance
        
        with open(File, 'a') as json_file:                                                 # creating json file with append mode for allowing writing and adding the file
            json.dump(Data, json_file, separators=(',', ':'))
            json_file.write('\n')
            
        print('Account is successfully SerializedToJson')              # returning message if the conversion and creating json file has been successfully performed
        
    except Exception as e:                                              # error handler exception that return the message if there is error and the running part
        return f'Serialization error:{str(e)}'
def DeserializeFromJson(File = 'account.json'):                   # Creating the method that will deserialize json file and parse its content to new account 
    try:                                                           # usinf exception handler for handling the error
        Account_Deserialize = []                                   # creating the empty list to store the deserialized json content
        with open(File, 'r') as json_file:                        # reading the json content in read mode line by line
            for row in json_file:
                print('-->', row.strip())
                Data = json.loads(row.strip())
                Account_type = Data['Account_type']               # retrieving the Account type
                Data = Data['Detail']                              # retrieving the account details
                if Account_type in ACCOUNT_TYPE_MAP:                # checking if the file content to retrieve is json object
                    account_class = ACCOUNT_TYPE_MAP[Account_type]     # using Account type map to deserialize the json file content into readable methode
                    account_obj = account_class(
                        Data['Account Owner'],                         
                        Data['Account Number'],
                        Data['Balance']
                    )
                    if Account_type == 'Saving Account':
                        account_obj.interest_Rate = Data['Interest rate']
                    elif Account_type == 'Checking Account':                            # assigning the instance of the class object attribute
                        account_obj.overdraft_limit = Data['OVerdraft Limit']
                    elif Account_type == 'Credit Card Account':
                        account_obj.credit_limit = Data['Credit Limit']
                        account_obj.outstanding_balance = Data['Outstanding Balance']
                    
                    Account_Deserialize.append(account_obj)            # using append  to keep add the content that are being converted
        return Account_Deserialize
    except FileNotFoundError:                                           # returning the exception handler
        return 'The File not Found'

if __name__ == '__main__':                                # using main  to call the serialized and deserialized  function
     
    account1 = Credit_Card_Account('Davis Kren', '21340', 5000, 6000,450,)    # content to be serialized 
    serialize_result1 = SerializeToJson(account1)
    print(serialize_result1)


    # Deserialize the account objects from JSON
    Account_Deserialize = DeserializeFromJson()
    if Account_Deserialize:
        for account in Account_Deserialize:
            print(json.dumps(account, default=lambda x: x.__dict__, separators=(',', ':')))
    else:
        print("")
   
                        
                    