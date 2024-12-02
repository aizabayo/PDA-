"""The file that contain the instance of superclass and all subclass to display the \
      class function and property"""
import json
from employee import Employee
from management import Manager
from director import Director
from interns import Intern
#Creating the instance of the super class Employee and of other subclasses to be return
Emp = Employee('215003','Francis', 'Mutwe', 'mutwefrancis@gmail.com', 5000)
print(Emp)
management = Manager('213045', "Daniel", "Kalisa", "kalisadaniel@milinda.com", 15000, "Plant Manager", 5,10)
print(management)
directory = Director('213040', "Frank", "James", "jamesfrank@milindi.com", 25000, "Finance", 5000)
print(directory)
interm = Intern('10089', "Jan", "levikson", "ljan@andrew.cmu.edu", 5000, "CMU Africa", "Electrical and Computer Engineering", 6, '02-02-2023', '01-07-2023', 'Intern')
print(interm)
info_detail = [Emp, management, directory, interm]          #declare info_detail as list to store the instance of classes
# creating loop to iterate in each element of the class whose instances stored in list
for detail in info_detail:
      print(detail)