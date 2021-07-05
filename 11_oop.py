'''
29 WHAT IS OBJECT ORIENTED PROGRAMING ?
ans : Object-Oriented Programming(OOP), is all about creating “objects”. 
    An object is a group of interrelated variables and functions. 
    These variables are often referred to as properties of the object and functions are referred to as the behavior of the objects.
    "reuseable code"
    Almost everything in Python is an object, with its properties and methods.

    A Class is like an object constructor, or a "blueprint" for creating objects.

'''
class programar:
    company ="microsoft "
    salary =  50000 
    workplace = "bombay "

    def greet(self):
          print("good morning everyone")
    
    @staticmethod
    def greets():
        print("good morning everyone")

    
    def __init__(self, name, product):
        self.name = name
        self.product = product
  

    def getinfo(self):
        print(f"name = {self.name} product = {self.product}  ")
 

keyur = programar("keyur","website")
keyur.greet()
keyur.greets()
print(keyur.company)
print(keyur.salary)
print(keyur.workplace)    

keyur.getinfo()
