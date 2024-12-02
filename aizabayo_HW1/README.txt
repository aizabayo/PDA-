# Implemention of hierachy base class

## Employee Details

Considering Employee as super class with child class Director, Manager, intern.

Employee class contain attribute which are common to  all classes:

* Name  
* Identity Number   
* Email  
* Salary.  

Method for calculating the Earning rate which will be used by all class to find the earning based on your categories.
implemented override method for printing the information detail of employee using  __str__()

Every subclass has is stored in its own py file and i imported the super class on the top of each subclass.
* Manager subclass in manegement.py file
* Director subclass in director.py file
* intern subclass in intern.py file

 The last file is file where containing instance of classes which is where if you want to run the code you can use info.py because all classes instance are imported in it.

the strucuture of class are shared in Unfied Modelling Language(UML) in the link below.

All instance of sub and supclass are in info.py file where they can be easily runned and provide the detail of each employee.

Here is the example of the code considering the intern subclass

"""Designing the intern class which is designied to show intern information and how much they\
    earned during the period of the internship, it was also inherited from super class Employee\
        to class its attribute"""
from employee import Employee                       # importing the Super class Employee inorder to interact with its property


![mukapa](UML_pda.jpg)

